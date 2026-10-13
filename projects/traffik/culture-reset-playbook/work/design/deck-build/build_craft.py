import os
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "_helpers.py")).read())

# Traffik type (wearetraffik.com): Libre Caslon for display, Acumin Pro for text
HEAD = "Libre Caslon Text"
BODY = "Acumin Pro"
FONT = BODY


def text(s, x, y, w, h, t, size=18, bold=False, color=INK, lh=1.15):
    tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    head = size >= 20
    for i, line in enumerate(t.split("\n")):
        para = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        para.line_spacing = lh
        r = para.add_run()
        r.text = line
        r.font.name = HEAD if head else BODY
        r.font.size = Pt(size)
        r.font.bold = bold and not head  # Caslon carries weight on its own
        r.font.color.rgb = color
    return tb


def checklist(s, items, x=0.7, y=2.3, w=11.9, size=16, colsn=2):
    per = -(-len(items) // colsn)
    cw = (w - 0.4 * (colsn - 1)) / colsn
    for i, it in enumerate(items):
        c, r = i // per, i % per
        cx, cy = x + c * (cw + 0.4), y + r * 0.62
        box = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(cx), Inches(cy + 0.08), Inches(0.26), Inches(0.26))
        box.fill.background()
        box.line.color.rgb = INK
        box.line.width = Pt(1.5)
        text(s, cx + 0.45, cy, cw - 0.5, 0.6, it, size, False, INK, 1.1)


# 1 Cover
n[0] += 1
s = p.slides.add_slide(BLANK)
bg(s, INK)
rect(s, 0.7, 2.2, 1.2, 0.08, ACC)
text(s, 0.7, 2.5, 12, 1.6, "The Craft", 80, True, WHITE, 1.0)
text(s, 0.7, 3.9, 11, 1, "The designer reset, and how we make the work.\nFor the design team.", 24, False, WHITE)
text(s, 0.7, 6.2, 11, 0.6, "Andres Fabian, Creative Director · v0.1 working draft · October 2026", 14, False, GREY)

# R1 Why
s = slide("Section 01 · The reset", "We don't have a talent problem.\nWe have a system problem.")
cols(s, [
    ("No time to think", "Dates are set by asking \"when will it be done?\". A third of creative requests come with a day or less. Discovery and ideation get squeezed out."),
    ("Rework", "About a quarter of creative tasks are rework, edits or revisions. That's time that should have gone into the idea."),
    ("Nobody checks the right things", "QC checks grammar. Nobody checks the brief, the claims or the craft. Mistakes reach clients and look like ours."),
], size=14)
text(s, 0.7, 6.2, 11.9, 0.6, "The fix is a better system, and a higher bar we hold each other to.", 14, True, ACC)
notes(s, "Numbers from the Task Hub export, Apr 28 – Oct 9 2026. Rework is estimated from task names.")

# R2 Manifesto
s = slide("The reset", "What we stand for", dark=True)
text(s, 0.7, 2.3, 11.9, 3.8, "We do discovery on our own work.\nWe think before we make pixels.\nWe craft what leaves the building.\nWe show work every week and get better on purpose.", 30, True, WHITE, 1.35)

# R3 Expectations
s = slide("The reset", "What we expect, and how we'll know")
table(s, 0.7, 2.1, 11.9, [
    ["Expectation", "What it looks like", "How we know"],
    ["Discovery on every Full-track job", "Category audit wall, immersion, 2–3 insight candidates. 15% of the timeline", "Every G1 opens with your discovery share-out. No share-out, no G1"],
    ["Thinking before pixels", "20+ rough ideas, concept sentences, ADLOBs. 20% of the timeline", "The ACD reviews the wall, not the favourite"],
    ["Making the case", "Rationale, the insight's source, the competitive map", "On the slides at G1 and G2"],
    ["Crafted output", "Real-size checks, type hierarchy, image quality, licences, finish", "\"On brand\" signed by an AD who didn't make it"],
    ["Weekly crit", "45 minutes. Work shown before every G2", "Attendance, and work shown before G2"],
    ["Growth", "One personal craft goal, reviewed quarterly", "Every 1:1"],
], [2.8, 4.9, 4.2], 12, 0.6)

