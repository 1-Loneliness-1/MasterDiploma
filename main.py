import sys

from PyQt6.QtWidgets import QApplication

from simple_ui import SimpleUI

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SimpleUI()
    window.show()
    sys.exit(app.exec())
