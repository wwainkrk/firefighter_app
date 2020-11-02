"""
Firefighter app

Author: Sebastian Warszawa
Website: https://github.com/wwainkrk
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox
from PyQt5.QtGui import QIcon

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class LoginForm(QWidget):
    """
    Constructor for Login Form, with necessary widgets with fields
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Okno logowania')
        self.setWindowIcon(QIcon("icons/firefighter.svg"))                  # the same icon as in main window
        self.resize(500, 150)

        layout = QGridLayout()

        # Username
        self.label_username = QLabel('<font size="4"> Nazwa użytkownika: </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Podaj nazwę użytkownika')
        layout.addWidget(self.label_username, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)

        # Password
        self.label_password = QLabel('<font size="4"> Hasło: </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('Podaj hasło')
        layout.addWidget(self.label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        self.button_login = QPushButton('Zaloguj')
        #self.button_login.clicked.connect()


class Firefighter(QWidget):

    def __init__(self):
        super().__init__()                          # Constructor from QWidget class

        self.init_UI()                               # Settings for our app

    def init_UI(self):

        self.setGeometry(300, 300, 300, 220)
        self.setWindowIcon(QIcon("icons/firefighter.svg"))
        self.setWindowTitle('Firefighter Order')

        self.show()


def db_connection():
    # We will create engine, session and mapper for SQLite database

    engine = create_engine('sqlite:///database\\JRG.db', echo=True)
    base = declarative_base()

    session = sessionmaker(bind=engine)
    session.configure(bind=engine)

    return session


def main():

    session = db_connection()
    app = QApplication(sys.argv)
    main_window = Firefighter()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()