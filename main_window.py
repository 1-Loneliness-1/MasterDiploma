from PyQt6.QtWidgets import QMainWindow


class MainWindowUi(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Новый прием")
