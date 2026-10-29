# Copper Canyon website — public-site functional audit

Audited: October 29, 2026  
Source: [www.thecoppercanyon.com](https://www.thecoppercanyon.com/) and its linked public pages.  
Scope: externally visible pages and links. No authenticated Wix access, orders, payments, or form submissions were performed.

## Essential migration checklist

| Feature | Observed on current site | Required in replacement | Priority | Verification |
|---|---|---|---|---|
| Home / about | Home page, About section, chef/owner Michael Krikorian history, signature food, tequila description | Branded restaurant landing page; about/story content | Must | Content review with Michael |
| Table reservations | Home CTA linked to Yelp Reservations widget (see problem below) | Visible Reserve button linking to verified live reservation flow, plus phone fallback | Must | **Open a test booking and ensure Yelp hours/availability configured** |
| Online ordering | Top navigation to order.online business; separate home order link to orderthecoppercanyon.com | Pickup / delivery CTA(s) directing to operational services | Must | Verify restaurant, menu, ordering hours, pickup/delivery and checkout |
| Gift cards | Loopz gift-card checkout link on home | Buy a Gift Card button; external checkout | Must | Test product/page accessibility and payment with management |
| Dine-in menu | Dedicated page with menu page images rather than accessible text | Direct access initially; later HTML searchable menu + downloadable current PDF | Must | Verify menu versions/prices and new lunch menu |
| Takeout menu | An accessible /takeout-menu page is live, with image named Carryout_Delivery Menu 2022 | Dedicated pickup/delivery menu access | Must | **2022 image may be outdated** |
| Beer & wine menu | Dedicated /copy-of-takeout-menu image page | Drinks / Beer & Wine section or link; new menu asset | Must | Confirm current stock and selections |
| Photos/gallery | Dedicated /gallery; homepage venue photo thumbnails labelled Main Dining Room, Bar, Tequila Bar, Outdoor Patio | Clickable photo gallery with categories and accessible descriptions | Should | Replace placeholders with approved venue photography |
| Private parties / inquiries | Homepage "PRIVATE PARTIES" callout and contact form with First Name, Last Name, Email, Phone | Event inquiries and management-routed form | Must | **Wix form destination and notification workflow not verifiable publicly** |
| Contact | Address 51 First Avenue, Atlantic Highlands, NJ 07716; (732) 291-8444; form | Click-to-call, map/directions, accessible contact info, inquiries | Must | Verify correct contact destination |
| Social | Linked Instagram and Facebook | Social links in header/footer | Should | Verify account ownership and exact handles |
| Experiences | /experiences page reads "We're not offering any experiences at the moment" | Optional events/experiences page; do not promote nonexistent events | Later | Confirm upcoming schedule |
| Review/press | NYT restaurant-review link from homepage | Optional press/recognition section | Later | Verify rights and current link |
| Mobile / accessibility / SEO | Existing Wix site with image-only menu sections | Mobile-friendly navigation, meaningful alt text, structured menu HTML, local SEO, accessibility | Must | Manual browser and accessibility QA |
| Hours | Website homepage says "OPEN DAILY 4pm CLOSED SUNDAY" | Make current lunch service prominent; publish approved actual operating hours | Must | **Homepage contradicts new lunch service** |

## Verified source URLs and observed behavior

- Homepage / About / Contact: https://www.thecoppercanyon.com/
- Dine-in menu: https://www.thecoppercanyon.com/copy-of-take-out-menu
- Takeout menu (found via direct URL, not clearly in main navigation): https://www.thecoppercanyon.com/takeout-menu
- Beer and wine menu: https://www.thecoppercanyon.com/copy-of-takeout-menu
- Photo gallery: https://www.thecoppercanyon.com/gallery
- Experiences: https://www.thecoppercanyon.com/experiences — currently no offerings displayed
- Online order, main navigation: https://order.online/business/copper-canyon--51-1st-ave-14146713 — automated public request encounters security/loading screen, **not validated as a complete customer checkout**.
- Online order, secondary/home CTA: https://www.orderthecoppercanyon.com/ — ordering site loads a cart shell, but dynamic menu/checkout not verified.
- Gift cards: https://my.loopz.io/gift-card/d4568136-585d-4129-941e-ec1863cd267f?locale=en-US — linked checkout; could not independently validate transactional flow.
- Yelp reservation link seen on original homepage: https://www.yelp.com/reservations/copper-canyon-atlantic-highlands/widget?color-scheme=light%22&orientation=vertical — includes a stray encoded quotation mark (`%22`) and did not load in automated inspection. Candidate clean landing URL: https://www.yelp.com/reservations/copper-canyon-atlantic-highlands **must be tested with a browser/management account**.
- Instagram (linked from home): https://www.instagram.com/thecoppercanyon/
- Facebook (linked from home): https://www.facebook.com/thecoppercanyon
- NYT review (linked): https://www.nytimes.com/2011/05/29/nyregion/the-copper-canyon-restaurant-review.html?_r=3

## Site information / draft content

- Address: 51 First Avenue, Atlantic Highlands, NJ 07716
- Phone: (732) 291-8444
- Chef/owner: Michael Krikorian
- Signature items named on website: Southwestern Crab Cakes, NY Strip Steak, Spring Rolls; margaritas and tequila collection.
- New schedule supplied by restaurant project (confirm with management before launch): Monday–Friday 12 PM–9 PM; Saturday 4 PM–9 PM; Sunday closed.
- Existing public homepage still advertises a 4 PM opening and older menu files. Do not uncritically transfer out-of-date text, prices, opening times or menus.

## Build strategy

### Phase A — functional parity on a new Copper Canyon page
1. Hero with **Reserve**, **Order Online**, **View Menus**, **Call** actions.
2. Distinct Dine-In / Takeout / Beer & Wine menu links until current, text-based menus are approved.
3. Gift-card link and private-event inquiry CTA.
4. Phone, directions, hours, social links.
5. Short story and illustrative photo gallery.
6. Existing external platforms remain responsible for booking, payment, ordering and fulfillment; don't collect payment/card information on the new site.

### Phase B — replacement and QA
1. Obtain current lunch/dinner/drinks menus (prefer source editable or quality PDF).
2. Replace stock photos with genuine approved photos and official logos.
3. Verify Yelp setup (reservations may be unavailable on some dates), DoorDash/Order Online provider, alternate ordering site, and Loopz gift-card checkout.
4. Recreate contact/private-events form using a confirmed recipient/backend (Wix form settings or replacement service). **Do not publish a form that appears to submit but silently discards inquiries.**
5. Verify exact published hours, branding/tequila-count claims, SEO and mobile functionality.
6. Test all links end-to-end on iPhone and desktop, including a test inquiry and successful reservation availability routing.

## Deliberate limitations

This is a public-page crawl, **not** a login to Wix or to ordering/reservation/gift-card dashboards. It cannot prove that transactions, form notifications, or current Yelp table availability work. Third-party services may be JS-loaded or block automated access. No transactions were attempted.

The new site can preserve outgoing third-party links right away, but true feature parity for forms and commercial flows requires live provider validation.
