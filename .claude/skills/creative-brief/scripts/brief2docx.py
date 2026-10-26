import re,sys
from docx import Document
from docx.shared import Pt,Cm,RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
RED=RGBColor(0xC8,0x10,0x2E); GREY=RGBColor(0x59,0x59,0x59); DARK=RGBColor(0x26,0x26,0x26)
src=open(sys.argv[1],encoding='utf-8').read().splitlines()
d=Document()
for s in d.sections: s.left_margin=s.right_margin=Cm(2.0); s.top_margin=s.bottom_margin=Cm(1.6)
st=d.styles['Normal']; st.font.name='Arial'; st.font.size=Pt(10); st.font.color.rgb=GREY
st.element.rPr.rFonts.set(qn('w:eastAsia'),'Arial')
pf=st.paragraph_format; pf.space_after=Pt(3); pf.space_before=Pt(0); pf.line_spacing=1.15
def runs(p,t):
    for part in re.split(r'(\*\*.+?\*\*|\*[^*]+?\*)',t.replace('`','')):
        if not part: continue
        if part.startswith('**'): r=p.add_run(part[2:-2]); r.bold=True; r.font.color.rgb=DARK
        elif part.startswith('*'): r=p.add_run(part[1:-1]); r.italic=True
        else: r=p.add_run(part)
def rule(p,color='C8102E',sz='8'):
    pPr=p._p.get_or_add_pPr(); b=OxmlElement('w:pBdr'); bt=OxmlElement('w:bottom')
    for k,v in (('w:val','single'),('w:sz',sz),('w:space','4'),('w:color',color)): bt.set(qn(k),v)
    b.append(bt); pPr.append(b)
for l in src:
    if l.startswith('@ '):
        a,b,c=[x.strip() for x in l[2:].split('|')]
        for txt,size,col,bold in ((a,22,RED,True),(b,10,RED,True),(c,8.5,GREY,False)):
            p=d.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.RIGHT; p.paragraph_format.space_after=Pt(0)
            r=p.add_run(txt); r.bold=bold; r.font.size=Pt(size); r.font.color.rgb=col
        rule(p); p.paragraph_format.space_after=Pt(6)
    elif l.startswith('## '):
        p=d.add_paragraph(); p.paragraph_format.space_before=Pt(11); p.paragraph_format.space_after=Pt(2); p.paragraph_format.keep_with_next=True
        r=p.add_run(l[3:].replace('*','').upper()); r.bold=True; r.font.size=Pt(12); r.font.color.rgb=RED
    elif l.startswith('### '):
        p=d.add_paragraph(); p.paragraph_format.space_before=Pt(5); p.paragraph_format.space_after=Pt(1); p.paragraph_format.keep_with_next=True
        r=p.add_run(l[4:]); r.bold=True; r.font.size=Pt(10.5); r.font.color.rgb=DARK
    elif l.startswith('> '):
        p=d.add_paragraph(); p.paragraph_format.space_after=Pt(1); p.paragraph_format.left_indent=Cm(0.35); p.paragraph_format.line_spacing=1.0
        for part in re.split(r'(\*\*.+?\*\*)',l[2:]):
            if not part: continue
            r=p.add_run(part.strip('*')); r.font.size=Pt(8.5); r.font.color.rgb=RGBColor(0x8C,0x8C,0x8C)
            if part.startswith('**'): r.bold=True
    elif l.startswith('- '):
        p=d.add_paragraph(style='List Bullet'); p.paragraph_format.space_after=Pt(1); runs(p,l[2:])
    elif l.strip()=='---':
        p=d.add_paragraph(); rule(p,'BFBFBF','4')
    elif l.strip(): runs(d.add_paragraph(),l)
d.save(sys.argv[2])
