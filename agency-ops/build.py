from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

INK = RGBColor(0x14, 0x14, 0x14)
GREY = RGBColor(0x6B, 0x6B, 0x6B)
LINE = RGBColor(0xDD, 0xDD, 0xDD)
ACC = RGBColor(0xFF, 0x4D, 0x00)
PAPER = RGBColor(0xFA, 0xF8, 0xF5)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
HEAD = "Libre Caslon Text"  # Traffik display
BODY = "Acumin Pro"  # Traffik text
FONT = BODY

p = Presentation()
p.slide_width, p.slide_height = Inches(13.333), Inches(7.5)
BLANK = p.slide_layouts[6]
n = [0]


def bg(s, c):
    f = s.background.fill
    f.solid()
    f.fore_color.rgb = c


def text(s, x, y, w, h, t, size=18, bold=False, color=INK, lh=1.15):
    tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    for i, line in enumerate(t.split("\n")):
        para = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        para.line_spacing = lh
        r = para.add_run()
        r.text = line
        head = size >= 20
        r.font.name, r.font.size, r.font.bold = (HEAD if head else BODY), Pt(size), (bold and not head)
        r.font.color.rgb = color
    return tb


def rect(s, x, y, w, h, c):
    r = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    r.fill.solid()
    r.fill.fore_color.rgb = c
    r.line.fill.background()
    return r


def slide(kicker, title, dark=False):
    n[0] += 1
    s = p.slides.add_slide(BLANK)
    bg(s, INK if dark else PAPER)
    fg = WHITE if dark else INK
    text(s, 0.7, 0.5, 8, 0.4, kicker.upper(), 11, True, ACC)
    text(s, 0.7, 0.85, 11.9, 1.2, title, 34, True, fg, 1.0)
    text(s, 12.2, 7.0, 0.8, 0.3, f"{n[0]:02d}", 10, False, GREY)
    text(s, 0.7, 7.0, 6, 0.3, "THE STANDARD · Creative + Accounts Playbook · v0.1 draft", 10, False, GREY)
    return s


def table(s, x, y, w, rows, colw, size=13, rowh=0.45):
    t = s.shapes.add_table(len(rows), len(rows[0]), Inches(x), Inches(y), Inches(w), Inches(rowh * len(rows))).table
    for i, cw in enumerate(colw):
        t.columns[i].width = Inches(cw)
    for r, row in enumerate(rows):
        for c, val in enumerate(row):
            cell = t.cell(r, c)
            cell.fill.solid()
            cell.fill.fore_color.rgb = INK if r == 0 else (WHITE if r % 2 else PAPER)
            tf = cell.text_frame
            tf.word_wrap = True
            tf.paragraphs[0].text = ""
            run = tf.paragraphs[0].add_run()
            run.text = val
            run.font.name, run.font.size = FONT, Pt(size if r else size - 1)
            run.font.bold = r == 0 or c == 0
            run.font.color.rgb = WHITE if r == 0 else INK
    return t


def cols(s, items, y=2.4, h=4.2, size=15):
    k = len(items)
    w = (11.9 - 0.3 * (k - 1)) / k
    for i, (head, body) in enumerate(items):
        x = 0.7 + i * (w + 0.3)
        rect(s, x, y, w, 0.06, ACC)
        text(s, x, y + 0.2, w, 0.8, head, 20, True)
        text(s, x, y + 1.0, w, h - 1.0, body, size, False, INK, 1.25)


def notes(s, t):
    s.notes_slide.notes_text_frame.text = t


# 1 Cover
n[0] += 1
s = p.slides.add_slide(BLANK)
bg(s, INK)
rect(s, 0.7, 2.2, 1.2, 0.08, ACC)
text(s, 0.7, 2.5, 12, 1.6, "The Standard", 80, True, WHITE, 1.0)
text(s, 0.7, 3.9, 11, 1, "How the creative department and accounts work together.\nOperations and process playbook.", 24, False, WHITE)
text(s, 0.7, 6.2, 11, 0.6, "Andres Fabian, Creative Director · v0.1 working draft · October 2026", 14, False, GREY)

