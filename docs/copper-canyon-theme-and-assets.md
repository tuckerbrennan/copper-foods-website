# Copper Canyon visual identity & original-site image migration

Updated: October 30, 2026 — **presentation pass**

## Website sources and archives

- Original website: https://www.thecoppercanyon.com/
- Original restaurant gallery: https://www.thecoppercanyon.com/gallery
- **Personal** Google Drive folder: https://drive.google.com/drive/folders/1qQWBS7sWwLyLCPDmZy_UF5QRqDVHDPWe
- Archived original restaurant files (32 images): https://drive.google.com/drive/folders/1ZypQCdOp-fW3tI3ZIGz4fC2wF9hfEyyq
- Original image URL & checksum manifest: saved in that archive as `image_manifest.csv`
- Locally hosted website assets: [`assets/copper-canyon/`](../assets/copper-canyon/README.md) — **14 real original-site files**

## Brand palette

The existing restaurant site's horseshoe logo uses black lettering and a copper-colored horseshoe on transparent/white background. The newer printed lunch menu shows a muted copper-red horseshoe on warm off-white paper.

The working palette is inspired by these supplied sources, not an exact audited Wix CSS extraction.

| Token | Color | Use |
|---|---|---|
| Deep cocoa | `#241A18` | Navigation, footers |
| Espresso | `#31201E` | Dark accents |
| Copper red | `#8F5143` | Prices and small accents |
| Warm terracotta | `#C28E75` | Lunch callout |
| Light copper | `#D6A183` | Accents over dark |
| Parchment | `#F8F1E8` | Pages |
| Warm white | `#FAF6EF` | Reading panels |
| Soft sepia | `#EEE3D5` | Menu sections |

Typography: Cormorant Garamond for display headings and DM Sans for body/interface text. The true horseshoe logo is displayed as a locally stored image, not recreated.

## Migration result

1. The first public-site crawl downloaded **32 image files totaling 11,844,613 bytes**, from **33 discovered images across 8 pages**. One non-essential remote graphic returned HTTP 403.
2. The files were archived with full filenames, checksums and URL origins in the correct personal Google Drive account (**tucker.t.brennan@gmail.com**).
3. We visually inspected real restaurant, bar, patio, and food photography.
4. **Fourteen selected image files**, including the original Copper Canyon horseshoe logo, were copied **byte-for-byte** into the GitHub repository.
5. The Copper Canyon landing page and digital menus now load their imagery directly from `assets/copper-canyon/`. No external Wix or Unsplash image URLs remain in the served HTML.
6. The group homepage shows actual Copper Canyon photos for Copper Canyon only. Higo and Gaslight have attractive typography-and-CSS graphic panels, **not** photos purporting to show those venues.
7. Instagram `@thecoppercanyon` did not return publicly accessible image content in the unauthenticated crawl. **Zero Instagram photos** were used; no claim of an Instagram archive is made.

## Still required for production

- Review image choices and photo reuse authorization with Michael.
- Provide Higo and Gaslight real images and official logos.
- Confirm updated menus, reservations, ordering, gift-card functionality, hours, and the private-party contact route.
- Check the site at desktop/tablet/iPhone viewport sizes and approve before pointing the real restaurant domain at this draft.

**Important:** The GitHub Pages presentation is public; it should remain a stakeholder demo, not be mistaken for the fully approved restaurant website.
