#!/usr/bin/env python3
"""Archive public image files referenced by the official Copper Canyon website.

Runs on GitHub Actions so outbound HTTP requests originate from the hosted runner.
Does not require credentials or download anything behind authentication.
Only crawls thecoppercanyon.com and only downloads public Wix media image URLs.
"""
from __future__ import annotations

import csv
import hashlib
import html
import os
import re
import sys
import time
from collections import deque
from pathlib import Path
from urllib.parse import urljoin, urlparse, urlunparse

import requests
from bs4 import BeautifulSoup

SITE = "https://www.thecoppercanyon.com"
OUTPUT = Path("copper-canyon-site-archive")
IMAGES = OUTPUT / "images"
MAX_PAGES = 35
MAX_IMAGES = 500
MAX_FILE_BYTES = 35 * 1024 * 1024
MAX_TOTAL_BYTES = 500 * 1024 * 1024
TIMEOUT = (12, 35)

# This list is the 22-item site inventory previously established by inspection.
# It is supplemented with every further image link found during the crawl.
SEED_IDS = [
    "fb6df9_c9702d12a1c1456aaa371bfe033fb192~mv2.png",
    "fb6df9_eeebc62b908046e7bf68acf9f2424cd3~mv2.png",
    "e63476_57ca95920983499cbf629623efe0999d~mv2_d_3648_2736_s_4_2.jpg",
    "e63476_531fa30ea58046dc9dc5e93a76f28fe1~mv2_d_1920_1300_s_2.jpg",
    "e63476_a669cc2403014a5e8ad4366bf65b64a6~mv2.jpg",
    "e63476_91236addfa0442468146ce39d5286ea7~mv2.jpg",
    "e63476_d3d4c1aa33844320ade977428e7abbaa~mv2.jpg",
    "e63476_3db1b55fbccb4023b93a0590e4c95827~mv2.jpg",
    "e63476_f891fe74e7034b5ea18d154238a6a593~mv2.jpg",
    "fb6df9_fa8925a3d3ab4259be223478e0044bae~mv2.jpeg",
    "fb6df9_c9fe35ca4de94d00b6b09f231d5919df~mv2.jpeg",
    "fb6df9_0efc501e3bb5418082e0a38e8def46c3~mv2.jpeg",
    "fb6df9_4b118717ab9f4e9e8400344185e0d9aa~mv2.jpeg",
    "fb6df9_4c8abbf6cc124009acbc8b3db1347274~mv2.jpeg",
    "fb6df9_b0a5eff689b0418a9078d6c275bf8fc6~mv2.jpeg",
    "fb6df9_628c3c684f0a4bea9ab6a24cca4504fc~mv2.jpeg",
    "fb6df9_8f3a3c2cf2fd45bfa88c7e36beff68d5~mv2.jpg",
    "fb6df9_a029ef80abe74846b060cf85f3efecfb~mv2.jpg",
    "fb6df9_12a734b35083421a8508f284875f7722~mv2.jpg",
    "e63476_c1956c8dc4084ba8a536eaf44a9098d9~mv2.jpg",
    "fb6df9_9f6e4a52f96e434b899e26a86f9d3edd~mv2.png",
    "fb6df9_2f06c45323724de9b1f2e0afd80fbb02~mv2.png",
]

START_PAGES = [
    SITE + "/",
    SITE + "/gallery",
    SITE + "/dine-in-menu",
    SITE + "/copy-of-take-out-menu",
    SITE + "/takeout-menu",
    SITE + "/beer-and-wine",
    SITE + "/copy-of-takeout-menu",
    SITE + "/experiences",
]

MEDIA_RE = re.compile(
    r"(?:(?:https?:)?//static[.]wixstatic[.]com)?/media/"
    r"([a-zA-Z0-9_~.-]+[.](?:jpg|jpeg|png|gif|webp|svg|avif|bmp))",
    re.IGNORECASE,
)
WIX_IMAGE_RE = re.compile(
    r"wix:image://v1/([a-zA-Z0-9_~.-]+[.](?:jpg|jpeg|png|gif|webp|svg|avif|bmp))",
    re.IGNORECASE,
)
IMAGE_MIME = {"image/jpeg", "image/png", "image/webp", "image/gif", "image/svg+xml",
              "image/avif", "image/bmp", "image/x-icon"}
HTML_EXTENSIONS = {".html", ".htm", ""}


def normalized_markup(markup: str) -> str:
    return html.unescape(markup).replace(r"\/", "/").replace(r"\u002F", "/").replace(
        r"\u003A", ":"
    ).replace(r"\u002f", "/").replace(r"\u003a", ":")


def site_page(url: str) -> str | None:
    parsed = urlparse(urljoin(SITE, url))
    if parsed.scheme != "https" or parsed.hostname not in {
        "thecoppercanyon.com", "www.thecoppercanyon.com"
    }:
        return None
    if Path(parsed.path).suffix.lower() not in HTML_EXTENSIONS:
        return None
    if any(t in parsed.path.lower() for t in ["/account", "/login", "/checkout", "/members"]):
        return None
    return urlunparse(("https", "www.thecoppercanyon.com", parsed.path or "/", "", "", ""))


def extract_image_ids(markup: str) -> set[str]:
    body = normalized_markup(markup)
    return {m.group(1) for m in MEDIA_RE.finditer(body)} | {
        m.group(1) for m in WIX_IMAGE_RE.finditer(body)
    }


def looks_like_image(blob: bytes, content_type: str) -> bool:
    ctype = content_type.split(";")[0].strip().lower()
    if ctype not in IMAGE_MIME:
        return False
    if blob.startswith((b"\xff\xd8\xff", b"\x89PNG\r\n\x1a\n", b"GIF87a", b"GIF89a",
                        b"RIFF", b"\x00\x00\x00")):
        return True
    if ctype == "image/svg+xml" and b"<svg" in blob[:5000].lower():
        return True
    return False


