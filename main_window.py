from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QPushButton


class MainWindowUi(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Новый прием")
        self.setWindowIcon(QIcon("icons/main_icon32.ico"))
        self.setFixedSize(QSize(1465, 750))

        start_stop_rec_button = QPushButton(QIcon("icons/start_rec.ico"), "", self)
        start_stop_rec_button.move(10, 10)