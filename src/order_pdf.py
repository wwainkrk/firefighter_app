"""
Firefighter app

Author: Sebastian Warszawa
Website: https://github.com/wwainkrk
"""

import datetime, time
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.platypus import ListFlowable, ListItem
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER, TA_RIGHT, TA_LEFT, TA_JUSTIFY

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
        self.doc = SimpleDocTemplate("firefighter_test.pdf", pagesize=letter,
                                rightMargin=20, leftMargin=20,
                                topMargin=20, bottomMargin=20)          # constructor of document with settings for margins

        self.create_header()
        self.create_paragraphs()
        self.create_footer()
        # self.create_sections()
        self.doc.build(self.doc_elements)

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
        styles.add(ParagraphStyle(name='Justify', fontName='FreeSans', alignment=TA_JUSTIFY))

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
        # Main paragraphs, main points of documents for loop
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

        # New style for paragraph - bold text directly in content
        style = self.doc_styles['Paragraph']
        style.leading = 24                      # Space after paragraph line

        counter = 1                             # Number of paragraph
        for label in paragraphs_label:
            list_item = Paragraph(f"<b>{counter}. {label}</b>", style)
            self.doc_elements.append(list_item)
            self.paragraph_switch(counter)
            counter += 1

    def create_footer(self):
        ptext = f'<font size="14"><b>Podpisał D-ca JRG-4</b></font>'
        self.doc_elements.append(Paragraph(ptext, self.doc_styles['Right']))

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

    def trucks_crew(self):
        # style = self.doc_styles["Justify"]
        # style.leftIndent = 35
        # style.rightIndent = 35
        # ptext = f"<b>GBARt 2,5/25 GCBA 5/24 ………………………</b>"
        # trucks = Paragraph(ptext, style)
        # trucks.width = self.doc.width
        # trucks.style.alignment = TA_JUSTIFY
        # print(trucks.width)
        data = [['GBARt 2,5/25', 'GCBA 5/24', '………………………']]
        table_width = (self.doc.width - self.doc.leftMargin - self.doc.rightMargin) / 3
        t = Table(data, table_width)

        self.doc_elements.append(t)

    def oxygen_apparatuses(self):
        data = [
            ['GBARt 2,5/25', '1. .................', '2. ........................'],
            ['GCBA 5/24', '1. .................', '2. ........................']
        ]

        t = Table(data)

        self.doc_elements.append(t)

    def divers(self):
        data = [
            ['1. .................', '2. ........................', '3. .........................'],
            ['4. .................', '5. ........................', '6. .........................']
        ]

        t = Table(data)

        self.doc_elements.append(t)

    def medical_lifeguards(self):
        # Function for ligfeguards section, only two places for lifeguards

        data = [
            ['1. .................', '2. ........................']
        ]

        t = Table(data)

        self.doc_elements.append(t)

    def activities(self):
        # Function for activities in a day, e.g. Physical Education, workshops.

        data = [
            ['1. ........................'],
            ['2. ........................'],
            ['3. ........................'],
            ['4. ........................'],
            ['5. ........................'],
            ['6. ........................']
        ]

        t = Table(data)

        self.doc_elements.append(t)

    def off_work(self):
        # Function for section with firefighters on holidays or different days off

        ptext = f'<font size="14"><b>Urlopy</b></font>'
        holidays = Paragraph(ptext, style=self.doc_styles['Left'])

        self.doc_elements.append(holidays)

        data = [
            ['1. .................', '2. ........................', '3. .........................'],
            ['4. .................', '5. ........................', '6. .........................']
        ]

        t = Table(data)

        self.doc_elements.append(t)

        ptext = f'<font size="14"><b>Czas wolny</b></font>'
        freetime = Paragraph(ptext, style=self.doc_styles['Left'])

        self.doc_elements.append(freetime)

        data = [
            ['1. .................', '2. ........................', '3. .........................'],
            ['4. .................', '5. ........................', '6. .........................'],
            ['7. .................', '8. ........................', '9. .........................']
        ]

        t = Table(data)

        self.doc_elements.append(t)

    def home_duty(self):
        # Function foe section with firefighter, which are on home duty and which they could arrive on phone call

        data = [
            ['1. .................', '2. ........................', '3. .........................'],
            ['4. .................', '5. ........................', '6. .........................'],
            ['7. .................', '8. ........................', '9. .........................']
        ]

        t = Table(data)

        self.doc_elements.append(t)

    def comments(self):
        data = [
            ['.................']
        ]

        t = Table(data)

        self.doc_elements.append(t)

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
