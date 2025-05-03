from PyQt6 import QtGui, QtCore
from PyQt6.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QTextEdit,
    QLabel, QGroupBox, QHBoxLayout, QFrame
)
from audio_processor import AudioProcessor


class SimpleUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.audio_processor = AudioProcessor()
        # self.audio_processor.transcription_done.connect(self.on_transcription_done)

        self.setWindowTitle("Новый прием")
        self.setFixedSize(1000, 750)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/main_icon32.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.setWindowIcon(icon)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_horizontal_layout = QHBoxLayout()
        central_widget.setLayout(main_horizontal_layout)

        # Блок формирования первой колонки интерфейса
        first_column_layout = QVBoxLayout()
        main_horizontal_layout.addLayout(first_column_layout)

        self.gbPatientInfo = QGroupBox()
        self.gbPatientInfo.setGeometry(QtCore.QRect(10, 10, 661, 261))
        self.gbPatientInfo.setStyleSheet("background-color: #676767;\nborder-radius: 10px;\nborder: 2px solid #ABABAB;\n")
        self.gbPatientInfo.setTitle("")
        first_column_layout.addWidget(self.gbPatientInfo)

        self.lName = QLabel(text="ФИО: Иванов Иван Иванович", parent=self.gbPatientInfo)
        self.lName.setGeometry(QtCore.QRect(10, 12, 611, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lName.setFont(font)
        self.lName.setStyleSheet("border: 0px solid #FFFFFF;\n")

        self.lAgeBirthday = QLabel(text="Возраст/дата рождения: 99 лет (12.12.1212)", parent=self.gbPatientInfo)
        self.lAgeBirthday.setGeometry(QtCore.QRect(10, 40, 411, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lAgeBirthday.setFont(font)
        self.lAgeBirthday.setStyleSheet("border: 0px;")

        self.lSex = QLabel(text="Пол: Мужской", parent=self.gbPatientInfo)
        self.lSex.setGeometry(QtCore.QRect(10, 70, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lSex.setFont(font)
        self.lSex.setStyleSheet("border: 0px;")

        self.lCardNum = QLabel(text="№ карты: 12345", parent=self.gbPatientInfo)
        self.lCardNum.setGeometry(QtCore.QRect(10, 95, 211, 20))
        self.lCardNum.setFont(font)
        self.lCardNum.setStyleSheet("border: 0px;")

        self.lPolisNum = QLabel(text="№ полиса: 123-123-00", parent=self.gbPatientInfo)
        self.lPolisNum.setGeometry(QtCore.QRect(10, 122, 191, 20))
        self.lPolisNum.setFont(font)
        self.lPolisNum.setStyleSheet("border: 0px;")

        self.lAllergy = QLabel(text="Аллергии: пыльца, белок", parent=self.gbPatientInfo)
        self.lAllergy.setGeometry(QtCore.QRect(10, 150, 311, 22))
        self.lAllergy.setFont(font)
        self.lAllergy.setStyleSheet("border: 0px;\nborder-radius: 5px;\nbackground-color: #FF8282;\n"
                                    "padding-left: 2px;\n")

        self.lBloodType = QLabel(text="Группа крови: 1(+)", parent=self.gbPatientInfo)
        self.lBloodType.setGeometry(QtCore.QRect(10, 210, 151, 20))
        self.lBloodType.setFont(font)
        self.lBloodType.setStyleSheet("border: 0px;")

        self.lChrDiseases = QLabel(text="Хрон. болезни: Гипертония", parent=self.gbPatientInfo)
        self.lChrDiseases.setGeometry(QtCore.QRect(10, 180, 311, 20))
        self.lChrDiseases.setFont(font)
        self.lChrDiseases.setStyleSheet("border: 0px;")

        # Формирование интерфейса нижнего блока первого столбца
        first_column_bottom_h_layout = QHBoxLayout()
        first_column_layout.addLayout(first_column_bottom_h_layout)

        symptoms_layout = QVBoxLayout()
        first_column_bottom_h_layout.addLayout(symptoms_layout)

        self.lSymptoms = QLabel(text="симптомы")
        self.lSymptoms.setGeometry(QtCore.QRect(10, 293, 104, 29))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.lSymptoms.setFont(font)
        self.lSymptoms.setStyleSheet("border-top-left-radius: 10px;\nborder-top-right-radius: 10px;\n"
                                        "border: 2px solid #ABABAB;\nmin-height: 25px;\nmin-width: 100px;\nmax-height: 25px;\nmax-width: 100px;\n"
                                        "background-color: #DADADA;\n")
        self.lSymptoms.setFrameShape(QFrame.Shape.NoFrame)
        self.lSymptoms.setFrameShadow(QFrame.Shadow.Plain)
        self.lSymptoms.setLineWidth(1)
        self.lSymptoms.setMidLineWidth(1)
        self.lSymptoms.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        symptoms_layout.addWidget(self.lSymptoms)

        self.etSymptoms = QTextEdit()
        self.etSymptoms.setPlaceholderText("Начинайте записывать симптомы...")
        self.etSymptoms.setGeometry(QtCore.QRect(10, 320, 381, 400))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.etSymptoms.setFont(font)
        self.etSymptoms.setStyleSheet("border: 2px solid #ABABAB;\nborder-radius: 10px;")
        symptoms_layout.addWidget(self.etSymptoms)

        # Формирование столбца с полями "Диагноз" и "лекарства"
        diagnosis_and_drugs_layout = QVBoxLayout()
        first_column_bottom_h_layout.addLayout(diagnosis_and_drugs_layout)

        self.lDiagnose = QLabel(text="диагноз")
        self.lDiagnose.setGeometry(QtCore.QRect(400, 293, 104, 29))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lDiagnose.setFont(font)
        self.lDiagnose.setStyleSheet(
            "border-top-left-radius: 10px;\nborder-top-right-radius: 10px;\nborder: 2px solid #ABABAB;\n"
            "min-height: 25px;\nmin-width: 100px;\nmax-height: 25px;\nmax-width: 100px;\nbackground-color: #DADADA;")
        self.lDiagnose.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        diagnosis_and_drugs_layout.addWidget(self.lDiagnose)

        self.etDiagnose = QTextEdit()
        self.etDiagnose.setPlaceholderText("Введите диагноз...")
        self.etDiagnose.setGeometry(QtCore.QRect(400, 320, 271, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.etDiagnose.setFont(font)
        self.etDiagnose.setStyleSheet("border: 2px solid #ABABAB;\nborder-radius: 10px;")
        diagnosis_and_drugs_layout.addWidget(self.etDiagnose)

        self.lCurrentDrugs = QLabel(text="лекарства")
        self.lCurrentDrugs.setGeometry(QtCore.QRect(400, 453, 104, 29))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lCurrentDrugs.setFont(font)
        self.lCurrentDrugs.setStyleSheet("border-top-left-radius: 10px;\nborder-top-right-radius: 10px;\n"
                                   "border: 2px solid #ABABAB;\nmin-height: 25px;\nmin-width: 100px;\n"
                                   "max-height: 25px;\nmax-width: 100px;\nbackground-color: #DADADA;")
        self.lCurrentDrugs.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        diagnosis_and_drugs_layout.addWidget(self.lCurrentDrugs)

        self.etDrugs = QTextEdit()
        self.etDrugs.setPlaceholderText("Введите назначаемые лекарства...")
        self.etDrugs.setGeometry(QtCore.QRect(400, 480, 271, 231))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.etDrugs.setFont(font)
        self.etDrugs.setStyleSheet("border: 2px solid #ABABAB;\nborder-radius: 10px;")
        diagnosis_and_drugs_layout.addWidget(self.etDrugs)

        # Формирование второй колонки главной разметки
        second_column_layout = QVBoxLayout()
        main_horizontal_layout.addLayout(second_column_layout)

        self.lResDrugText = QLabel(text="назнач. лекарства")
        self.lResDrugText.setGeometry(QtCore.QRect(690, 19, 174, 29))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lResDrugText.setFont(font)
        self.lResDrugText.setStyleSheet("border-top-left-radius: 10px;\nborder-top-right-radius: 10px;\n"
                                   "border: 2px solid #ABABAB;\nmin-height: 25px;\nmin-width: 170px;\n"
                                   "max-height: 25px;\nmax-width: 170px;\nbackground-color: #DADADA;")
        second_column_layout.addWidget(self.lResDrugText)

        self.lResDrugBody = QLabel()
        self.lResDrugBody.setGeometry(QtCore.QRect(690, 46, 281, 225))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lResDrugBody.setFont(font)
        self.lResDrugBody.setStyleSheet("border: 2px solid #ABABAB;\nborder-top-right-radius: 10px;\n"
                                     "border-bottom-left-radius: 10px;\nborder-bottom-right-radius: 10px;\n"
                                     "background-color: #FFFFFF;")
        self.lResDrugBody.setText("")
        second_column_layout.addWidget(self.lResDrugBody)


