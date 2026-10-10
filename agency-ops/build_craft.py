exec(open(__file__.replace("build_craft.py", "_helpers.py")).read())


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
text(s, 0.7, 3.9, 11, 1, "How we get from a signed brief to a campaign platform.\nA field guide for the design team.", 24, False, WHITE)
text(s, 0.7, 6.2, 11, 0.6, "Andres Fabian, Creative Director · v0.1 working draft · October 2026", 14, False, GREY)

# 2 Flow
s = slide("The flow", "Three phases before anything gets polished")
cols(s, [
    ("01 · Discovery", "Understand the problem better than the client does. Find the truth worth dramatizing.\n\n~15% of the timeline\nEnds in: insight candidates"),
    ("02 · Ideation", "Generate many rough ideas, then choose. Pen before pixels. Sentence before layout.\n\n~20% of the timeline\nEnds in: G1 territories"),
    ("03 · Platform", "Turn the chosen idea into a system that makes dozens of executions.\n\n~25% of the timeline\nEnds in: G2 concept"),
], size=16)
text(s, 0.7, 6.3, 11.9, 0.5, "Concept before polish. Craft never disguises a weak idea.", 15, True, ACC)

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
    "Discovery shared with the ACD before ideation starts",
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
    ["Generating Variant Matrix files from masters", "Skipping craft QA"],
], [5.95, 5.95], 14, 0.65)

out = __file__.replace("build_craft.py", "The_Craft_v0.1.pptx")
p.save(out)
print(out, n[0])
