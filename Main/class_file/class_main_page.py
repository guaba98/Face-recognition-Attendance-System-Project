from UI.MainWidget import Ui_MainWidget
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QCursor, QPixmap
import sys

class MainPage(QWidget, Ui_MainWidget):
    def __init__(self, controller):
        super().__init__()

        self.setupUi(self)
        self.setCursor(QCursor(QPixmap('../img/icon/cursor_1.png').scaled(50, 50)))
