// CD feedback page for Figma file uMbsQueRTlDnrD9lFkPNFe (SAPIEN M3 RESILIA 2026).
// Source: territory-review_v01.md (creative-engine-director, 2026-10-15).
// Run with the Figma MCP use_figma tool (skillNames: figma-use). It needs edit access to the file.
// Adds a new page "CD feedback" with six 1920x1080 frames. It touches no existing page or node.
// Safe to retry: if a page named "CD feedback" already exists, it stops without changes.

if (figma.root.children.some(p => p.name === 'CD feedback')) {
  return { skipped: true, reason: 'A page named "CD feedback" already exists; nothing changed.' };
}

const R = { family: 'Inter', style: 'Regular' };
const B = { family: 'Inter', style: 'Bold' };
const SB = { family: 'Inter', style: 'Semi Bold' };
await Promise.all([R, B, SB].map(f => figma.loadFontAsync(f)));

const BG = { r: 0.09, g: 0.09, b: 0.1 };
const WHITE = { r: 1, g: 1, b: 1 };
const GREY = { r: 0.72, g: 0.72, b: 0.74 };
const RED = { r: 0.84, g: 0.2, b: 0.24 };
const BEIGE = { r: 0.86, g: 0.78, b: 0.66 };

const page = figma.createPage();
page.name = 'CD feedback';
await figma.setCurrentPageAsync(page);

const created = [page.id];

function text(parent, chars, font, size, color, width) {
  const t = figma.createText();
  t.fontName = font;
  t.fontSize = size;
  t.characters = chars;
  t.fills = [{ type: 'SOLID', color }];
  t.lineHeight = { unit: 'PERCENT', value: 140 };
  parent.appendChild(t);
  if (width) { t.textAutoResize = 'HEIGHT'; t.resize(width, t.height); }
  created.push(t.id);
  return t;
}

function slide(i, kicker, title) {
  const f = figma.createAutoLayout('VERTICAL', { name: `CD feedback ${String(i).padStart(2, '0')} · ${title}` });
  page.appendChild(f);
  f.x = (i - 1) * 2040; f.y = 0;
  f.primaryAxisSizingMode = 'FIXED'; f.counterAxisSizingMode = 'FIXED';
  f.resize(1920, 1080);
  f.paddingLeft = f.paddingRight = 140; f.paddingTop = 120; f.paddingBottom = 100;
  f.itemSpacing = 28;
  f.fills = [{ type: 'SOLID', color: BG }];
  created.push(f.id);
  text(f, kicker.toUpperCase(), SB, 20, RED);
  text(f, title, B, 64, WHITE, 1640);
  return f;
}

function columns(parent, cols) {
  const row = figma.createAutoLayout('HORIZONTAL', { name: 'Columns', itemSpacing: 80 });
  parent.appendChild(row);
  row.layoutSizingHorizontal = 'FILL';
  created.push(row.id);
  const w = Math.floor((1640 - 80 * (cols.length - 1)) / cols.length);
  for (const c of cols) {
    const col = figma.createAutoLayout('VERTICAL', { name: c.head, itemSpacing: 14 });
    row.appendChild(col);
    created.push(col.id);
    text(col, c.head, SB, 26, c.color || BEIGE, w);
    text(col, c.body, R, 22, GREY, w);
  }
  return row;
}

