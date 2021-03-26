"""
Firefighter app

Author: Sebastian Warszawa
Website: https://github.com/wwainkrk
"""

import datetime, time
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.platypus import ListFlowable, ListItem
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER, TA_RIGHT, TA_LEFT

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping


def create_pdf():
    # Creating document
    doc = SimpleDocTemplate("firefighter_test.pdf", pagesize=letter,
                            rightMargin=20, leftMargin=20,
                            topMargin=20, bottomMargin=20)          # constructor of document with settings for margins

    # Elements on page which will be print
    doc_elements = []
    register_fonts()
    doc_styles = set_styles()
    create_header(doc_elements, doc_styles)
    create_sections(doc_elements, doc_styles)
    doc.build(doc_elements)


def register_fonts():
    # Register font and set style with new Font
    pdfmetrics.registerFont(TTFont('FreeSans', "fonts/FreeSans.ttf"))
    pdfmetrics.registerFont(TTFont('FreeSansBold', "fonts/FreeSansBold.ttf"))
    pdfmetrics.registerFont(TTFont('FreeSansItalic', "fonts/FreeSansOblique.ttf"))
    pdfmetrics.registerFont(TTFont('FreeSansBoldItalic', "fonts/FreeSansBoldOblique.ttf"))

    pdfmetrics.registerFontFamily('FreeSans', normal='FreeSans', bold='FreeSansBold', italic='FreeSansItalic', boldItalic='FreeSansBoldItalic')
    addMapping('FreeSans', 0, 0, 'FreeSans')
    addMapping('FreeSans', 0, 1, 'FreeSansItalic')
    addMapping('FreeSans', 1, 0, 'FreeSansBold')
    addMapping('FreeSans', 1, 1, 'FreeSansBoldItalic')


def set_styles():
    # Setting additional styles for document
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(name='Left', fontName='FreeSans', alignment=TA_LEFT))
    styles.add(ParagraphStyle(name='Center', fontName='FreeSans', alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='Right', fontName='FreeSans', alignment=TA_RIGHT))        # style to set paragraph on right side of page

    return styles


def create_header(elements, styles):
    date = datetime.datetime.now().date()
    ptext = f'<font size="12"><i>Kraków, dn. {date.day}.{date.month}.{date.year}</i></font>'
    elements.append(Paragraph(ptext, styles['Right']))
    elements.append(Spacer(1, 12))

    day_of_year = time.localtime().tm_yday
    ptext = f'<font size="16"><b>ROZKAZ DZIENNY NR {day_of_year}/{date.year} r.</b></font>'
    elements.append(Paragraph(ptext, styles['Center']))
    elements.append(Spacer(1, 12))

    ptext = '<font size="12"><b>Dowódcy Jednostki Ratunkowo Gaśniczej Nr 4</b></font>'
    elements.append(Paragraph(ptext, styles['Center']))
    elements.append(Spacer(1, 12))

    ptext = f'<font size="12">z dnia {date.day}.{date.month}.{date.year} r.</font>'
    elements.append(Paragraph(ptext, styles['Center']))
    elements.append(Spacer(1, 12))


def create_sections(elements, styles):
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

    counter = 1
    for label in service_label:
        list_item = ListItem(Paragraph(f"{counter}. {label}", styles['Left']), value=False)
        service_list.append(list_item)
        counter += 1

    service = ListFlowable(service_list, leftIndent=37.5)
    elements.append(service)

    ptext = f'<font size="14"><b>Podpisał D-ca JRG-4</b></font>'
    elements.append(Paragraph(ptext, styles['Right']))


create_pdf()