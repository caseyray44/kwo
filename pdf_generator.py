from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib import colors
from io import BytesIO
from PIL import Image as PILImage

def create_sop_pdf(title, toc, sections):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, topMargin=0.5*inch, bottomMargin=0.5*inch)
    styles = getSampleStyleSheet()
    story = []
    
    # Title
    story.append(Paragraph(title, styles["Title"]))
    story.append(Spacer(1, 0.3 * inch))
    
    # Table of Contents
    story.append(Paragraph("Table of Contents", styles["Heading1"]))
    toc_data = [[Paragraph(line, styles["BodyText"]) for line in toc.split("\n")] for line in toc.split("\n")]
    toc_table = Table(toc_data)
    toc_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0)
    ]))
    story.append(toc_table)
    story.append(Spacer(1, 0.3 * inch))
    
    # Sections
    for sec in sections:
        if not (sec["content"] or sec["lists"] or sec["photos"]):
            continue
        story.append(Paragraph(sec["title"], styles["Heading1"]))
        story.append(Spacer(1, 0.2 * inch))
        
        if sec["content"]:
            story.append(Paragraph(sec["content"], styles["BodyText"]))
            story.append(Spacer(1, 0.2 * inch))
        
        if sec["lists"]:
            for i, item in enumerate(sec["lists"].split("\n"), 1):
                if item.strip():
                    story.append(Paragraph(f"{i}. {item}", styles["BodyText"]))
                    story.append(Spacer(1, 0.1 * inch))
        
        if sec["photos"]:
            for photo in sec["photos"]:
                img = PILImage.open(photo)
                img_width, img_height = img.size
                max_width = 3 * inch
                if img_width > max_width:
                    ratio = max_width / img_width
                    img_width = max_width
                    img_height *= ratio
                photo.seek(0)
                story.append(Image(photo, width=img_width, height=img_height))
                story.append(Spacer(1, 0.2 * inch))
    
    doc.build(story)
    buffer.seek(0)
    return buffer
