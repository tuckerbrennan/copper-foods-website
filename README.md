# Copper Foods — Website Concept

A mobile-first presentation website for **Copper Canyon**, **Higo**, and **Gaslight** in Atlantic Highlands, NJ. This is a stakeholder prototype for Michael, **not an approved production launch**. A dedicated Copper Canyon page has been added.

## Files

- `index.html`: group homepage with venue sections, lunch announcement, and directions
- `copper-canyon.html`: dedicated Copper Canyon page with links to digital menus, reservations, online ordering, gift cards, gallery, hours, directions, and event-contact CTA
- `copper-canyon-menus.html`: searchable HTML content organized into Lunch, Dinner, and one shared Drinks menu; deep links `#lunch`, `#dinner`, `#drinks`
- `copper-canyon-menus.css`, `copper-canyon-menus.js`: responsive menu layout and progressive-enhancement selector
- `data/copper-canyon-menu.json`: structured food and drink source with separate service prices
- `copper-canyon.css`, `copper-canyon.js`: venue-specific styling and gallery lightbox
- `docs/copper-canyon-site-audit.md`: detailed crawl of the original site and functional-parity checklist
- `docs/copper-canyon-menu-transcription.md`: photo sources, reviewed item counts, shared drinks rule, and verification gaps
- `styles.css`: responsive design system
- `app.js`: accessible mobile navigation and current copyright year

Built as plain HTML, CSS, and JavaScript; no build step or credentials.

## Preview

GitHub Pages is enabled for the `main` branch. Preview URLs:

- https://tuckerbrennan.github.io/copper-foods-website/
- https://tuckerbrennan.github.io/copper-foods-website/copper-canyon.html
- https://tuckerbrennan.github.io/copper-foods-website/copper-canyon-menus.html#lunch
- https://tuckerbrennan.github.io/copper-foods-website/copper-canyon-menus.html#dinner
- https://tuckerbrennan.github.io/copper-foods-website/copper-canyon-menus.html#drinks

Deployment is asynchronous; Pages URLs may briefly show an old version while the latest commit deploys. The repository and its preview are public.

## Confirm before public launch

- **Photography:** Food, drinks and restaurant photos currently come from Unsplash and are **illustrative placeholders**; they are not photos of the restaurants. Replace with approved restaurant photography.
- **Brand identity:** Replace the draft text wordmark and add the real transparent restaurant logos.
- **Facts:** Confirm addresses, operating hours, copy, phone, menu availability, and reservation links with Michael. Current draft lists Copper Canyon and Higo at 51 First Avenue; Gaslight at 33 First Avenue.
- **Functional parity:** Copper Canyon now provides external links for booking, ordering, and gift cards, but checkout, reservation availability, and the Yelp URL remain **untested**. The old contact/private-party form has **not yet been migrated** because its delivery destination is unknown; the new page provides a working telephone CTA in the meantime.
- **Links:** Copper Canyon's website and Copper Foods / Gaslight Linktree pages are linked. Add independently verified direct menu and reservation URLs.
- **Site readiness:** Review mobile behavior, accessibility, venue-specific pages, events, and privacy/legal requirements.

## Proposed roadmap

1. Review homepage direction with Michael.
2. Collect approved brand assets and photos.
3. Verify and sign off on the new Copper Canyon lunch, dinner and **shared** drinks menus (see transcription doc); test on mobile.
4. Add separate pages for Higo and Gaslight, plus an events listing.
5. Verify links, hours, and calls to action.
6. Obtain Michael's approval before any restaurant-domain cutover.