# 2 What we heard
s = slide("Why", "We don't have a talent problem.\nWe have a system problem.")
cols(s, [
    ("Inconsistent work", "Every project is presented differently. Fidelity at each stage is unclear across ACDs, ADs and designers."),
    ("Invisible thinking", "Clients can't see where a concept came from. Rationale and insight aren't on the page."),
    ("No house standard", "There's no agency template for how work reaches a client."),
    ("Unlimited changes", "Requests go straight to designers. No round limits, scope creep, lost time and money."),
], size=14)

# 3 Root causes
s = slide("Diagnosis", "Three root causes behind the symptoms")
cols(s, [
    ("1 · No real brief", "Work often starts without a brief, or with a 16-page AI essay that makes no choices. Without agreed criteria, nobody can judge the work. That's how a client stays silently unhappy."),
    ("2 · Nobody owns insight", "Media plans from budget, Accounts from the ask. Creative gets the leftovers. \"First round AI\" fills the gap with generic output."),
    ("3 · Studio not at the table", "Timelines and RFPs are promised without production input or budget. The studio absorbs it, and no time is left for discovery or ideation."),
])

# 4 Culture
s = slide("Where we're going", "From → To", dark=True)
text(s, 0.7, 2.4, 5.5, 0.5, "TODAY", 12, True, GREY)
text(s, 0.7, 2.9, 5.5, 3, "Disconnected departments\nUnder-resourced, disheartened teams\nAccount-led budget culture", 26, False, WHITE, 1.4)
text(s, 7.0, 2.4, 5.5, 0.5, "IN 6 MONTHS", 12, True, ACC)
text(s, 7.0, 2.9, 5.6, 3, "High-achieving\nAward-winning\nAmbitious, entrepreneurial", 26, True, WHITE, 1.4)

# 5 Pillars
s = slide("The playbook", "Four pillars")
cols(s, [
    ("1 · No signed brief, no work", "One-page brief. Signed by the CD and the client before anything starts.\n\nOwner: Andres + Cayley"),
    ("2 · Gates and fidelity", "Four gates, a clear fidelity at each one, one presentation standard.\n\nOwner: Andres"),
    ("3 · Scope and client protocol", "Round limits, triage, QC gate, dates from the plan, daily stand-up.\n\nOwner: Andres + Darcey"),
    ("4 · The designer reset", "Discovery on every job, crafted output, weekly crit, excellence as the standard.\n\nOwner: Andres"),
], size=14)

# 6 Pillar 1 rules
s = slide("Pillar 1", "No signed brief, no work")
text(s, 0.7, 2.3, 6.2, 4.4,
     "1.  Every Full-track project starts with a one-page brief. Light-track jobs start from the ticket and change log.\n"
     "2.  One named account lead writes it. Media supplies audience and placement. Insight comes from the truth hunt.\n"
     "3.  Andres approves or bounces it within 1 business day.\n"
     "4.  A bounce always names the missing choice (\"two audiences\", \"no single proposition\").\n"
     "5.  The client signs the brief before any creative work starts.\n"
     "6.  Every presentation and every piece of feedback is judged against the signed brief.",
     16, False, INK, 1.35)
rect(s, 7.4, 2.3, 5.2, 4.2, INK)
text(s, 7.7, 2.6, 4.7, 0.5, "THE TEST FOR ANY CLIENT REQUEST", 12, True, ACC)
text(s, 7.7, 3.1, 4.7, 3.2, "Does this change the brief?\n\nYes → new brief, possibly new scope.\nNo → feedback, inside the rounds.", 22, True, WHITE, 1.3)

# 7 One-page brief
s = slide("Pillar 1", "Research pack vs. the brief")
table(s, 0.7, 2.3, 6.4, [
    ["", "Research pack", "The brief"],
    ["Length", "As long as needed", "One page, hard limit"],
    ["AI", "Encouraged: RFPs, audiences, competitors, data", "Can draft. A human makes every choice"],
    ["Purpose", "Background", "The decisions"],
    ["Signed", "No", "Andres + client"],
], [1.2, 2.6, 2.6], 13, 0.7)
text(s, 7.6, 2.3, 5, 0.5, "THE ONE-PAGE BRIEF", 12, True, ACC)
text(s, 7.6, 2.75, 5, 4,
     "The problem\nThe one person (from real data)\nThe truth: one sentence + its source\nThe single-minded proposition\nReasons to believe (credible, verifiable)\nMandatories (incl. MLR/legal)\nDeliverables + budget\nTimeline\nHow we'll judge success",
     17, False, INK, 1.4)
