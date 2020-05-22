import datetime, time
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER, TA_RIGHT

# Creating document
doc = SimpleDocTemplate("firefighter_test.pdf", pagesize=letter,
                        rightMargin=9, leftMargin=25,
                        topMargin=20, bottomMargin=20)          # constructor of document with settings for margins

# Elements on page which will be print
elements = []

# Setting additional styles for document
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Left', fontName='Times'))
styles.add(ParagraphStyle(name='Center', fontName='Times', alignment=TA_CENTER))    # style for good looking document
styles.add(ParagraphStyle(name='Right', fontName='Times', alignment=TA_RIGHT))        # style to set paragraph on right side of page

date = datetime.datetime.now().date()
ptext = f'<font size="12">Kraków, dn. {date.day}.{date.month}.{date.year}</font>'
elements.append(Paragraph(ptext, styles['Right']))
elements.append(Spacer(1, 12))

day_of_year = time.localtime().tm_yday
ptext = f'<font size="16">ROZKAZ DZIENNY NR {day_of_year}/{date.year}</font>'
elements.append(Paragraph(ptext, styles['Center']))
elements.append(Spacer(1, 12))

ptext = '<font size="12">Dowódcy Jednostki Ratunkowo Gaśniczej Nr 4</font>'
elements.append(Paragraph(ptext, styles['Center']))
elements.append(Spacer(1, 12))

ptext = f'<font size="12">z dnia {date.day}.{date.month}.{date.year}</font>'
elements.append(Paragraph(ptext, styles['Center']))
elements.append(Spacer(1, 12))

doc.build(elements)