# R4 Two tracks
s = slide("The reset", "Two tracks: the process fits the job")
table(s, 0.7, 2.2, 11.9, [
    ["", "Light track", "Full track"],
    ["What", "Edits, resizes, variants, template changes to approved work", "New ideas, new builds, campaigns, rebrands, anything regulated"],
    ["Starts with", "Ticket + change log", "Signed one-page brief"],
    ["Your process", "Build → QC → send", "Discovery → Ideation → Platform → gates G1, G2, G3"],
    ["Reviewer", "A senior designer who didn't make it (web: Jordan)", "Andres, or an ACD who didn't make it"],
    ["Reaches the client", "Sent with the change log, after QC", "Presented by an ACD or CD"],
], [2.2, 4.8, 4.9], 13, 0.65)
text(s, 0.7, 6.3, 11.9, 0.5, "Maker is never checker: nobody reviews or QCs their own work.", 13, True, ACC)

# R5 Your day
s = slide("The reset", "Your day on the board")
cols(s, [
    ("By 9:40", "Move your cards to their real stage. Confirm yesterday's hours (one click). Mark anything blocked, with a reason and an owner."),
    ("9:45 stand-up", "15 minutes, PM-led. Your PM reads your cards; you answer three questions: What moves today? Will it make the promised date? What's blocking you, and who owns it?"),
    ("All day", "WIP limit: 3 cards in progress. If a date is at risk, say it early: the account lead talks to the client, not you."),
], size=14)
text(s, 0.7, 6.2, 11.9, 0.6, "No work on the board, no work. Untracked work goes on the board today.", 13, True, ACC)

# R6 QC
s = slide("The reset", "Nothing leaves without five YESes")
table(s, 0.7, 2.2, 11.9, [
    ["Question", "Checked by"],
    ["1 · Does it meet the brief?", "Account lead + ACD"],
    ["2 · Is it on brand?", "An AD who didn't make it"],
    ["3 · Does it deliver what was asked? Every change-log item done", "QC team (Judy, Katie)"],
    ["4 · Any mistakes? Claims and numbers confirmed; spelling, links, CTAs", "Account lead + QC team"],
    ["5 · Is the presentation ready?", "ACD"],
], [7.9, 4.0], 14, 0.7)
text(s, 0.7, 6.3, 11.9, 0.5, "Section 02 onwards is the field guide: how we do discovery, ideation, platforms and make the case.", 13, False, GREY)

# 2 Flow
s = slide("Section 02 · The field guide", "Three phases before anything gets polished")
cols(s, [
    ("01 · Discovery", "Understand the problem better than the client does. Find the truth worth dramatizing.\n\n15% of the timeline\nEnds in: insight candidates"),
    ("02 · Ideation", "Generate many rough ideas, then choose. Pen before pixels. Sentence before layout.\n\n20% of the timeline\nEnds in: G1 territories"),
    ("03 · Platform", "Turn the chosen idea into a system that makes dozens of executions.\n\n~25% of the timeline\nEnds in: G2 concept"),
], size=16)
text(s, 0.7, 6.3, 11.9, 0.5, "Full-track work. Light-track jobs (edits, resizes, variants) go straight to build and QC.", 15, True, ACC)

# 3 Discovery divider
s = slide("Phase 01", "Discovery", dark=True)
text(s, 0.7, 2.6, 11, 3, "Goal: arrive at ideation with a truth, not a mood board.\n\nInput: the signed one-page brief.\nOutput: 2–3 insight candidates, a category audit and a list of what everyone else does.", 24, False, WHITE, 1.4)

# 4 Discovery activities
s = slide("Phase 01 · Discovery", "What we do")
cols(s, [
    ("Interrogate the brief", "Who exactly is the one person? What is the one benefit? What is the real problem behind the ask? If the brief can't answer, bounce it."),
    ("Immerse", "Use the product. Walk the campus, read the IFU, sit through the application form. Talk to one real customer or front-line person if you can."),
    ("Audit the category", "Collect 20–30 competitor ads, sites and posts. Map what everyone does. That's the territory we avoid."),
    ("Hunt the tension", "Look for the gap between what people say and what they do, feel or fear. A truth with friction in it is an insight. A fact isn't."),
], size=14)

