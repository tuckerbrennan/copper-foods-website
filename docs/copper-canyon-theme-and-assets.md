# Copper Canyon visual identity & legacy media inventory

Updated: October 29, 2026

## Source

Original website: https://www.thecoppercanyon.com/  
Website gallery: https://www.thecoppercanyon.com/gallery  
Project Drive folder (personal account **tucker.t.brennan@gmail.com**): https://drive.google.com/drive/folders/1qQWBS7sWwLyLCPDmZy_UF5QRqDVHDPWe

## Branding

The original website shows a black-lettered Copper Canyon horseshoe logo. A photograph of the newer printed lunch menu supplied by the restaurant shows black script lettering with a muted copper-red horseshoe on warm off-white paper.

The original site did not yield downloadable CSS values. This is a **brand-informed approximation**, not a verified pixel-perfect reproduction of Wix CSS.

### Design palette (Copper Canyon only)

| Token | Hex | Usage |
|---|---|---|
| Charcoal / dark cocoa | `#241A18` | Navigation/footer backgrounds |
| Deep espresso | `#31201E` | Dark accents |
| Copper-red | `#8F5143` | Prices and small accents on light backgrounds |
| Warm terracotta | `#C28E75` | Lunch callout panels |
| Light copper | `#D6A183` | Accent on dark surfaces |
| Parchment | `#F8F1E8` | Page backgrounds |
| Warm white | `#FAF6EF` | Reading surfaces |
| Soft sepia | `#EEE3D5` | Menu-feature background |

Typography: Cormorant Garamond (display), DM Sans (navigation, prices and body text). Original handwritten logo artwork remains an image, not a recreated text wordmark.

Styles are scoped to `.cc-site` and `.cc-menu-site` in `copper-canyon-theme.css`. Copper Foods parent branding, Higo and Gaslight are intentionally unchanged.

## Asset inventory

The private Google Drive folder includes:
- `Copper_Canyon_Transparent_Logo.png`: previously supplied **black-and-white** logo copy (actual PNG stored).
- `Copper_Canyon_Menu_Brand_Reference.jpg`: crop from the restaurant's supplied lunch-menu photo showing the copper-red logo (actual JPEG stored; not a website download).
- `Copper_Canyon_Original_Website_Asset_Inventory.csv`: **22 original Wix URL references**: logos, labeled photos, gallery photos, older menu scans and other graphics.
- `Copper_Canyon_Website_Assets_README.md`: archive notes and migration instructions.

**Original Wix image files were not downloaded**: requests to `static.wixstatic.com` through the available transfer tools did not return usable binary files. The direct original CDN URLs were recorded instead. This is a partial asset migration, not a claim that all the website photos are safely backed up.

## Images now referenced in the prototype

The Copper Canyon pages temporarily reference these exact first-party website photo URLs via `<img>` tags:

- Original logo: https://static.wixstatic.com/media/fb6df9_c9702d12a1c1456aaa371bfe033fb192~mv2.png
- Main dining room: https://static.wixstatic.com/media/e63476_a669cc2403014a5e8ad4366bf65b64a6~mv2.jpg
- Bar area: https://static.wixstatic.com/media/e63476_91236addfa0442468146ce39d5286ea7~mv2.jpg
- Tequila bar: https://static.wixstatic.com/media/e63476_d3d4c1aa33844320ade977428e7abbaa~mv2.jpg
- Outdoor patio: https://static.wixstatic.com/media/e63476_3db1b55fbccb4023b93a0590e4c95827~mv2.jpg
- More bar selections: https://static.wixstatic.com/media/e63476_f891fe74e7034b5ea18d154238a6a593~mv2.jpg

These are **hotlinks**, not downloaded/local copies. If image retrieval fails in the browser, the image element falls back to existing illustrative imagery. Confirmation on a real phone/browser remains required. These links should not be treated as a permanent hosting solution.

## Completion steps

1. Ask Michael for Wix Media Manager access or a full-quality media export; recover the real JPG/PNG originals to the Drive folder.
2. Obtain explicit approval to reuse all source photos and logos.
3. Replace CDN hotlinks and Unsplash fallback images with approved, locally stored photography in the GitHub repository.
4. Review the Copper Canyon theme on iPhone and desktop.
5. Verify the menu entries/prices, operating hours, ordering, reservations and inquiry functionality already documented in the site audit.
6. Approve and publish restaurant-specific branding only after management review.