// 01 Summary
let s = slide(1, 'Creative Director feedback · Territories, not finished animations · Oct 2026', 'Both territories: REWORK. Recommended route: a fusion.');
text(s, 'Judged as territories: the idea, fit with the brief, whether it survives the :30, and claim safety. Finish is not judged. Verdicts use CreativeEngine’s scale (KILL · REWORK · ADVANCE · BET THE PITCH).', R, 26, GREY, 1640);
columns(s, [
  { head: '01 Nature meets Science — REWORK', body: 'Keep: the wingbeat-to-leaflets match-cut (the best single idea in the deck) and the warm palette.\nFix: the “body does it naturally” premise produces claims Edwards can’t make; the nature montage is generic; the product arrives at scene 6; written for a VO the brief doesn’t ask for; doesn’t survive the :30.' },
  { head: '02 Precisely Engineered — REWORK', body: 'Keep: product-first, titles-only, pillars in order; it survives the :30.\nFix: robotic arms in a sci-fi lab is a category cliché on Edwards’ avoid list; may misstate how the valve is made (ask Edwards); the device renders don’t show the real dock and valve; it never shows what the dock does; heart static, background not beige.' },
  { head: 'Recommended: fuse on the brief’s spine', body: 'T02’s skeleton + T01’s one real idea, built on the brief’s main concept: the red glass heart moving forward on beige.\nWorking concept sentence (not a line): “The system draws the heart’s own anatomy inward, so the heart can keep moving forward.”' , color: RED },
]);

// 02 T01
s = slide(2, 'Territory 01', 'Nature meets Science');
columns(s, [
  { head: 'Strengths', body: '• Wingbeat match-cut into leaflets opening and closing gives the required RESILIA moment a meaning, not just a render.\n• Warm, organic, “never sterile”; the glass heart on beige with speed streaks is the closest image to the brief’s two fixed elements.\n• A point of view in a category that defaults to spec sheets.' },
  { head: 'Weaknesses', body: '• The premise keeps generating unsupported “natural” claims. The only sourced naturalness claim is about the dock: “designed to support natural annular motion”.\n• Honeycomb, DNA, tree rings, fingerprints: a montage that could open a film for any product. DNA is on Edwards’ avoid list. “Nature meets Science” is the “Where X meets Y” formula.\n• Product name at scene 6; the dock mechanism never appears; outcomes crowded into the end card.\n• Copy sits in a Narration column; 6 of 10 scenes have no on-screen text. Brief: text on screen, no narration needed. “Morgan Freeman-type VO” asks for a sound-alike — needs a decision.\n• “A new life for heart patients everywhere” overreaches a narrow indication.\n• The three pillars are not the structure.' },
]);

// 03 T02
s = slide(3, 'Territory 02', 'Precisely Engineered');
columns(s, [
  { head: 'Strengths', body: '• Product-first: suits a launch film, text-only format and the :30.\n• Device placed into the red glass heart is a usable climax and a natural home for the dock / valve-in-dock sequence.\n• Outcomes block is closest to the messaging doc (keeps “ENCIRCLE main cohort”, “through 2 years”).\n• Touches all three pillars in order.' },
  { head: 'Weaknesses', body: '• Robotic arms, blue light, sci-fi abstraction, electronic score: the default precision spot. Edwards avoids “fake futuristic medicine or labs” and “sci-fi for its own sake”. Low ownability.\n• May misstate manufacturing. Unverified: Edwards tissue valves may be hand-sewn — if so, a human-hands story is truer and stronger. Ask Edwards.\n• Device renders appear AI-generated and don’t depict the SAPIEN M3 dock or valve. Edwards rule: never generate their products, even in comps. Flag only — Andres decides.\n• Shows how it’s made, not what it does: the dock drawing anatomy inward is absent.\n• Dark red-black ground; the heart doesn’t move forward.\n• A list of supers, not a story.' },
]);