# 5 Discovery checklist
s = slide("Phase 01 · Checklist", "Before you leave Discovery")
checklist(s, [
    "I've read the signed brief and can say the proposition in one sentence",
    "I can describe the one person: a real human, not a demographic",
    "I've used or experienced the product or service myself",
    "Category audit done: 20+ examples, patterns named",
    "\"What everyone does\" list written, to avoid",
    "2–3 insight candidates, each written as one sentence with tension",
    "Every insight is true for this client, not any client in the category",
    "Mandatories and legal/MLR limits noted",
    "Questions for the brief owner raised, not guessed",
    "Discovery share-out ready: it opens the G1 presentation",
], size=15)

# 6 Ideation divider
s = slide("Phase 02", "Ideation", dark=True)
text(s, 0.7, 2.6, 11, 3, "Goal: many genuinely different ideas, then the courage to pick.\n\nInput: insight candidates.\nOutput: 2–3 territories ready for G1.", 24, False, WHITE, 1.4)

# 7 Ideation rules
s = slide("Phase 02 · Ideation", "House rules")
cols(s, [
    ("Quantity first", "Fill the wall before judging it. The first ideas are everyone's ideas; good ones usually come after the obvious ones are out."),
    ("Pen before pixels", "Thumbnails and sentences. No Figma polish, no mood boards pretending to be concepts."),
    ("Sentence first", "Every idea must be writable as one concept sentence. If you can't write it, it isn't an idea yet."),
    ("Judge later, ruthlessly", "Explore without a jury. Then converge hard: keep the few that are true, surprising and ownable."),
], size=14)

# 8 Ideation tools
s = slide("Phase 02 · Ideation", "Tools for when you're stuck")
table(s, 0.7, 2.2, 11.9, [
    ["Tool", "Ask", "Try it on"],
    ["Opposite", "What if we said or showed the reverse of the category?", "The category audit"],
    ["Show, don't tell", "How would we prove the benefit without stating it?", "The proposition"],
    ["Imply, don't reveal", "What can we leave out so the viewer completes it?", "The key visual"],
    ["Exaggerate", "Push the truth until it's absurd but still true", "The insight"],
    ["Fusion", "Merge two objects, worlds or symbols into one image", "Product + benefit"],
    ["Context shift", "Put the familiar somewhere unexpected", "Media and placement"],
    ["Literal language", "Take an expression from the category literally", "Audience language"],
], [2.4, 6.4, 3.1], 13, 0.55)
text(s, 0.7, 6.6, 11.9, 0.4, "Exaggerate, don't contrive: the idea must grow out of the truth, not be bolted on.", 13, False, GREY)

# 9 Ideation checklist
s = slide("Phase 02 · Checklist", "Before you take territories to G1")
checklist(s, [
    "20+ rough ideas on the wall before any were judged",
    "Ideas started on paper or as sentences, not in Figma",
    "Each territory is written as one concept sentence",
    "Each territory comes from a named insight",
    "Territories are genuinely different, not three colours of one idea",
    "Cold read: someone outside the project gets it in 5 seconds",
    "\"Done before?\" check run against the category and award annuals",
    "No territory relies on stock clichés of the category",
    "Each has a rough key visual + a headline + a why line",
    "ACD has reviewed the wall, not just the favourites",
], size=15)

# 10 What a territory looks like
s = slide("Phase 02 · Output", "A territory at G1")
items = [("Name", "Two or three words the team can call it"),
         ("Insight", "The truth it comes from"),
         ("Concept sentence", "The idea, in one line"),
         ("Rough key visual", "Sketch or scamp. Greyscale is fine"),
         ("Headline", "One line that could run"),
         ("Why it's right", "Its link to the brief")]
for i, (h, b) in enumerate(items):
    y = 2.25 + i * 0.72
    text(s, 0.7, y, 0.6, 0.6, f"{i+1}", 24, True, ACC)
    text(s, 1.4, y + 0.05, 3.4, 0.6, h, 18, True)
    text(s, 4.8, y + 0.08, 7.8, 0.6, b, 16, False, GREY)
notes(s, "Rough on purpose. Polish at G1 makes clients judge the execution instead of the idea.")

# 11 Platform divider
s = slide("Phase 03", "Campaign platform development", dark=True)
text(s, 0.7, 2.6, 11, 3, "Goal: prove the idea is a system, not a single ad.\n\nInput: the territory the client chose at G1.\nOutput: the G2 concept: a platform shown working across real channels.", 24, False, WHITE, 1.4)