def download_image(session: requests.Session, filename: str, known_from: list[str],
                   already_bytes: int) -> tuple[dict[str, str], int]:
    source_url = "https://static.wixstatic.com/media/" + filename
    row = {"filename": filename, "url": source_url,
           "source_pages": " | ".join(known_from),
           "status": "", "bytes": "0", "sha256": "", "error": ""}
    if already_bytes >= MAX_TOTAL_BYTES:
        row["status"], row["error"] = "skipped", "archive size cap reached"
        return row, 0
    try:
        with session.get(source_url, stream=True, timeout=TIMEOUT) as response:
            response.raise_for_status()
            ctype = response.headers.get("Content-Type", "")
            buf = bytearray()
            for part in response.iter_content(chunk_size=128 * 1024):
                if part:
                    buf.extend(part)
                if len(buf) > MAX_FILE_BYTES:
                    raise ValueError("image exceeds per-file size cap")
                if len(buf) + already_bytes > MAX_TOTAL_BYTES:
                    raise ValueError("archive size cap reached")
            content = bytes(buf)
            if not looks_like_image(content, ctype):
                raise ValueError("not image bytes (content-type: " + ctype + ")")
            safe_name = Path(filename).name
            (IMAGES / safe_name).write_bytes(content)
            row.update(status="downloaded", bytes=str(len(content)),
                       sha256=hashlib.sha256(content).hexdigest())
            return row, len(content)
    except Exception as exc:
        row.update(status="failed", error=str(exc)[:250])
        return row, 0


def main() -> None:
    IMAGES.mkdir(parents=True, exist_ok=True)
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (compatible; CopperFoodsMediaArchive/1.0; "
                      "+https://www.thecoppercanyon.com/)",
        "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    })

    image_sources: dict[str, set[str]] = {
        fid: {"prior-site-inventory"} for fid in SEED_IDS
    }
    frontier = deque(START_PAGES)
    visited: set[str] = set()
    pages: list[dict[str, str]] = []

    while frontier and len(visited) < MAX_PAGES:
        page = site_page(frontier.popleft())
        if not page or page in visited:
            continue
        visited.add(page)
        print("Crawl:", page, flush=True)
        try:
            response = session.get(page, timeout=TIMEOUT)
            response.raise_for_status()
            if "text/html" not in response.headers.get("Content-Type", "").lower():
                raise ValueError("not an HTML page")
            markup = normalized_markup(response.text)
            found = extract_image_ids(markup)
            for fid in found:
                image_sources.setdefault(fid, set()).add(page)
            soup = BeautifulSoup(markup, "html.parser")
            for element in soup.find_all(["a", "link"]):
                href = element.get("href", "")
                if href:
                    next_page = site_page(href)
                    if next_page and next_page not in visited:
                        frontier.append(next_page)
            pages.append({"url": page, "status": "downloaded",
                          "image_references": str(len(found)), "error": ""})
        except Exception as exc:
            pages.append({"url": page, "status": "failed",
                          "image_references": "0", "error": str(exc)[:250]})
            print("Page error:", exc, file=sys.stderr, flush=True)
        time.sleep(0.4)

    rows: list[dict[str, str]] = []
    total_bytes = 0
    all_ids = sorted(image_sources)
    print("Found", len(all_ids), "unique original-media image references", flush=True)
    for index, filename in enumerate(all_ids[:MAX_IMAGES], 1):
        row, downloaded = download_image(
            session, filename, sorted(image_sources[filename]), total_bytes
        )
        rows.append(row)
        total_bytes += downloaded
        print(f"{index}/{min(len(all_ids), MAX_IMAGES)} {row['status']} "
              f"{filename} ({downloaded} bytes)", flush=True)
        time.sleep(0.25)

    for filename in all_ids[MAX_IMAGES:]:
        rows.append({"filename": filename,
                     "url": "https://static.wixstatic.com/media/" + filename,
                     "source_pages": " | ".join(sorted(image_sources[filename])),
                     "status": "skipped", "bytes": "0", "sha256": "",
                     "error": "maximum image count reached"})

    with (OUTPUT / "image_manifest.csv").open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=[
            "filename", "url", "source_pages", "status", "bytes", "sha256", "error"
        ])
        writer.writeheader()
        writer.writerows(rows)

    with (OUTPUT / "page_manifest.csv").open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=[
            "url", "status", "image_references", "error"
        ])
        writer.writeheader()
        writer.writerows(pages)

    downloaded = sum(r["status"] == "downloaded" for r in rows)
    failed = sum(r["status"] == "failed" for r in rows)
    summary = (
        "Copper Canyon public-website media archive\n"
        "Source: https://www.thecoppercanyon.com/\n"
        "Saved as original-resolution image bytes wherever the CDN permitted.\n"
        f"Pages checked: {len(pages)}\n"
        f"Unique image URLs discovered: {len(all_ids)}\n"
        f"Image files downloaded: {downloaded}\n"
        f"Failed downloads: {failed}\n"
        f"Total bytes downloaded: {total_bytes}\n"
        "Images are retained with the original Wix media filenames.\n"
        "Manifest includes provenance and HTTP errors for missing assets.\n"
        "This is an authorized public-site archive, not a Wix Media Manager export.\n"
        "Verify reuse rights, menu currency, and full-resolution fidelity before publishing.\n"
    )
    (OUTPUT / "README.txt").write_text(summary, encoding="utf-8")
    print(summary, flush=True)

    # Do not report an empty archive as success.
    if not downloaded:
        sys.exit("No image bytes could be retrieved from the Wix media CDN")


if __name__ == "__main__":
    main()
