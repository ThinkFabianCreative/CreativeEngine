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
FONT = "Inter"

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
        r.font.name, r.font.size, r.font.bold = FONT, Pt(size), bold
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
    text(s, 0.7, 7.0, 6, 0.3, "THE CRAFT · Designer field guide · v0.1 draft", 10, False, GREY)
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


