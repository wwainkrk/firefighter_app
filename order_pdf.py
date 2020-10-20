import datetime, time
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.platypus import ListFlowable, ListItem
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER, TA_RIGHT

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Creating document
doc = SimpleDocTemplate("firefighter_test.pdf", pagesize=letter,
                        rightMargin=9, leftMargin=25,
                        topMargin=20, bottomMargin=20)          # constructor of document with settings for margins

# Elements on page which will be print
elements = []

# Register font and set style with new Font
pdfmetrics.registerFont(TTFont('FreeSans', "fonts/FreeSans.ttf"))
pdfmetrics.registerFont(TTFont('FreeSansBold', "fonts/FreeSansBold.ttf"))
pdfmetrics.registerFont(TTFont('FreeSansItalic', "fonts/FreeSansOblique.ttf"))

# Setting additional styles for document
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Left', fontName='FreeSans'))
styles.add(ParagraphStyle(name='HeaderBoldCenter', fontName='FreeSansBold', alignment=TA_CENTER))    # style for good looking document
styles.add(ParagraphStyle(name='HeaderCenter', fontName='FreeSans', alignment=TA_CENTER))
styles.add(ParagraphStyle(name='Right', fontName='FreeSans', alignment=TA_RIGHT))        # style to set paragraph on right side of page
styles.add(ParagraphStyle(name='FooterBoldRight', fontName='FreeSansBold', alignment=TA_RIGHT))

date = datetime.datetime.now().date()
ptext = f'<font size="12">Kraków, dn. {date.day}.{date.month}.{date.year}</font>'
elements.append(Paragraph(ptext, styles['Right']))
elements.append(Spacer(1, 12))

day_of_year = time.localtime().tm_yday
ptext = f'<font size="16"><b>ROZKAZ DZIENNY NR {day_of_year}/{date.year} r.</b></font>'
elements.append(Paragraph(ptext, styles['HeaderBoldCenter']))
elements.append(Spacer(1, 12))

ptext = '<font size="12"><b>Dowódcy Jednostki Ratunkowo Gaśniczej Nr 4</b></font>'
elements.append(Paragraph(ptext, styles['HeaderBoldCenter']))
elements.append(Spacer(1, 12))

ptext = f'<font size="12">z dnia {date.day}.{date.month}.{date.year} r.</font>'
elements.append(Paragraph(ptext, styles['HeaderCenter']))
elements.append(Spacer(1, 12))

service_label = ['Dyżur domowy  Dowódcy Grupy ',
                 'Dyżurny operacyjny Rejonu',
                 'Oficer Operacyjny',
                 'Dowódca zmiany',
                 'Dyżurny PA JRG',
                 'Szef zmiany',
                 'Garażomistrz',
                 'Dowódca działań ratowniczych SGRW-N',
                 'Bosman',
                 'Podoficer dyżurny',
                 'Strażak dyżurny'
                ]

service_list = []

for label in service_label:
    list_item = ListItem(Paragraph(label, styles['Left']), value=False)
    service_list.append(list_item)

service = ListFlowable(service_list, leftIndent=37.5)
elements.append(service)

ptext = f'<font size="14">Podpisał D-ca JRG-4</font>'
elements.append(Paragraph(ptext, styles['FooterBoldRight']))

doc.build(elements)