notes(s, "A 16-page brief is no brief. AI makes length free, so it avoids the hard choices. Research can be long; the brief can't.")

# 7b Truth hunt
s = slide("Pillar 1", "Briefs built on truth, not on information")
cols(s, [
    ("The truth hunt", "Before the brief: 60–90 minutes with the account lead, Cayley, Connor and the ACD. Ends with 2–3 candidate truths, each with a source."),
    ("Label the evidence", "Verified: client data, research, performance.\nObserved: discovery, conversations, using the product.\nHypothesis: a guess, marked and tested."),
    ("Where truths come from", "Connor's performance data. Cayley's audience data. The client's research and front-line people. Customers in their own words."),
], size=14)
text(s, 0.7, 6.2, 11.9, 0.6, "Great work starts from a truth (Pete Barry). AI can gather; a truth needs a source a person can point to.", 14, True, ACC)

# 7c Two tracks
s = slide("Pillar 1", "Two tracks: the process fits the job")
table(s, 0.7, 2.2, 11.9, [
    ["", "Light track", "Full track"],
    ["What", "Updates to approved work: edits, resizes, variants, template changes", "New ideas, new builds, campaigns, rebrands, anything regulated"],
    ["Starts with", "Ticket + change log", "Signed one-page brief + truth hunt"],
    ["Gates", "None: build → QC → send", "G0 → G1 → G2 → G3"],
    ["Discovery", "Read the brief and the change log", "15% discovery + 20% ideation, protected in the plan"],
    ["Reviewer", "Senior designer who didn't make it (web: Jordan)", "Andres (or the ACD who didn't make it)"],
    ["Reaches the client", "Sent with change log, after QC", "Presented by ACD or CD"],
], [2.2, 4.8, 4.9], 13, 0.6)

# 8 Gates
s = slide("Pillar 2", "Four gates. Clear fidelity at each.")
table(s, 0.7, 2.2, 11.9, [
    ["Gate", "Purpose", "What we show", "Owner", "Not allowed yet"],
    ["G0 Brief", "Agree the problem", "Signed one-page brief", "Accounts + Andres", "Any design"],
    ["G1 Territories", "Agree the direction", "Discovery share-out + 2–3 territories: concept sentence, rough key visual, headline, why", "ACD · web: Andres", "Polish, mockups, systems"],
    ["G2 Concept", "Agree the idea", "1 recommendation (+1 max) in 3 real executions", "AD · ACD/CD signs off", "Final assets"],
    ["G3 Final", "Approve for production", "Full system, real copy, real formats", "AD/GD, ACD + CD sign off", "New ideas"],
], [1.7, 2.0, 4.4, 2.0, 1.8], 13, 0.8)
text(s, 0.7, 6.3, 11.9, 0.5, "Full track: discovery 15% + ideation 20% of every timeline. Accounts can't compress them away.", 14, True, ACC)

# 9 Gates by type
s = slide("Pillar 2", "Same gates, every type of project")
cols(s, [
    ("Rebrand", "G1 brand territories\nG2 identity on 5 real touchpoints\nG3 guidelines + toolkit"),
    ("Campaign / Meta", "G1 platform territories\nG2 platform proven across 3 executions\nG3 rollout + Variant Matrix"),
    ("Web / product", "G1 experience principles + stylescapes\nG2 key screens hi-fi + 1 prototype flow\nG3 full UI + handoff\nG4 Build: dev → QA → launch → 30-day check-in"),
], size=16)
notes(s, "Web gets its own build gate because Jordan, Damba, Aaron and Matt run a full design-to-dev pipeline.")

# 10 Concept card
s = slide("Pillar 2", "Every concept carries a Concept Card")
items = [("Insight", "The human truth, in one sentence"),
         ("Idea", "The concept sentence. No sentence, no idea yet"),
         ("Why it's right", "Its link to the brief's single proposition"),
         ("How it shows up", "1–3 executions"),
         ("Judge it on", "The 2–3 criteria the client should react to")]
for i, (h, b) in enumerate(items):
    y = 2.3 + i * 0.85
    text(s, 0.7, y, 0.6, 0.6, f"{i+1}", 28, True, ACC)
    text(s, 1.4, y + 0.05, 3.2, 0.6, h, 20, True)
    text(s, 4.6, y + 0.1, 8, 0.6, b, 17, False, GREY)
