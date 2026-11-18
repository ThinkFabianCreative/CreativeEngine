"""Render index.html from the Family Stories collection data, as Webflow's CMS would.

Merged direction (2026-11-02): card look from Figma MFK-Andres (Story Bento, node 193:1305)
and the Netlify v4 build; behaviour from this prototype (Finsweet filters + pagination,
layout script).

Run: python3 -I build.py
Reads ../../research/webflow-family-stories.json. Writes index.html next to this file.
"""
import html
import json
import pathlib
import random
import time

HERE = pathlib.Path(__file__).parent
DATA = HERE / "../../research/webflow-family-stories.json"

PROGRAMS = ["Lifeline", "Safe Haven", "Balance", "Boost", "Pillars"]
FORMATS = ["Video", "Read", "Where Are They Now?"]

# Flat color blocks from Figma / v4: path (viewBox 0 0 100 100, stretched) and placement.
DECO = {
    "roof": ("M0 45 L50 10 L100 45 V100 H0Z", "right:0;bottom:0;width:62%;height:55%"),
    "arch": ("M0 100 V40 A50 40 0 0 1 100 40 V100Z", "left:0;bottom:0;width:58%;height:60%"),
    "curve": ("M100 0 V100 H10 C10 40 50 0 100 0Z", "right:0;top:0;width:60%;height:100%"),
}
PLAY = ('<span class="play" aria-hidden="true"><svg viewBox="0 0 22 26">'
        '<path d="M0 0 L22 13 L0 26 Z" fill="currentColor"/></svg></span>')

# TEST DATA. Filter testing only: random programs (and Where Are They Now?) from a fixed seed,
# so every chip has results and the run is repeatable. Video comes from real video links only.
RNG = random.Random(2026)
TEST_TAGS = True

# Quotes are their own item type in the same collection (type: "quote" in the JSON).
# In Webflow a Sort Order field places them; here one quote follows every N stories.
QUOTE_EVERY = 5


def e(s):
    return html.escape(s or "", quote=True)


def tags(story):
    found = story["program_tags"] or story.get("program_tags_guess") or []
    return [t.replace("PLACEHOLDER: ", "") for t in found]


def story_tags(s):
    if TEST_TAGS:
        programs = sorted(RNG.sample(PROGRAMS, RNG.choice([1, 1, 2, 2, 3])), key=PROGRAMS.index)
        formats = ["Read"]
        if RNG.random() < 0.2:
            formats.append("Where Are They Now?")
    else:
        programs = tags(s)
        formats = list(s.get("format_guess") or ["Read"])
    if s["slug"] == "jeremiahs-journey" and "Where Are They Now?" not in formats:
        formats.append("Where Are They Now?")
    if s.get("has_video"):
        formats.append("Video")
    return programs, formats


def field(name, values):
    """One hidden plain-text field per tag type, e.g. "Lifeline, Boost". Chips match with
    fs-list-operator="contain", so no nested Collection Lists are needed."""
    return f'<div class="fs-field" fs-list-field="{name}">{e(", ".join(values))}</div>'


def item(inner, size="single"):
    return f'''
      <div class="bento-item w-dyn-item" role="listitem" fs-list-element="item" fs-list-stagger="35" data-size="{size}">{inner}
      </div>'''


def deco(kind, color):
    d, pos = DECO[kind]
    return (f'<svg class="deco" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true" '
            f'style="{pos};color:{color}"><path fill="currentColor" d="{d}"/></svg>')


def card_type(s, video_n):
    """Stand-in for the CMS "Card type" option field."""
    if s["slug"] == "jeremiahs-journey":
        return "feature"
    if s.get("has_video"):
        return "video-warm" if video_n % 2 == 0 else "video-cool"
    return "photo"


def story_card(s, kind):
    programs, formats = story_tags(s)
    fields = field("program", programs) + field("format", formats)
    href = e(s.get("video_url") or s["url"])
    name = s.get("video_headline") or s["title"]
    desc = f'<p class="card-description">{e(s["preview"])}</p>' if s["preview"] else ""

    if kind == "feature":
        body = (f'{deco("curve", "var(--mfk-peach)")}{PLAY}'
                f'<span class="pill">Where Are They Now?</span>'
                f'<h3 class="card-title card-title--xl">{e(name)}</h3>{desc}')
        return item(f'<a class="bento-card" href="{href}" data-variant="feature">{body}{fields}</a>', "double")

    if kind.startswith("video"):
        block = deco("roof", "var(--mfk-sun)") if kind == "video-warm" else deco("arch", "var(--mfk-orange)")
        dur = f'<span class="pill pill--time">{e(s["video_duration"])}</span>' if s.get("video_duration") else ""
        body = f'{block}{PLAY}<span class="pill">Video Story</span><h3 class="card-title">{e(name)}</h3>{dur}'
        return item(f'<a class="bento-card" href="{href}" data-variant="{kind}">{body}{fields}</a>')

    badge = programs[0] if programs else "Story"
    body = (f'<img class="poster" src="{e(s["main_image_url"])}" alt="" loading="lazy">'
            f'<span class="pill category-badge">{e(badge)}</span>'
            f'<h3 class="card-title">{e(name)}</h3>{desc}')
    return item(f'<a class="bento-card" href="{href}" data-variant="photo">{body}{fields}</a>')


def quote_card(q):
    programs = RNG.sample(PROGRAMS, RNG.choice([1, 2])) if TEST_TAGS else list(q["program_tags_guess"])
    programs.sort(key=PROGRAMS.index)
    return item(f'''
        <figure class="bento-card" data-variant="quote-{q["quote_tone"]}">
          <blockquote class="quote-text">“{e(q["quote_text"])}”</blockquote>
          <figcaption class="quote-by">{e(q["quote_attribution"])}</figcaption>
          {field("program", programs)}{field("type", ["Quote"])}
        </figure>''')


def chip(name, value, hidden=False):
    attr = " hidden" if hidden else ""
    return f'''<label class="filter-chip w-checkbox"{attr}>
          <input type="checkbox" class="filter-input" name="{name}" fs-list-field="{name}" fs-list-operator="contain" fs-list-value="{e(value)}">
          <span class="filter-label">{e(value)}</span>
        </label>'''


def main():
    items = json.loads(DATA.read_text())
    stories = [x for x in items if x["type"] == "story"]
    quotes = [x for x in items if x["type"] == "quote"]
    any_video = any(s.get("has_video") for s in stories)
    format_chips = "".join(chip("format", f, hidden=(f == "Video" and not any_video)) for f in FORMATS)
    program_chips = "".join(chip("program", p) for p in PROGRAMS)

    parts, videos = [], 0
    for i, s in enumerate(stories):
        kind = card_type(s, videos)
        videos += kind.startswith("video")
        parts.append(story_card(s, kind))
        n = i // QUOTE_EVERY
        if (i + 1) % QUOTE_EVERY == 0 and n < len(quotes):
            parts.append(quote_card(quotes[n]))

    page = (HERE / "template.html").read_text()
    page = page.replace("{{FORMAT_CHIPS}}", format_chips).replace("{{PROGRAM_CHIPS}}", program_chips)
    page = page.replace("{{CARDS}}", "".join(parts)).replace("{{TOTAL}}", str(len(stories) + len(quotes)))
    page = page.replace("{{BUILD}}", str(int(time.time())))  # cache-bust local CSS/JS
    (HERE / "index.html").write_text(page)
    print(f"index.html: {len(stories)} stories, {len(quotes)} quotes")


if __name__ == "__main__":
    main()
