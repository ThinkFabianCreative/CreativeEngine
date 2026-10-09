// Figma Slides build-state generator: TMTT XLT deck (Slides file sBqCMoTCaPupEZj9aRleUq).
// Run LAST, through use_figma, once the 7 masters are locked (including the Vesta swap).
// For each slide: it clones the master once per CLICK. In each state, layers not yet revealed
// get opacity 0 and +40px y. States are wired with Smart Animate on click; the master keeps
// Yash's notes and later states get "(build N of slide 0X)".
// Reveal groups are matched by layer-name prefix / text start, from Yash's CLICK cues (build-spec.md).
// Masters are never edited by this script except to set their own transition.
// To regenerate: first delete all slides after each master in its row, then run this.

const REVEALS = {
  // masterId: [ [click1 matchers], [click2 matchers], ... ]  (a matcher matches node.name startsWith or TEXT characters startsWith)
  '3:2':  [['Tagline', 'XLT']],
  '3:10': [['Rectangle@C-frame', 'Rectangle@panel', 'Your guests'], ['That’s the value']],
  '3:34': [['Our promise'], ['Rectangle@rule', 'with the full', 'Empower', 'Repair', 'across the', 'Enable', 'Expertise', 'what comes', 'Elevate', 'Every case']],
  '3:52': [['TCT']],
  '4:5':  [['EXTERNAL', 'What customers', '01', 'Heart Teams', 'They value', '02', 'Physicians', 'Four behavioral'],
           ['INTERNAL', 'What it asks', '03', 'The portfolio supports', 'Therapy campaigns stay', '04', 'What sets us', 'Finding patients']],
  '4:25': [['Today'], ['ONE STORY', 'Portfolio promise', 'Three pillars', 'The & creative', 'Therapy campaigns', 'JOURNEY', 'who ·', 'Adobe'],
           ['What we learn', '2027'], ['Portfolio marketing', 'Audience intelligence', 'Brand', 'Content system', 'Digital', 'Orchestration'], ['2.7x', 'more case volume']],
  '4:86': [['Use the playbook', 'One story, told', 'Keep therapy', 'The portfolio supports', 'Build the partner', 'A multi-year', '&@separator'], ['Patient-matched']],
};
// NOTE: matchers ending in @... are placeholders. Resolve them to real node IDs by inspecting each master
// before running (e.g. the C highlight frame, the dark panel, the eyebrow rule, the 72px separator "&"s).
// The generator body is written at run time from this map. Keep this file as the source of truth for reveal order.