text(s, 0.7, 6.5, 11.9, 0.4, "No card, no presentation. It turns \"I don't like the blue\" into \"does this dramatize the insight?\"", 14, True)

# 11 Presentation spine
s = slide("Pillar 2", "One agency presentation spine")
spine = ["Cover", "What you asked", "What we learned", "The strategy in one line", "The work (Concept Cards)",
         "Executions", "Our recommendation + why", "Decisions we need today", "Next gate + rounds left"]
for i, t in enumerate(spine):
    c, r = i % 3, i // 3
    x, y = 0.7 + c * 4.05, 2.3 + r * 1.4
    rect(s, x, y, 3.8, 1.2, ACC if i == 7 else WHITE)
    text(s, x + 0.2, y + 0.15, 3.4, 1, f"{i+1:02d}\n{t}", 16, True, WHITE if i == 7 else INK)
notes(s, "The neutral, editorial frame keeps the client's work as the hero. Slide 8 matters most: it tells the client what they're there to decide.")

# 11b Presented, never just sent
s = slide("Pillar 2", "Creative is presented, never just sent")
table(s, 0.7, 2.2, 7.2, [
    ["Stage", "How it reaches the client", "Who"],
    ["G1 Territories", "Live presentation", "ACD or CD"],
    ["G2 Concept", "Live presentation", "ACD or CD"],
    ["G3 Final", "Live or recorded walkthrough", "ACD · web: Andres"],
    ["Correction rounds", "Sent with the change log, every item marked", "Accounts, after QC gate"],
], [2.0, 3.3, 1.9], 13, 0.7)
rect(s, 8.3, 2.2, 4.3, 4.3, INK)
text(s, 8.6, 2.5, 3.8, 0.5, "WHY", 12, True, ACC)
text(s, 8.6, 3.0, 3.8, 3.4, "Work sent cold gets judged on taste: \"she looks too old.\"\n\nWork presented gets judged on the brief: the insight, the idea, the decisions we need.", 17, True, WHITE, 1.3)
text(s, 0.7, 6.0, 7.2, 0.8, "Older or busy clients: a 3–5 minute recorded walkthrough by the ACD counts as presented.", 13, False, GREY)

# 11c Review by job size (web)
s = slide("Pillar 2", "Who reviews: split by job size")
table(s, 0.7, 2.2, 11.9, [
    ["Track", "What it covers", "Reviewer", "Presents to client"],
    ["Light", "Updates to approved work: page edits, template changes, resizes, variants, bug-level fixes", "Jordan (web) · senior designer on the job", "Sent with change log, after QC"],
    ["Full", "New builds, new concepts, anything at G1 or G2, regulated claims", "Andres", "ACD or CD, live or recorded"],
], [1.4, 5.2, 3.0, 2.3], 14, 0.9)
text(s, 0.7, 5.3, 11.9, 1.2,
     "Maker is never checker: Jordan never reviews his own work; Damba's work on Light jobs goes to Jordan.\n"
     "For the first 6 weeks Andres spot-checks Jordan's reviews. Then Jordan's review scope grows job by job.",
     14, False, INK, 1.4)
notes(s, "Protects Andres's time now and gives Jordan a path into the ACD role he holds by title.")

# 12 Pillar 3 rounds + triage
s = slide("Pillar 3", "Rounds and triage")
table(s, 0.7, 2.3, 5.2, [
    ["Gate", "Rounds included"],
    ["G1 Territories", "1"],
    ["G2 Concept", "2"],
    ["G3 Final", "2 + polish"],
    ["Beyond", "Change order"],
], [3, 2.2], 15, 0.65)
text(s, 6.5, 2.3, 6, 0.5, "NOTHING REACHES A DESIGNER UNTIL IT'S TRIAGED", 12, True, ACC)
text(s, 6.5, 2.8, 6.1, 3.5,
     "FIX: inside scope and the round → go\n"
     "CHANGE: inside scope, costs a round → client confirms\n"
     "NEW: outside the brief → change order or park it\n\n"
     "One consolidated set of client notes per round, in writing.\n"
     "A change to the idea goes to the ACD or CD before anyone touches a file.\n"
     "Rounds are written into every SOW.",
     15, False, INK, 1.4)

