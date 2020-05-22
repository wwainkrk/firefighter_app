from reportlab.pdfgen import canvas
# from reportlab.rl_config import defaultPageSize
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_JUSTIFY, TA_RIGHT

# Creating document
# pdf = canvas.Canvas("firefighter_test.pdf")
# draw_my_ruler(pdf)                                # execute some helping labels

doc = SimpleDocTemplate("firefighter_test.pdf", pagesize=letter,
                        rightMargin=9, leftMargin=25,
                        topMargin=20, bottomMargin=20)          # constructor of document with settings for margins

# Elements on page which will be print
elements = []

# Setting additional styles for document
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Left', fontName='Times'))
styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))    # style for good looking document
styles.add(ParagraphStyle(name='Right', alignment=TA_RIGHT))        # style to set paragraph on right side of page

ptext = '<font size="12">Times New Roman</font>'
elements.append(Paragraph(ptext, styles['Left']))


# Setting fonts for document
# print(pdf.getAvailableFonts())
# print(PAGE_HEIGHT, PAGE_WIDTH)

#pdf.setFont("Times-Roman", 20)
#pdf.drawCentredString(PAGE_HEIGHT/2, PAGE_WIDTH/2, "Times New Roman")
#pdf.save()

doc.build(elements)