# 12 What a platform is
s = slide("Phase 03 · Platform", "What a campaign platform contains")
cols(s, [
    ("Platform idea", "The concept sentence and the line that carries it. It should outlive any single execution."),
    ("Visual premise", "The rule behind the visuals: what we always do. A premise, not a template."),
    ("Voice", "How it sounds. Three do's and three don'ts, with examples."),
    ("System kit", "Type hierarchy, colour jobs, image rules, logo and legal lockups, motion behaviour."),
], size=14)

# 13 Platform tests
s = slide("Phase 03 · Platform", "Six tests a platform must pass")
table(s, 0.7, 2.2, 11.9, [
    ["Test", "How to run it", "Fails when"],
    ["Generativity", "List 10 executions in 10 minutes", "Ideas run dry after 3"],
    ["Ownability", "Cover the logo. Could a competitor run it?", "Yes"],
    ["Channel stretch", "Make it work as a Meta static, a :15 and a landing page", "It only works in one format"],
    ["Simplicity", "Say it in one sentence to someone outside the team", "It needs a paragraph"],
    ["Premise, not template", "Make two executions that look different but feel the same", "They only work if they look identical"],
    ["Longevity", "Could it run for 2–3 years?", "It's a one-season gag"],
], [2.4, 5.9, 3.6], 13, 0.6)

# 14 Platform steps
s = slide("Phase 03 · Platform", "How we build it")
steps = [("Hero execution", "Make the one piece that best shows the idea. Craft it properly."),
         ("Prove 3 channels", "Meta static, social video, web or landing page. Real sizes, real copy."),
         ("Write the rules", "Visual premise, voice, system kit, extracted from what worked."),
         ("Build the masters", "Figma master components per size, ready for the Variant Matrix."),
         ("Concept Card", "Insight, idea, why it's right, how it shows up, what to judge it on.")]
for i, (h, b) in enumerate(steps):
    x = 0.7 + i * 2.42
    rect(s, x, 2.3, 2.25, 0.06, ACC)
    text(s, x, 2.5, 2.25, 0.5, f"{i+1:02d}", 22, True, ACC)
    text(s, x, 3.05, 2.25, 0.9, h, 17, True)
    text(s, x, 3.9, 2.2, 2.5, b, 14, False, INK, 1.25)

# 15 Platform checklist
s = slide("Phase 03 · Checklist", "Before you take the platform to G2")
checklist(s, [
    "Platform idea fits in one sentence",
    "Hero execution is crafted, not placeholder",
    "Shown in at least 3 channels at real sizes",
    "Passes the six platform tests",
    "Visual premise written down, not just implied",
    "Type hierarchy delivers the idea in the right reading order",
    "Checked at real size: phone screen, feed, at a glance",
    "Real copy, approved claims, legal/MLR lines in place",
    "Figma masters built for the Variant Matrix",
    "Concept Card complete and checked against the signed brief",
], size=15)

# 15b Making the case: divider
s = slide("Section 03", "Making the case", dark=True)
text(s, 0.7, 2.6, 11, 3, "Good work loses when nobody can see the thinking.\n\nThe ADLOB, the rationale, the insight's source, the competitive map, the line, and how we steal well.", 24, False, WHITE, 1.4)

# 15c ADLOB
s = slide("Making the case", "The ADLOB: show the idea as an ad")
cols(s, [
    ("What it is", "An ad-like object: one idea rendered as a rough ad. A visual, a line, the logo. Black marker or greyscale. Not a mood board, not a strategy statement."),
    ("Why rough", "Clients and crits judge the idea, not the finish. Keep the layouts rough and the ideas fancy (Cosmopulos, via Barry)."),
    ("The tests", "Can I explain it on a Post-it? Where's the leap? Does the viewer complete it? Why only this brand? Does it make you smile, think or feel something (SLIP IT)?"),
    ("Fails when", "Execution without an idea. Strategy dressed as a concept. A visual gag with no brand in it. Clever without meaning."),
], size=13)
text(s, 0.7, 6.2, 11.9, 0.6, "One ADLOB per sheet. Cold read: pin it up, walk away, ask someone outside the project what it says.", 13, True, ACC)
notes(s, "ADLOB is CreativeEngine's internal term (creative-object-taxonomy.md). Method: Barry's roughs, one-sentence idea, cold read and SLIP IT.")