# 12b QC gate
def yn(s, x, y, w, head, qs):
    rect(s, x, y, w, 0.06, ACC)
    text(s, x, y + 0.12, w, 0.4, head, 15, True)
    for i, q in enumerate(qs):
        yy = y + 0.6 + i * 0.42
        text(s, x, yy, w - 1.0, 0.4, q, 11.5, False, INK, 1.0)
        text(s, x + w - 0.95, yy, 0.95, 0.4, "Y  /  N", 11, True, GREY)

s = slide("Pillar 3", "QC gate: every answer YES, or it doesn't go out")
yn(s, 0.7, 2.0, 3.8, "1 · Meeting the brief?", [
    "Answers the signed brief's proposition",
    "Speaks to the one person in the brief",
    "Built on the agreed insight / territory",
    "Fidelity right for this gate",
    "Concept Card present and accurate",
])
yn(s, 4.75, 2.0, 3.8, "2 · On brand guidelines?", [
    "Logo use, clear space, lockups correct",
    "Brand colours and typefaces only",
    "Imagery matches brand style",
    "Tone of voice matches the brand",
    "Image and font licences confirmed",
])
yn(s, 8.8, 2.0, 3.8, "3 · Delivering what was asked?", [
    "Every item on the change log done",
    "Nothing changed that wasn't asked",
    "All deliverables, sizes and formats present",
    "Specs met (dimensions, bleed, file type)",
    "Ambiguous notes clarified, not guessed",
])
yn(s, 0.7, 4.6, 5.8, "4 · Any mistakes?", [
    "Spelling, grammar, punctuation clean",
    "Numbers, prices, dates, claims verified with client in writing",
    "Legal, disclaimer and compliance/MLR lines present",
    "Names, URLs, phone numbers, CTAs correct and working",
])
yn(s, 6.8, 4.6, 5.8, "5 · Presentation ready?", [
    "Uses the agency presentation spine",
    "No typos, placeholders or leftover comments",
    "Decisions we need are stated",
    "Round count and next gate shown",
])
notes(s, "Sections 1 and 4 (claims) are signed by Accounts. Sections 3 and 4 (details) by the QC team, Judy and Katie, who get the brief, guidelines and change log. Section 2 by an AD who didn't make the work; 5 by the ACD. Any NO: fix it, or the ACD signs off on an explanation.")

s = slide("Pillar 3", "Who signs the QC gate")
table(s, 0.7, 2.2, 11.9, [
    ["Section", "Signed by", "Why"],
    ["Change log → ticket tasks + Done", "PM + Accounts", "Each feedback item becomes a task; Done = QC gate passed"],
    ["1 · Meeting the brief", "Accounts + ACD", "Accounts own the brief and client direction; ACD owns the idea"],
    ["2 · On brand", "An AD who didn't make it", "Craft and brand standards"],
    ["3 · Delivering what was asked", "QC team (Judy, Katie)", "Ticks the change log, with the brief and guidelines in hand"],
    ["4 · Mistakes: claims and numbers", "Accounts", "Confirmed with the client in writing"],
    ["4 · Mistakes: language and details", "QC team (Judy, Katie)", "Proofing, links, CTAs"],
    ["5 · Presentation ready", "ACD", "Last look before it leaves the building"],
], [3.6, 2.8, 5.5], 13, 0.58)
text(s, 0.7, 6.3, 11.9, 0.5, "Maker is never checker: whoever built the work can't sign its QC. Every round ships with a change log, each item marked done, clarified or out of scope.", 14, True, ACC)

# 14b Working hours
s = slide("Pillar 3", "Working hours and turnaround")
text(s, 0.7, 2.3, 6.4, 4.3,
     "1.  Turnaround is measured in business days. A Friday-evening client reply is a Monday-morning task.\n"
     "2.  Timelines are built without weekends. If a date only works with weekend work, the timeline is fixed at kickoff.\n"
     "3.  No client sends after 3 PM Friday, unless the client agrees review happens next business week.\n"
     "4.  Weekend work only by exception: a genuine emergency, approved in advance by the CD, with time given back.\n"
     "5.  \"ASAP\" becomes a dated deadline set by Accounts and PM, not an open-ended expectation.",
     15, False, INK, 1.35)
