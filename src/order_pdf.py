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


class OrderPDF:
    # Constructor of elements to print, necessary styles, and registration of fonts
    def __init__(self):
        self.doc_elements = []
        self.register_fonts()
        self.doc_styles = self.set_styles()

    def create_pdf(self):
        # Creating document
        doc = SimpleDocTemplate("firefighter_test.pdf", pagesize=letter,
                                rightMargin=20, leftMargin=20,
                                topMargin=20, bottomMargin=20)          # constructor of document with settings for margins

        self.create_header()
        self.create_paragraphs()
        self.create_sections()
        doc.build(self.doc_elements)

    def register_fonts(self):
        # Register font and set style with new Font
        pdfmetrics.registerFont(TTFont('FreeSans', "fonts/FreeSans.ttf"))
        pdfmetrics.registerFont(TTFont('FreeSansBold', "fonts/FreeSansBold.ttf"))
        pdfmetrics.registerFont(TTFont('FreeSansItalic', "fonts/FreeSansOblique.ttf"))
        pdfmetrics.registerFont(TTFont('FreeSansBoldItalic', "fonts/FreeSansBoldOblique.ttf"))

        pdfmetrics.registerFontFamily('FreeSans', normal='FreeSans', bold='FreeSansBold', italic='FreeSansItalic',
                                      boldItalic='FreeSansBoldItalic')
        addMapping('FreeSans', 0, 0, 'FreeSans')
        addMapping('FreeSans', 0, 1, 'FreeSansItalic')
        addMapping('FreeSans', 1, 0, 'FreeSansBold')
        addMapping('FreeSans', 1, 1, 'FreeSansBoldItalic')

    def set_styles(self):
        # Setting additional styles for document
        styles = getSampleStyleSheet()

        # style to set paragraph on right side of page
        styles.add(ParagraphStyle(name='Left', fontName='FreeSans', alignment=TA_LEFT))
        styles.add(ParagraphStyle(name='Center', fontName='FreeSans', alignment=TA_CENTER))
        styles.add(ParagraphStyle(name='Right', fontName='FreeSans', alignment=TA_RIGHT))

        styles.add(ParagraphStyle(name='Paragraph', fontName='FreeSans', fontSize=14))

        return styles

    def create_header(self):
        date = datetime.datetime.now().date()
        ptext = f'<font size="12"><i>Kraków, dn. {date.day}.{date.month}.{date.year}</i></font>'
        self.doc_elements.append(Paragraph(ptext, self.doc_styles['Right']))
        self.doc_elements.append(Spacer(1, 12))

        day_of_year = time.localtime().tm_yday
        ptext = f'<font size="16"><b>ROZKAZ DZIENNY NR {day_of_year}/{date.year} r.</b></font>'
        self.doc_elements.append(Paragraph(ptext, self.doc_styles['Center']))
        self.doc_elements.append(Spacer(1, 12))

        ptext = '<font size="12"><b>Dowódcy Jednostki Ratunkowo Gaśniczej Nr 4</b></font>'
        self.doc_elements.append(Paragraph(ptext, self.doc_styles['Center']))
        self.doc_elements.append(Spacer(1, 12))

        ptext = f'<font size="12">z dnia {date.day}.{date.month}.{date.year} r.</font>'
        self.doc_elements.append(Paragraph(ptext, self.doc_styles['Center']))
        self.doc_elements.append(Spacer(1, 12))

    def create_paragraphs(self):
        paragraphs_label = [
            'SŁUŻBA',
            'PODZIAŁ BOJOWY',
            'PRACA W APARATACH POWIETRZNYCH (z łącznością podhełmową)',
            'DYŻURNI NURKOWIE',
            'DYŻURNI RATOWNICY MEDYCZNI PSP',
            'ZAJĘCIA',
            'WOLNE',
            'DYŻUR DOMOWY',
            'UWAGI'
        ]

        paragraphs_list = []

        style = self.doc_styles['Paragraph']
        style.leading = 24

        counter = 1
        for label in paragraphs_label:
            list_item = ListItem(Paragraph(f"<b>{counter}. {label}</b>", style), value=False)
            paragraphs_list.append(list_item)
            self.paragraph_switch(counter)
            counter += 1

        paragraphs = ListFlowable(paragraphs_list)

        self.doc_elements.append(paragraphs)

    def create_sections(self):
        service_label = [
            'Dyżur domowy  Dowódcy Grupy ',
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

        service_list = ListFlowable(
            [ListItem(Paragraph(service, self.doc_styles['Left']), leftIndent=35, bulletColor='black') for
             service in service_label],
            bulletType='bullet',
            start='-'
        )

        self.doc_elements.append(service_list)

        ptext = f'<font size="14"><b>Podpisał D-ca JRG-4</b></font>'
        self.doc_elements.append(Paragraph(ptext, self.doc_styles['Right']))

    def trucks_crew(self):
        print(2)

    def oxygen_apparatuses(self):
        print(3)

    def divers(self):
        print(4)

    def medical_lifeguards(self):
        print(5)

    def activities(self):
        print(6)

    def off_work(self):
        print(7)

    def home_duty(self):
        print(8)

    def comments(self):
        print(9)

    def paragraph_switch(self, arg):
        switcher = {
            1: self.create_sections,
            2: self.trucks_crew,
            3: self.oxygen_apparatuses,
            4: self.divers,
            5: self.medical_lifeguards,
            6: self.activities,
            7: self.off_work,
            8: self.home_duty,
            9: self.comments
        }

        func = switcher.get(arg, lambda: "Invalid month")

        func()


pdf = OrderPDF()
pdf.create_pdf()
