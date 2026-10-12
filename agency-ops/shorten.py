"""Build the short presented decks (v0.2): chosen slides first, then an Appendix divider and the rest."""
import copy, sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

def shorten(src, out, main, label, head="Inter", body="Inter"):
    p = Presentation(src)
    n = len(p.slides)
    # appendix divider
    s = p.slides.add_slide(p.slide_layouts[6])
    f = s.background.fill; f.solid(); f.fore_color.rgb = RGBColor(0x14, 0x14, 0x14)
    tb = s.shapes.add_textbox(Inches(0.7), Inches(2.6), Inches(11.9), Inches(2))
    tf = tb.text_frame; tf.word_wrap = True
    r = tf.paragraphs[0].add_run(); r.text = "Appendix"
    r.font.size = Pt(60); r.font.bold = head == "Inter"; r.font.name = head; r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    pp = tf.add_paragraph(); r2 = pp.add_run(); r2.text = f"The detail behind {label}. For reference, not for the room."
    r2.font.size = Pt(22); r2.font.name = body; r2.font.color.rgb = RGBColor(0xBB, 0xBB, 0xBB)
    ids = list(p.slides._sldIdLst)
    order = [i - 1 for i in main] + [n] + [i for i in range(n) if i + 1 not in main]
    lst = p.slides._sldIdLst
    for el in ids: lst.remove(el)
    for i in order: lst.append(ids[i])
    # renumber the page-number boxes (right-hand footer)
    for k, sl in enumerate(p.slides, 1):
        for sh in sl.shapes:
            if sh.has_text_frame and sh.left > Inches(12) and sh.top > Inches(6.8) and sh.text_frame.text.strip().isdigit():
                run = sh.text_frame.paragraphs[0].runs[0]; run.text = f"{k:02d}"
    p.save(out); print(out, len(main), "presented +", n - len(main), "appendix")

shorten("The_Standard_v0.1.pptx", "The_Standard_v0.2.pptx", [1, 2, 3, 32, 6, 18, 21, 14, 22, 33], "The Standard", head="Libre Caslon Text", body="Acumin Pro")
shorten("The_Craft_v0.1.pptx", "The_Craft_v0.2.pptx", [1, 2, 3, 4, 6, 8, 10, 13, 18, 23, 24, 33], "The Craft", head="Libre Caslon Text", body="Acumin Pro")