rect(s, 7.5, 2.3, 5.1, 4.2, INK)
text(s, 7.8, 2.6, 4.6, 0.5, "WHY IT MATTERS", 12, True, ACC)
text(s, 7.8, 3.1, 4.6, 3.3, "Edits rushed on a weekend skip QC. On print and regulated work, that's where expensive mistakes happen.\n\nProtected weekends are how the team knows the reset is real.", 18, True, WHITE, 1.3)

# 15c Daily stand-up
s = slide("Pillar 3", "Daily stand-up: 15 minutes, PM-led")
table(s, 0.7, 2.1, 7.0, [
    ["Order", "PM calls out", "Time"],
    ["1 · Blocked", "Reason, owner, since when. Cleared today?", "2 min"],
    ["2 · With client / Feedback", "Round x of y. Feedback due when?", "2 min"],
    ["3 · Review / QC", "Who is it waiting on? Clear by noon?", "2 min"],
    ["4 · In progress", "Person by person, three questions", "7 min"],
    ["5 · Ready / Intake", "Anything without a brief doesn't start", "1 min"],
    ["6 · Close", "Read back commitments and blocker owners", "1 min"],
], [2.4, 3.6, 1.0], 12, 0.55)
rect(s, 8.1, 2.1, 4.5, 4.4, INK)
text(s, 8.4, 2.35, 4.0, 0.4, "THREE QUESTIONS PER DESIGNER", 12, True, ACC)
text(s, 8.4, 2.85, 4.0, 2.2, "1. What moves today?\n2. Will it make the promised date?\n3. What's blocking you, and who owns it?", 17, True, WHITE, 1.45)
text(s, 8.4, 4.9, 4.0, 1.5, "Cards updated and hours confirmed by 9:40. No problem-solving in the room: park it. The PM updates the board live.", 12, False, WHITE, 1.35)
text(s, 0.7, 6.25, 7.0, 0.5, "Walk the board right to left: finishing beats starting.", 13, True, ACC)

# 13 Dates from the plan
s = slide("Pillar 3", "Dates come from the plan, not from a guess")
cols(s, [
    ("Standard times", "The Task Hub already holds 593 standard times. The PM builds the plan from them, and the plan sets the date."),
    ("Earlier than plan", "The account lead negotiates with the client: what gets cut, moved or resourced. Designers aren't asked to absorb it."),
    ("Off the menu", "Large or unusual work (360º, full websites): the ACD estimates within 48 hours."),
    ("Every RFP", "Includes a production line. Rates owned by Darcey + Brent. Standard times reviewed every quarter against logged hours."),
], size=14)
text(s, 0.7, 6.2, 11.9, 0.6, "Stop asking \"when will this be done?\" The answer is in the plan.", 14, True, ACC)

# 13b Time logging + board
s = slide("Pillar 3", "Our tool: the Task Hub board")
cols(s, [
    ("One board", "Every job on one board by stage: Intake, Ready, In progress, Internal review, Quality Control, With client, Feedback, Done. Blocked work has a reason, an owner and a date."),
    ("One owner per role", "One account lead, one creative lead, one reviewer who isn't the maker, one QC owner. No \"Darcey/Brad/Ky\"."),
    ("Hours, daily", "Everyone logs hours daily, Accounts and PM included. Under 5 minutes, half-hour steps. Unlogged hours don't exist when staffing is decided."),
], size=14)

# 14 Meta menu
s = slide("Pillar 3", "Meta ads baseline menu (to calibrate)")
table(s, 0.7, 2.2, 11.9, [
    ["Tier", "What it is", "Duration", "Rounds"],
    ["Variant", "New copy or image on an approved concept", "2–3 days", "1"],
    ["Static set", "New concept, 3–5 statics across feed, story, reel cover", "2 weeks", "Concept 1 + final 2"],
    ["Video, existing footage", ":06/:15 edit, captions, sizes", "1–2 weeks", "2"],
    ["Video, new production", "Script, shoot or 3D, edit", "4–6 weeks", "Script 1 + edit 2"],
    ["Campaign launch", "New concept, statics + video, multi-audience", "3–4 weeks", "Full gates"],
    ["Variant pack S / M / L", "3×3×3 = 27 / 5×5×3 = 75 / larger: ACD scopes", "Template-built", "QA only"],
], [2.6, 5.4, 1.8, 2.1], 13, 0.6)
text(s, 0.7, 6.5, 11.9, 0.4, "Placeholder durations. Replaced by calibration data after 6 weeks.", 12, False, GREY)

