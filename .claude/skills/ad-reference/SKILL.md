---
name: ad-reference
description: Find, study and file reference ads from Ads of the World (adsoftheworld.com) and CreativeEngine's own ad-reference index. Use when a brief or rough idea needs proven precedents by mechanism, medium or category (Find); when the user points at ads or a collection worth keeping (Harvest); or when a concept needs a "has this been done?" check before it is presented (Done before). Links and our own analysis only; never copies of the ads.
---

# Ad reference

A working library of proven advertising, built from Ads of the World and our own analysis. It gives the room precedents to borrow from, and it catches an idea that has already run before a client does.

This skill is method. WordSmither and DesignChamp own the creative judgment; CreativeDirector owns selection and the originality call.

## Sources

| Source | What it is | Read first |
|---|---|---|
| `shared/knowledge/ad-reference/` | CreativeEngine's own index: ads we have looked at, tagged by mechanism, with our read of why they work | `README.md` (rules, tag vocabulary), then `index.md` |
| Ads of the World | Public archive of professional and student campaigns, part of The Clio Network | `references/adsoftheworld.md` (URLs, filter IDs, robots, terms) |

Always search the index before the site. The index grows with every run, so it gets faster and more useful over time.

## Hard rules

1. **Links and our analysis, never copies.** The Clio terms that cover Ads of the World allow personal, temporary viewing only, forbid commercial use and forbid mirroring. So the index holds bibliographic facts (title, brand, agency, year, country, medium), the link, our tags and our own words. Never download or save images, never copy the site's description text, never reproduce body copy. The one exception is the ad's own headline or line, quoted exactly and only when it is 15 words or fewer.
2. **Look at the ad before judging it.** Metadata is not the idea. Open the campaign in the browser and view the image or film before tagging a mechanism. If you could only read metadata, mark the entry `METADATA ONLY` and don't tag a mechanism with confidence.
3. **Respect robots.txt.** Never request `?page=` URLs (paginated listings are disallowed), `/tags`, `/watchlist`, `/bookmarked`, `/follows` or `/settings`. Narrow a search with keywords and filters instead of paging. No bulk crawling: a run reads what the task needs, typically under 30 campaign pages.
4. **Student work is labelled.** Ads of the World mixes professional and student campaigns, and the Education industry filter is dominated by student work. Prefer professional work as proof of what ran; student work is idea stimulus only and is tagged `STUDENT`.
5. **No client facts in the index.** The index is shared method. A client's brief, name, idea or verdict never goes into an entry. Anything about a client's concept (a Done-before report, the references chosen for a job) is written in that client's project folder.
6. **References are not evidence.** An ad's awards, results or claims are not facts about any client, and "it ran" is not proof "it worked". Never cite effectiveness you have not verified.
7. **Borrowing is allowed.** Taking a reference's structure, device or look directly is fine (Andres's taste profile). Name what is being borrowed so the Done-before check can judge the distance.

## Tools

- **Search and metadata:** WebFetch on `https://www.adsoftheworld.com/campaigns?search=<terms>` plus filters (see `references/adsoftheworld.md`), and on campaign pages.
- **Viewing the ad:** the built-in browser. Open the campaign page, read the large image URLs from the page (`image.adsoftheworld.com/...`), open each one and take a screenshot. Viewing is fine; saving is not. Use Claude in Chrome instead only when the user asks for it or the built-in browser can't load the page.
- No login is needed. If a page ever asks for one, stop and tell the user; never enter credentials.

## Mode 1: Find

**When:** EXPLORE or DEVELOP, when a brief, a truth or a rough idea needs precedents.

1. **State the need in one line:** the truth or problem, the medium, and the mechanism wanted if known (for example "reversal, print, a flaw reframed as a strength").
2. **Search the index** (`index.md`) by mechanism, device, medium, industry and lens.
3. **Search the site** if the index gives fewer than 3 useful references. Use 2–4 keyword searches built from the *idea* (the tension, the object, the behavior), not only the category. Add medium and industry filters to cut noise. Read only page 1 of each search.
4. **Shortlist and view.** Pick 5–8 candidates from the result titles, open each, view the ad.
5. **Return 3–5 references,** each as:

```
REFERENCE:  Brand · "Title" · Agency · Year · Country · Medium   [PRO / STUDENT]
LINK:       https://www.adsoftheworld.com/campaigns/<slug>
WHAT IT DOES: the idea in one sentence, in our words
MECHANISM:  tags from the vocabulary in README.md
BORROW:     the specific move worth taking for this brief
DON'T BORROW: what would make ours read as a copy, or what doesn't fit
```

6. **File** every ad you viewed and judged worth keeping into the index (Mode 2, steps 3–4). Don't file what you only skimmed.

## Mode 2: Harvest

**When:** the user points at ads, a brand, an agency, a collection or a search, or a Find run turns up work worth keeping.

1. Open each campaign page; get the metadata.
2. View the ad itself.
3. Write the entry file `shared/knowledge/ad-reference/entries/<slug>.md` in the format in `README.md`. The slug is the Ads of the World campaign slug.
4. Add one row to `index.md`. Keep rows sorted by date added, newest last.
5. Report what was filed, with links.

Harvest a few ads at a time, chosen for quality. The index is a curated library, not a mirror.

## Mode 3: Done before?

**When:** before a concept is presented to a client, in DEVELOP or JUDGE, or whenever someone asks "has this been done?". CreativeDirector uses it for the originality score.

1. **Break the concept into its parts:** the line or core phrase, the key word or image, the mechanism, the category and audience. Search each part separately, since precedents rarely match on all of them.
2. **Search the index, then the site:** the exact line, its key words and synonyms, the image, and the mechanism with the category filter.
3. **View every candidate** that matches on two or more parts.
4. **Grade the distance** for each close precedent:

| Distance | Meaning |
|---|---|
| **SAME** | Same line or same execution of the same idea. A real problem: rework or drop |
| **CLOSE** | Same mechanism and same key idea, different words or picture. Present only with a clear, stated difference |
| **SHARED TERRITORY** | Same word or theme, different idea or mechanism. Normal; note it |
| **DISTANT** | Surface overlap only |

5. **Write the report in the client's project folder** (`projects/<client>/<project>/work/reviews/..._done-before-check_vNN.md`), never in the shared index. Include what was searched, what was viewed, each precedent with its distance and link, and a one-line conclusion. File any ads worth keeping into the index as neutral entries, with no mention of the client.
6. **State the limit:** Ads of the World is one archive. "Not found here" is not "never done". Say which searches were run.

## What this skill does not do

- It doesn't decide whether an idea is good. That's the frameworks' and CreativeDirector's job.
- It doesn't prove effectiveness, awards or results.
- It doesn't store, download or redistribute anyone's ads.
