from PyQt6.QtWidgets import QApplication
from PyQt6 import uic
import sys


if __name__=='__main__':
    app = QApplication(sys.argv)

    window = uic.loadUi("main_window.ui")
    window.show()

    app.exec()