# 15 Who owns what
s = slide("Principle", "Media decides who and where.\nCreative decides what and how.\nAccounts gets approval.", dark=True)
text(s, 0.7, 4.3, 11.9, 2, "Media guidance arrives inside the one-page brief (the one person, placements, number of variants needed), not as a separate document.\nNo role loses anything. Every decision gets one owner.", 18, False, WHITE, 1.4)

# 16 Variant matrix
s = slide("Pilot · CMU Applications Open", "The Variant Matrix")
table(s, 0.7, 2.2, 11.9, [
    ["Step", "Owner", "Output"],
    ["Audience input", "Media (Cayley)", "Audiences, segment jobs, number of variants, placements"],
    ["Copy matrix", "Creative (Debbie / AD)", "Variant sheet: headlines + CTAs per audience"],
    ["Client approval", "Accounts", "Client approves the sheet (copy) and the masters (design), once each"],
    ["Masters", "AD", "One Figma master component per size (1:1, 4:5, 9:16)"],
    ["Generate · QA · export", "Andrea", "Matrix filled from the sheet, checked, exported"],
], [2.6, 2.8, 6.5], 14, 0.65)
text(s, 0.7, 6.3, 11.9, 0.5, "ADs stop being variant factories. We time the pilot against the manual way and show the numbers.", 14, True, ACC)

# 17 Cost of bad craft
s = slide("Pillar 4", "Craft is where the money is")
table(s, 0.7, 2.2, 11.9, [
    ["Cost of bad craft", "Where it shows up", "What we saw"],
    ["Rework", "Extra rounds, corrections, re-QC", "About 23% of creative tasks are rework by name"],
    ["Wasted media", "Spend behind ads nobody clicks", "Creative quality drives most of a campaign's results"],
    ["Late work", "Missed enrollment windows, late launches", "44% of tasks finish on their original date"],
    ["Errors", "Wrong claims, reprints, compliance fixes", "Grammar-only QC catches none of these"],
], [2.6, 4.2, 5.1], 13, 0.7)
text(s, 0.7, 6.1, 11.9, 0.7, "AI can make an edit. Only craft makes it right, on brand and worth paying for.", 15, True, ACC)
notes(s, "Task Hub export Apr 28 – Oct 9 2026. Rework is detected from task names, so it's an estimate. Check the exact creative-effectiveness study before quoting a figure.")

# 17b The designer reset
s = slide("Pillar 4", "The designer reset", dark=True)
text(s, 0.7, 2.4, 11.9, 3.8, "We do discovery on our own work.\nWe think before we make pixels.\nWe craft what leaves the building.\nWe show work every week and get better on purpose.", 30, True, WHITE, 1.35)
text(s, 0.7, 6.1, 11.9, 0.6, "Field guide: The Craft (discovery, ideation, campaign platform, checklists).", 14, False, GREY)

# 17c What we expect
s = slide("Pillar 4", "What we expect, and how we'll know")
table(s, 0.7, 2.1, 11.9, [
    ["Expectation", "What it looks like", "How we know"],
    ["Discovery on every Full-track job", "Category audit wall, immersion, 2–3 insight candidates. 15% of the timeline", "Every G1 opens with a discovery share-out. No share-out, no G1"],
    ["Thinking before pixels", "20+ rough ideas, concept sentences, a Concept Card. 20% of the timeline", "The ACD reviews the wall, not the favourite"],
    ["Crafted output", "Real-size checks, type hierarchy, image quality, licences, finish", "\"On brand\" signed by an AD who didn't make it"],
    ["Weekly crit", "45 minutes, every week. Work shown before every G2. Honest, specific, generous", "Attendance, and work shown before G2"],
    ["Excellence on purpose", "Shared reference library. One award-target project per quarter", "Entries made; work in the library"],
    ["Growth", "One personal craft goal per designer, reviewed quarterly", "Discussed in every 1:1"],
], [2.8, 4.9, 4.2], 12, 0.62)

