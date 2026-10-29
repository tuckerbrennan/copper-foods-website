# Copper Canyon menu transcription & QA

Updated: October 29, 2026

## Source materials (user-uploaded photos)

- Lunch launch menu: `IMG_9936.jpeg`
- Dinner small plates: `IMG_9938.jpeg`
- Dinner large plates, sides, and policy disclosure: `IMG_9939.jpeg`
- Margaritas, wine, and beer: `IMG_9940.jpeg`

The original photos were supplied in this chat; they are **not** committed to the public website repository.

## Files

- `data/copper-canyon-menu.json`: structured source for editable menu items, categories, descriptions, and prices
- `copper-canyon-menus.html`: fully rendered, accessible, crawlable HTML menu, with Lunch / Dinner / Drinks navigation
- `copper-canyon-menus.css`: typography, mobile/desktop layout, sticky menu selector
- `copper-canyon-menus.js`: progressive-enhancement section switcher; without JavaScript all menu sections are shown

## Content audit

- Lunch: **24 dishes** across four editorial groupings.
- Dinner: **21 small plates**, **14 large plates**, **9 sides & salsas** = **44 entries**.
- Drinks: **5 margaritas**, **8 wines**, **4 draft/domestic beers**, **6 imported bottled beers**, **1 ready-to-drink beverage** = **24 entries**.
- The **same canonical Drinks menu** is linked from Lunch and Dinner. Prices do not differ by service.
- The lunch chicken quesadilla is **$14, without mango-pineapple salsa**; the dinner chicken quesadilla is **$28, with mango-pineapple salsa**, matching the two uploaded menus.
- Chicken or shrimp posole soup appears with separate lunch (**$7 / $9**) and dinner (**$9 / $11**) prices.
- Beer & margarita pricing uses the drink-page photograph, with no assumed lunch discounts.
- The dinner photo's disclosures (3% credit-card processing fee, 20% automatic gratuity for six or more) are displayed under Dinner.

## Items needing management confirmation

1. **Dinner small plates photo is cropped on its right edge.** There may be other dishes not fully visible in the photograph. Only completely legible entries were added.
2. **Rosé bottle** is shown for **$48** but its producer isn't legible/identified. Site wording asks customers to inquire about the current selection.
3. Confirm current wine vintages, beer inventory, and all other menu prices before removing the website-preview disclaimer.
4. Confirm hours and whether the dinner menu's fee/gratuity disclosures also need to appear on lunch and drinks.
5. The old takeout menu appears dated. A legacy takeout link is retained pending newer takeout copy or ordering-provider validation.

## User-specified requirement

On October 29, 2026, user explicitly requested that **lunch drinks include all beers, wines, and margaritas at the same prices as dinner for the time being**. Treat this as a standing requirement until the user changes it.

## Spot-checks performed

- Exact menu entries, descriptions, and price strings checked against the structured source.
- Local CSS and JS references checked for repository presence.
- Internal section links and Lunch / Dinner / Drinks deep links checked.
- HTML section/article/div tags and CSS braces checked for balance.
- **Not yet performed:** live browser/device QA, reservation booking, order checkout, gift-card payment, or final approval by Michael.
