from PyQt6.QtWidgets import QApplication
from main_window import MainWindowUi
import sys


if __name__=='__main__':
    app = QApplication(sys.argv)

    window = MainWindowUi()
    window.show()

    app.exec()