# Ad reference index

CreativeEngine's own library of proven advertising: ads someone in the department has actually looked at, tagged by how the idea works, with our read of why. Maintained by the `ad-reference` skill (`.claude/skills/ad-reference/`). Started 2026-09-24.

| File | Holds |
|---|---|
| `index.md` | One row per ad: the searchable table |
| `entries/<slug>.md` | One file per ad: facts, link, tags and our analysis |

## Rules

- **Links and our words only.** No images, no copied descriptions, no body copy. The ad's own headline may be quoted exactly if it is 15 words or fewer. Source terms: `.claude/skills/ad-reference/references/adsoftheworld.md`.
- **Viewed, or say so.** An entry is `VIEWED` only if someone looked at the ad itself. Otherwise it is `METADATA ONLY`, and its mechanism tag is provisional.
- **No client facts.** Nothing about any client, brief or concept goes here: no client names, no "relevant to X", no verdicts on client work. Done-before reports and reference picks for a job live in that client's project folder.
- **Not evidence.** An ad's awards, results or claims prove nothing about any client. "It ran" is not "it worked".
- **Curated, not mirrored.** File ads worth learning from. A weak ad is filed only when it is a useful precedent for a Done-before check, and its read says so.

## Entry format

```
# <Brand> · "<Title>"

SOURCE:     Ads of the World · https://www.adsoftheworld.com/campaigns/<slug>
BRAND:      <brand>
AGENCY:     <agency or school>        TYPE: PRO / STUDENT
YEAR:       <month year published>    COUNTRY: <country>
MEDIUM:     <site medium types>       INDUSTRY: <site industries>
STATUS:     VIEWED <date> / METADATA ONLY <date>
LINE:       "<the ad's own headline, ≤15 words>" (or none)

## What it does
One or two sentences, in our words: the idea, not the execution.

## How it works
MECHANISM:  <from the vocabulary below>
IDEA TYPE:  <from the vocabulary below>
DEVICE:     <copy devices, if any>
CARRIER:    headline / image / both / typography
LENS:       <writers' room lens it most resembles>

## Our read
Why it works or doesn't, what is worth borrowing, what would make a borrowing read as a copy.
```

## Tag vocabulary

Use these words so the index stays searchable. Add a new tag only when none fits, and add it here.

| Field | Values | Source |
|---|---|---|
| MECHANISM | omission · reversal · fusion · analogy · exaggeration · context-shift · literal-language · none-clear | `shared/frameworks/pricken-idea-mechanisms.md` §2 |
| IDEA TYPE | truth-observation · reclaimed-word · deprivation · demonstration · enemy · confession · act · utility · manifesto · product-truth · category-cliché | CreativeEngine; writers' room |
| DEVICE | reversal · antithesis · parallelism · rule-of-three · misdirection · understatement · overstatement · omission · callback · double-meaning · juxtaposition · zeugma · paraprosdokian · imperative · question | `shared/frameworks/hey-whipple-copycraft.md` §5 |
| CARRIER | headline · image · both · typography | `shared/frameworks/barry-concept-art-direction.md` |
| LENS | sullivan · droga · wk · goodby | `WordSmither/knowledge/writers-room.md` |

## Searching

Search `index.md` by any column (grep works: `grep -i "reversal" index.md`). Open the entry files only for the rows that fit.
