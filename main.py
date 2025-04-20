from PyQt6.QtWidgets import QApplication, QWidget
import sys

from main_window import UiMainWindow

if __name__=='__main__':
    app = QApplication(sys.argv)

    window = UiMainWindow()
    window.show()

    app.exec()