// 04 Route
s = slide(4, 'Recommended route', 'Inward and forward');
text(s, 'Sourced truth (messaging doc): the dock draws the mitral apparatus “inward, rather than expanding outward against the anatomy”; native leaflet-based anchoring is “designed to support natural annular motion”. The second half of the concept sentence is a metaphor, not an outcome claim — copy and MLR keep it that way.', R, 26, GREY, 1640);
columns(s, [
  { head: ':60 beats (indicative, text on screen only)', body: '0–8s  Red glass heart moves forward on beige, then slows.\n8–30s  INNOVATION. Inside the heart: dock encircles, draws leaflets and chordae inward; valve deployed within the dock; RESILIA leaflets open and close. One nature rhyme here only (wingbeat or petal).\n30–45s  OUTCOMES. ENCIRCLE logo unchanged; data in the messaging doc’s wording; pillar icon slot.\n45–55s  LEGACY. “Trusted SAPIEN Platform. Built for Mitral.” RESILIA with “surgical” and the † treatment; pillar icon slot.\n55–60s  Heart resumes moving forward. End card, indication, footnotes.' },
  { head: ':30 and next steps', body: 'Heart forward → dock draws inward → valve and leaflets → one outcome beat → heart forward + end card. Write the :30 first to prove the spine.\n\nCopy: rewrite every super in the messaging doc’s wording; 3 different end lines; no superlatives, no “evolve”, no “where X meets Y”.\nDesign: storyboard on beige; device shots from approved reference only, labelled placeholders until then; three pillar-icon slots; plan footnote and disclaimer layout.\nOptional round: a human-hands craft story, only if Edwards confirms the valves are hand-made.' },
]);

// 05 Claims
s = slide(5, 'Fix before anything goes to Edwards', 'Claim drift against the 9/30 messaging');
columns(s, [
  { head: 'Correct the wording', body: '• “96% of patients achieving MR ≤1+” → 97% (and it is not “supplied copy”).\n• “The only controlled, reproducible mitral valve replacement” → no “only”, no “controlled”; doc: “Designed to empower reproducible…”.\n• “Sustained MR reduction” → doc: “consistent, near MR elimination”.\n• “RESLIA” typo.\n• “Prevent calcification” → doc: “proven to reduce calcification”, with the † disclaimer.\n• “Advancing TMVR like never before” → “advances TMVR”.\n• “Below 1% within 30-day mortality” → “Main cohort 30-day mortality <1%”.\n• “Responsive from access to deployment” → “Reassurance From Access to Deployment”.\n• “Evidence Demonstrates Efficacy” → use the full header.' },
  { head: 'Delete or hold', body: 'Delete — no source:\n• “Lets the body return to its natural state”\n• “Blood now flows effortlessly… as it naturally should”\n• “Effortlessly. Efficiently. Perfectly.” · “extraordinary… unprecedented”\n• “A new life for heart patients everywhere”\n• “From the leader of structural heart expertise” → doc: “Founded in Deep Structural Heart Expertise”\n• “Groundbreaking”, “new leading technology”, “could only come from EDWARDS”\n\nHold until Edwards answers:\n• ENCIRCLE / MAC outcomes under the SAPIEN M3 RESILIA name (doc footnote * says SAPIEN M3)\n• “near MR elimination” vs “MR elimination”\n• “Introducing” / “new” while U.S. status is unknown\n• Any RESILIA proof without “surgical” and the † disclaimer', color: RED },
]);

// 06 Questions
s = slide(6, 'Before the next round', 'What to ask Edwards');
text(s, '1. May ENCIRCLE and MAC outcomes appear under the SAPIEN M3 RESILIA name, or must they read “SAPIEN M3”?\n2. “Near MR elimination” or “MR elimination”?\n3. What approved device reference (CAD, renders, existing M3 animation) do we animate the dock, valve and leaflets from?\n4. Which footnotes, disclaimers and indication text must appear on screen in the :60 and :30?\n5. U.S. approval and launch status: can we say “Introducing” or “new”?\n6. Which messaging was “highlighted in green” (the required lines)?\n7. Is “performance in motion” the campaign agency’s line, and may we use it?\n8. How are SAPIEN M3 RESILIA valves made?\n9. When do the campaign artwork (heart moving forward) and the pillar icons arrive?\n10. Is narration welcome, or is the film text-only?\n\nAlso before Edwards: run a done-before precedent check on the fused route, and check every claim against the original messaging document, not the transcription.', R, 26, GREY, 1640);

return { pageId: page.id, frames: page.children.map(n => ({ id: n.id, name: n.name })), createdCount: created.length, createdNodeIds: created };