# 15d Rationale
s = slide("Making the case", "Every idea travels with its rationale")
table(s, 0.7, 2.2, 11.9, [
    ["Line", "Says", "Weak", "Strong"],
    ["1 · What we heard", "The problem in the client's terms", "\"You want more awareness.\"", "\"Riders think e-bikes are for people who can't ride.\""],
    ["2 · The truth we found", "The insight, with its source", "\"People love freedom.\"", "\"In 12 interviews, riders hid the battery in photos.\" (Observed)"],
    ["3 · The idea", "One sentence", "\"A bold, modern campaign.\"", "\"Show the hill, not the bike.\""],
    ["4 · Why it works", "Link to the proposition and the audience", "\"It's fresh and eye-catching.\"", "\"It sells the one benefit without saying 'electric'.\""],
], [2.2, 2.9, 2.6, 4.2], 12, 0.75)
text(s, 0.7, 6.2, 11.9, 0.6, "Four lines, said out loud in under 30 seconds. If line 2 has no source, it's an opinion. (Example is invented.)", 13, True, ACC)

# 15e Insight source
s = slide("Making the case", "Show where the insight came from")
cols(s, [
    ("The truth", "One sentence with tension. A truth with friction in it is an insight; a fact isn't."),
    ("The proof", "The quote, the data point, the photo from the immersion, the review that says it in the customer's words. Put it on the slide."),
    ("The label", "Verified (client data, research, performance) · Observed (discovery, conversations) · Hypothesis (marked, to be tested)."),
], size=14)
text(s, 0.7, 6.2, 11.9, 0.6, "The \"What we learned\" slide in every G1: truth + proof + label. Clients trust what they can see.", 13, True, ACC)

# 15f Competitive map
s = slide("Making the case", "Show the category before you show the idea")
cols(s, [
    ("Collect", "20–30 competitor ads, sites and posts. Screenshots with dates and links. Meta Ad Library for what's running now."),
    ("Map it", "Group by what they say and how they look. Name the patterns: \"everyone shows smiling graduates\", \"everyone leads with price\"."),
    ("Find the gap", "What nobody owns, that's true for us. That's the white space the territories aim at."),
    ("Show it", "One slide before the territories: the wall, the patterns, the gap. It makes our idea look as different as it is."),
], size=13)

# 15g Lines
s = slide("Making the case", "Headlines, taglines and slogans")
table(s, 0.7, 2.1, 11.9, [
    ["", "Headline", "Tagline / endline"],
    ["Job", "Sells this execution, now", "Carries the brand or campaign for years"],
    ["Lives", "In one ad", "Beside the logo, everywhere"],
    ["Test", "Does it stop you and make the visual better (1+1=3)?", "Stronger beside the brand name? Could a competitor say it? Will it last 3 years?"],
], [1.6, 5.0, 5.3], 13, 0.65)
text(s, 0.7, 4.9, 11.9, 1.6,
     "Write 30 to find 1: the good ones come in the middle and the end of the list (Barry's 1-in-10).\n"
     "Land the twist as late as possible, and cut every word after it. No exclamation marks.\n"
     "Say it out loud. If it's hard to say, it won't be repeated.",
     14, False, INK, 1.4)

# 15h Steal
s = slide("Making the case", "Steal like a pro")
cols(s, [
    ("Steal the mechanism", "Not the look. Ask how the ad works: reversal, omission, fusion, exaggeration, a twist. Then apply that engine to our truth."),
    ("Combine three", "One source is a copy. Three sources is a new idea. Mix a mechanism, a tone and a format from different places."),
    ("Know the line", "Taking a nugget and building on it is craft. Lifting a strategy, a line or an image is plagiarism (Barry)."),
    ("Keep a library", "Add one reference a week to the team library with why it works. Run a \"done before?\" check before any idea is shown. Credit references in pitch decks."),
], size=13)

# 15i Whipple: squeeze it
s = slide("Making the case", "Squeeze it: find the idea before the words")
cols(s, [
    ("Reduce", "Fill the blank: THIS BRAND = ____. THIS CAMPAIGN IS REALLY ABOUT ____. If a competitor could write the same answer, keep going."),
    ("Truth + conflict", "A truth with no conflict is an observation. Conflict with no truth is a gimmick. Look between what people say and what they do."),
    ("Find the enemy", "What are we fighting? A category habit, a belief, a hassle, an old assumption. Not a competitor, and never a manufactured fight."),
    ("Three truths", "Where do the product truth, the human truth and the cultural truth meet? Search there."),
], size=13)
notes(s, "Inspired by principles associated with Luke Sullivan's Hey Whipple, Squeeze This (CreativeEngine framework: hey-whipple-copycraft.md). Labels are ours, not quotes from the book.")

