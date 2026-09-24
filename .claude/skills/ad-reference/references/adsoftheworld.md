# Ads of the World: site reference

Checked 2026-09-24 by CreativeEngine (WebFetch, built-in browser). Re-check if a URL stops working.

## Ownership and terms

- Ads of the World (adsoftheworld.com) was founded by Ivan Raszl in 2005 and is owned and operated by Clio Awards LLC (site FAQ).
- The site's `/legal` page points to the Clio terms at `https://clios.com/terms-use`, which list adsoftheworld.com as a covered site.
- The use license allows temporarily downloading one copy for **personal, non-commercial, transitory viewing only**. It forbids using the materials for any commercial purpose or public display, removing proprietary notices, and transferring or "mirroring" the materials on another server.
- **What this means for us:** view ads on the site; store only links, bibliographic facts and our own analysis; never save images or copy the site's text into the repo or client work. The terms don't mention automated access, scraping or AI specifically, so keep automated reading light and task-driven.

## robots.txt (as of 2026-09-24)

Disallowed for all user agents: `/healthcheck.html`, `/admin_dashboard`, `/campaigns_admin_index`, `/slides`, `/merge`, `/settings`, `/tags`, `/watchlist`, `/follows`, `/bookmarked`, `/*?page=`, `/default_image.psd`. Sitemap: `https://www.adsoftheworld.com/sitemap.xml.gz`.

**Never request a `?page=` URL.** Narrow with keywords and filters instead.

## URL patterns

| What | Pattern |
|---|---|
| Campaign | `/campaigns/<slug>` |
| Search | `/campaigns?search=<terms>` (spaces as `+`) |
| Search with filters | `/campaigns?search=<terms>&medium_type_ids[]=<id>&industry_ids[]=<id>` (repeat a parameter for several values) |
| Medium listing | `/medium_types/<name>` (e.g. `/medium_types/print`, about 35,000 print campaigns) |
| Industry listing | `/industries/<slug>` (e.g. `/industries/recreation-leisure`) |
| Country / region | `/countries/<slug>`, `/regions/<slug>` |
| Brand / agency | `/brands/<slug>`, `/agencies/<slug>` |
| Professional / student feeds | `/professional`, `/student` |
| Ad images | `https://image.adsoftheworld.com/<id>` (view in the browser only) |

A search returns up to about 40 results on page 1. Results mix professional and student work.

## Filter IDs (from the advanced search form, 2026-09-24)

**Medium** (`medium_type_ids[]`, up to 3): 12 360° · 5 Ambient · 6 Audio · 7 Content · 10 Design · 11 Digital · 8 Experiential · 1 Film · 9 Integrated · 4 OOH Outdoor · 2 Print · 3 Static Images

**Industry** (`industry_ids[]`, up to 3): 1 Agency Self-Promo · 2 Alcoholic Drinks · 3 Automotive and Personal Transportation · 4 Beauty · 5 Candy, Snacks · 47 Cannabis · 46 Delivery and Rideshare Services · 20 Drinks (Non Alcoholic) · 6 Education · 44 Electronic Devices · 7 Electronics, Technology · 8 Fashion · 9 Finance · 42 Fitness · 10 Food · 11 Gambling · 36 Gaming · 12 Health · 13 Hospitality, Tourism · 14 House, Garden · 39 Household Products · 15 Industrial · 41 Insurance · 43 Jewelry · 48 Lottery · 16 Media · 17 Military · 18 Movies · 19 Music · 21 Office Equipment · 35 Other · 22 Personal Accessories · 23 Pets · 24 Pharmaceutical · 25 Professional Services · 26 Public Interest · 40 Public Utility · 38 Real Estate · 27 Recreation, Leisure · 28 Religion · 29 Retail Services · 30 Sports · 45 Sportswear · 31 Tobacco · 32 Toys · 33 Transport · 37 Travel and Tourism · 34 TV and Streaming Promos

**Region** (`region_ids[]`, up to 2): 4 Africa · 1 Asia · 7 Central America · 5 Europe · 3 Far East · 8 Latin America · 2 Middle East · 6 North America · 9 Oceania

**Country** (`country_ids[]`, up to 3), common: 210 United States · 209 United Kingdom · 36 Canada · 11 Australia. Others: read the form on `/campaigns`.

**Collections** (`collection_ids[]`, up to 2), most useful for reference: 50 Classic Print Advertising · 1 Creative Typography in Advertising · 58 AOTW Editors Choice Collection · 60 The All Time Iconic TV Commercials Collection · 17 Experiential Advertising Highlights · 90 Cannes Lions Grand Prix Winners 2025 · 80 The Cannes Lions Grand Prix Winners 2024 · 63 The Cannes Lions Grand Prix Winners 2023 · 103 2026 Cannes Lions Winners · 102 Clio Award Winners 2026 · 88 Clio Award Winners 2025 · 78 Clio Award Winners 2024 · 56 Clio Award Winners 2023 · 51 Clio Award Winners 2022 · 79 AOTW Insurance Collection · 67 AOTW Transportation Collection. The full list is on the `/campaigns` search form.

## Known quirks

- Combining a collection filter with medium and industry filters returned unfiltered results in one test (2026-09-24). If results look unrelated, drop the collection filter.
- An empty keyword plus a filter works (`search=&medium_type_ids[]=2&industry_ids[]=6`). A keyword plus an industry filter returned nothing in one test; try the keyword alone, then filter by reading the results.
- The Education industry mostly returns student work from schools; for professional education advertising, search by keyword (university, college, business school, enrollment) and check the PRO/STUDENT label on each campaign.
- Short or acronym keywords match loosely: `MBA` returned unrelated fashion and luxury campaigns (2026-09-24). Use full words and phrases ("business school", "graduate program").
- Campaign pages carry an auto-written description ("This professional campaign titled ... was published in ..."), which is where the professional/student label, date, country, medium and industry come from.
- In the browser, the large ad images are the `img` elements whose source starts with `https://image.adsoftheworld.com/` and whose natural width is over about 600 px. Opening the image URL directly gives the cleanest view.