# 17d AI
s = slide("Pillar 4", "AI: for thinking wider, not for skipping the thinking")
cols(s, [
    ("Use it for", "Category audits, reference gathering, many rough variations, \"has this been done?\" checks, comps for pitches (credited, never final)."),
    ("Not for", "Writing the insight. Choosing the idea. Final assets. Replacing sketching and thinking time."),
    ("In production", "No AI in production until a pilot proves it on real files, with a named QA owner and measured results."),
], size=14)

# 18 Rollout
s = slide("Rollout", "How we roll it out")
table(s, 0.7, 2.2, 11.9, [
    ["When", "What", "Who"],
    ["Week 1", "Align on Pillars 1 and 3 with Darcey. Production budget in RFPs with Brent", "Andres, Darcey, Brent"],
    ["Week 1", "Designer reset session: The Craft + Pillar 4. Each designer brings one piece they're proud of and one they're not. Weekly crit starts", "Andres + design team"],
    ["Week 2", "Present to Andres's creative group + Accounts. Daily hours and stand-up start on the board", "Whole team"],
    ["Weeks 2–4", "Variant Matrix pilot on CMU Applications Open", "Cayley, Debbie, AD, Andrea"],
    ["Week 6", "Retro. Baselines updated from actuals. Playbook v1.0", "Andres + Darcey"],
    ["After v1.0", "Share results with Anthony. Offer the shared-client rules to Jeremy", "Andres"],
], [1.6, 7.3, 3.0], 13, 0.6)

# 19 Open
s = slide("Still to decide", "Open questions for v1.0")
text(s, 0.7, 2.3, 11.9, 4.2,
     "•  How the client signs the brief: email reply \"approved\", PDF signature or the task hub\n"
     "•  Whether BriefMachine becomes the official brief tool for Accounts and Cayley\n"
     "•  Meta dynamic creative: separate assets vs. text burned in (with Cayley and Brent)\n"
     "•  Feedback channel: PDF comments → task hub, or Figma comments where clients can use them\n"
     "•  Rules for shared medical clients with Jeremy's group\n"
     "•  Which award shows we target",
     18, False, INK, 1.5)

# 32 Five rules
s = slide("The Standard on one page", "Five rules and one place")
items = [("No brief, no work", "Full-track work starts from a signed one-page brief with one named account lead."),
         ("Five YESes before anything leaves", "Brief, brand, what was asked, no mistakes, presentation ready. The maker never checks their own work."),
         ("Dates come from the plan", "Built from standard times. No weekends unless the CD approves an exception."),
         ("Present, don't send", "New work is walked through by an ACD or CD. Corrections go out with the change log."),
         ("Discovery and crit", "A discovery share-out opens every G1. Weekly 45-minute crit, work shown before G2.")]
for i, (h, b) in enumerate(items):
    y = 2.15 + i * 0.78
    text(s, 0.7, y, 0.6, 0.6, f"{i+1}", 26, True, ACC)
    text(s, 1.35, y + 0.04, 3.9, 0.6, h, 18, True)
    text(s, 5.3, y + 0.08, 7.3, 0.7, b, 14, False, GREY)
rect(s, 0.7, 6.15, 11.9, 0.62, INK)
text(s, 0.95, 6.22, 11.4, 0.5, "One place: the Task Hub board. One owner per role, a reason on every blocker, stand-up at 9:45.", 14, True, WHITE)

# 33 Phased rollout
s = slide("Rollout", "One step at a time")
table(s, 0.7, 2.2, 11.9, [
    ["When", "We start", "Comes later"],
    ["Month 1", "The five rules · the board · 9:45 stand-up · weekly crit · designer reset session", "Everything else"],
    ["Month 2", "Daily hours · dates from standard times · Light vs. Full track", "Round limits in SOWs · Meta menu"],
    ["Month 3", "Round limits in new SOWs · Variant Matrix pilot · AI pilot with QA owner", "Leadership and Completed views"],
], [1.6, 6.6, 3.7], 14, 0.85)
text(s, 0.7, 5.9, 11.9, 0.8, "Month 1 partners: Darcey (Accounts and PM rules), Jeremy (shared QC and working hours). Anthony sees results after month 3.", 13, False, INK, 1.35)

out = "/Users/andresfabian/Documents/AI_Traffik_Projects/CreativeEngine/agency-ops/The_Standard_v0.1.pptx"
p.save(out)
print(out, n[0])