# 15j Whipple: shake out the ugly
s = slide("Making the case", "Shake out the ugly: six rounds of writing")
table(s, 0.7, 2.1, 11.9, [
    ["Round", "Write"],
    ["A · Obvious", "The expected category answers. Get them out of your system first"],
    ["B · Opposite", "What would the category never say?"],
    ["C · Human", "From real behaviour: contradiction, embarrassment, pride, laziness, status, fear"],
    ["D · Product", "Demonstrations, consequences, odd details, proof, unexpected uses"],
    ["E · Culture", "Language, rituals, memes, taboos and tensions around the problem"],
    ["F · Form", "Different structures, and different ways the words and the picture meet"],
], [2.4, 9.5], 13, 0.58)
text(s, 0.7, 6.3, 11.9, 0.5, "Bad early ideas are allowed. The goal is to get past the first idea, not to fill a list.", 13, True, ACC)

# 15k Whipple: stress test
s = slide("Making the case", "Before a line goes in front of anyone")
cols(s, [
    ("Stop + idea", "Would I notice it? Is there a thought, or only phrasing? Could it belong to another brand?"),
    ("Tension + reward", "Is there friction or surprise? Does the reader get a small payoff for getting it (the smile in the mind)?"),
    ("1 + 1 = 3", "With its image, does it say something neither says alone? If the line repeats the picture, cut one."),
    ("Squeeze", "Cut set-up, duplicate meaning, empty adjectives, strategy words, and the explanation of the joke. Can one more word go?"),
], size=13)
text(s, 0.7, 6.2, 11.9, 0.6, "Not a scorecard. Ask the questions, then trust the room at crit.", 13, True, ACC)

# 16 Before you present
s = slide("Every gate", "Before you present anything")
checklist(s, [
    "Does it answer the signed brief? Point to the line",
    "Can I say the idea in one sentence?",
    "Would it survive a cold read in 5 seconds?",
    "Is it specific to this client, or could it be anyone's?",
    "Any generic AI tells (stock gradients, glossy sameness, filler copy)?",
    "Is the fidelity right for this gate, no more and no less?",
    "Is it in the agency presentation spine?",
    "Do I know which decisions I need from the client?",
], size=16)

# 16b Weekly crit
s = slide("Every week", "Weekly crit: 45 minutes")
table(s, 0.7, 2.2, 11.9, [
    ["Minutes", "What happens"],
    ["0–5", "One sentence each: what you're showing and what you want from the room"],
    ["5–35", "3 pieces, 10 minutes each. Maker shows, the room asks, then critiques: brief, idea, craft, in that order"],
    ["35–40", "One reference someone found this week, and why it's good"],
    ["40–45", "Each maker names the one change they'll make"],
], [1.6, 10.3], 14, 0.7)
text(s, 0.7, 5.7, 11.9, 0.9, "Every Full-track job is shown at crit before G2. Critique the work, not the person. Specific beats nice.", 15, True, ACC)

# 17 Red flags
s = slide("Watch for", "Red flags in a crit")
cols(s, [
    ("Design before idea", "Beautiful layout, no sentence. A mood board presented as a concept."),
    ("Template thinking", "Every execution is the same layout with new words. That's a template, not a premise."),
    ("Category clichés", "The stock image every competitor would use. If it's on the audit wall, it's out."),
    ("First-round AI", "Unedited AI images or copy standing in for thinking. AI can explore; it can't decide."),
], size=14)

# 18 AI
s = slide("Tools", "Using AI well")
table(s, 0.7, 2.2, 11.9, [
    ["Use AI for", "Don't use AI for"],
    ["Category audits and reference gathering", "Writing the insight for you"],
    ["Generating many rough variations in ideation", "Choosing which idea is good"],
    ["Comps, pre-viz and pitch mood (credited, never final)", "Final assets presented as finished work"],
    ["Checking a concept: has it been done before?", "Replacing sketching and thinking time"],
    ["Brainstorm partner for headlines and angles (you choose)", "Skipping craft QA"],
], [5.95, 5.95], 14, 0.65)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "outputs", "review", "The_Craft_v0.1.pptx")
p.save(out)
print(out, n[0])
