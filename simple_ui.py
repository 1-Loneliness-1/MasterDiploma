from typing import Dict

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
        self.audio_processor.entities_recognition_done.connect(self.parse_entities)

        self.setWindowTitle("Новый прием")
        self.setFixedSize(1200, 750)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/main_icon32.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.setWindowIcon(icon)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_horizontal_layout = QHBoxLayout()
        central_widget.setLayout(main_horizontal_layout)

        # Блок формирования первой колонки интерфейса
        first_column_layout = QVBoxLayout()
        main_horizontal_layout.addLayout(first_column_layout, stretch=4)

        self.gbPatientInfo = QGroupBox()
        self.gbPatientInfo.setGeometry(QtCore.QRect(10, 10, 661, 261))
        self.gbPatientInfo.setStyleSheet("background-color: #676767;\nborder-radius: 10px;\nborder: 2px solid #ABABAB;\n")
        self.gbPatientInfo.setTitle("")
        first_column_layout.addWidget(self.gbPatientInfo, stretch=1)

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
        first_column_layout.addLayout(first_column_bottom_h_layout, stretch=2)

        symptoms_and_procedures_layout = QVBoxLayout()
        symptoms_and_procedures_layout.setSpacing(0)
        first_column_bottom_h_layout.addLayout(symptoms_and_procedures_layout)

        self.lSymptoms = QLabel(text="симптомы")
        self.lSymptoms.setGeometry(QtCore.QRect(10, 293, 104, 29))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.lSymptoms.setFont(font)
        self.lSymptoms.setStyleSheet("border-top-left-radius: 10px;\nborder-top-right-radius: 10px;\n"
                                        "border: 2px solid #ABABAB;\nmin-height: 25px;\nmin-width: 100px;\nmax-height: 25px;\nmax-width: 100px;\n"
                                        "background-color: #9B9B9B;\nmargin-top: 10px;")
        self.lSymptoms.setFrameShape(QFrame.Shape.NoFrame)
        self.lSymptoms.setFrameShadow(QFrame.Shadow.Plain)
        self.lSymptoms.setLineWidth(1)
        self.lSymptoms.setMidLineWidth(1)
        self.lSymptoms.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        symptoms_and_procedures_layout.addWidget(self.lSymptoms)

        self.etSymptoms = QTextEdit()
        self.etSymptoms.setPlaceholderText("Начинайте записывать симптомы...")
        self.etSymptoms.setGeometry(QtCore.QRect(10, 320, 381, 400))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.etSymptoms.setFont(font)
        self.etSymptoms.setStyleSheet("border: 2px solid #ABABAB;\nborder-top-right-radius: 10px;"
                                      "border-bottom-left-radius: 10px; border-bottom-right-radius: 10px;"
                                      "margin-right: 10px; margin-bottom: 10px;")
        symptoms_and_procedures_layout.addWidget(self.etSymptoms)

        self.lProcedures = QLabel(text="процедуры")
        self.lProcedures.setGeometry(QtCore.QRect(10, 293, 104, 29))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.lProcedures.setFont(font)
        self.lProcedures.setStyleSheet("border-top-left-radius: 10px;\nborder-top-right-radius: 10px;\n"
                                        "border: 2px solid #ABABAB;\nmin-height: 25px;\nmin-width: 100px;\nmax-height: 25px;\nmax-width: 100px;\n"
                                        "background-color: #9B9B9B;\nmargin-top: 10px;")
        self.lProcedures.setFrameShape(QFrame.Shape.NoFrame)
        self.lProcedures.setFrameShadow(QFrame.Shadow.Plain)
        self.lProcedures.setLineWidth(1)
        self.lProcedures.setMidLineWidth(1)
        self.lProcedures.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        symptoms_and_procedures_layout.addWidget(self.lProcedures)

        self.etProcedures = QTextEdit()
        self.etProcedures.setPlaceholderText("Здесь будут направления на сдачу анализов...")
        self.etProcedures.setGeometry(QtCore.QRect(10, 320, 381, 400))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.etProcedures.setFont(font)
        self.etProcedures.setStyleSheet("border: 2px solid #ABABAB;\nborder-top-right-radius: 10px;"
                                      "border-bottom-left-radius: 10px; border-bottom-right-radius: 10px;"
                                      "margin-right: 10px; margin-bottom: 10px;")
        symptoms_and_procedures_layout.addWidget(self.etProcedures)

        # Формирование столбца с полями "Диагноз" и "лекарства"
        diagnosis_and_drugs_layout = QVBoxLayout()
        diagnosis_and_drugs_layout.setSpacing(0)
        first_column_bottom_h_layout.addLayout(diagnosis_and_drugs_layout)

        self.lDiagnose = QLabel(text="диагноз")
        self.lDiagnose.setGeometry(QtCore.QRect(400, 293, 104, 29))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lDiagnose.setFont(font)
        self.lDiagnose.setStyleSheet(
            "border-top-left-radius: 10px;\nborder-top-right-radius: 10px;\nborder: 2px solid #ABABAB;\n"
            "min-height: 25px;\nmin-width: 100px;\nmax-height: 25px;\nmax-width: 100px;\nbackground-color: #9B9B9B;"
            "margin-top: 10px;")
        self.lDiagnose.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        diagnosis_and_drugs_layout.addWidget(self.lDiagnose)

        self.etDiagnose = QTextEdit()
        self.etDiagnose.setPlaceholderText("Введите диагноз...")
        self.etDiagnose.setGeometry(QtCore.QRect(400, 320, 271, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.etDiagnose.setFont(font)
        self.etDiagnose.setStyleSheet("border: 2px solid #ABABAB;\nborder-top-right-radius: 10px;"
                                      "border-bottom-left-radius: 10px; border-bottom-right-radius: 10px;"
                                      "margin-bottom: 20px;")
        diagnosis_and_drugs_layout.addWidget(self.etDiagnose)

        self.lCurrentDrugs = QLabel(text="лекарства")
        self.lCurrentDrugs.setGeometry(QtCore.QRect(400, 453, 104, 29))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lCurrentDrugs.setFont(font)
        self.lCurrentDrugs.setStyleSheet("border-top-left-radius: 10px;\nborder-top-right-radius: 10px;\n"
                                   "border: 2px solid #ABABAB;\nmin-height: 25px;\nmin-width: 100px;\n"
                                   "max-height: 25px;\nmax-width: 100px;\nbackground-color: #9B9B9B;")
        self.lCurrentDrugs.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        diagnosis_and_drugs_layout.addWidget(self.lCurrentDrugs)

        self.etDrugs = QTextEdit()
        self.etDrugs.setPlaceholderText("Введите назначаемые лекарства...")
        self.etDrugs.setGeometry(QtCore.QRect(400, 480, 271, 231))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.etDrugs.setFont(font)
        self.etDrugs.setStyleSheet("border: 2px solid #ABABAB;\nmargin-bottom: 10px;"
                                   "border-top-right-radius: 10px; border-bottom-left-radius: 10px;"
                                   "border-bottom-right-radius: 10px;")
        diagnosis_and_drugs_layout.addWidget(self.etDrugs)

        # Формирование второй колонки главной разметки
        second_column_layout = QVBoxLayout()
        second_column_layout.setSpacing(0)
        main_horizontal_layout.addLayout(second_column_layout, stretch=1)

        self.lResDrugText = QLabel(text="назнач. лекарства")
        self.lResDrugText.setGeometry(QtCore.QRect(690, 19, 174, 29))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lResDrugText.setFont(font)
        self.lResDrugText.setStyleSheet("border-top-left-radius: 10px;\nborder-top-right-radius: 10px;\n"
                                   "border: 2px solid #ABABAB;\nmin-height: 25px;\nmin-width: 170px;\n"
                                   "max-height: 25px;\nmax-width: 170px;\nbackground-color: #9B9B9B; margin-left: 10px;")
        second_column_layout.addWidget(self.lResDrugText)

        self.lResDrugBody = QLabel()
        self.lResDrugBody.setGeometry(QtCore.QRect(690, 46, 281, 225))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lResDrugBody.setFont(font)
        self.lResDrugBody.setStyleSheet("border: 2px solid #787878;\nborder-top-right-radius: 10px;\n"
                                     "border-bottom-left-radius: 10px;\nborder-bottom-right-radius: 10px;\n"
                                     "background-color: #2D2D2D; width: 281px; height: 225px; margin-left: 10px;")
        self.lResDrugBody.setText("")
        second_column_layout.addWidget(self.lResDrugBody, stretch=1)

        notes_layout = QVBoxLayout()
        notes_layout.setSpacing(0)
        second_column_layout.addLayout(notes_layout, stretch=1)

        self.lNotes = QLabel(text="Заметки")
        self.lNotes.setGeometry(QtCore.QRect(690, 325, 281, 16))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setUnderline(False)
        self.lNotes.setFont(font)
        self.lNotes.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lNotes.setStyleSheet("color: black; background-color: #FFFFAE; margin-left: 10px;"
                                  "margin-top: 15px; border-top-left-radius: 10px; border-top-right-radius: 10px;")
        notes_layout.addWidget(self.lNotes)

        self.etNotes = QTextEdit()
        self.etNotes.setGeometry(QtCore.QRect(690, 320, 281, 221))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.etNotes.setFont(font)
        self.etNotes.setStyleSheet("background-color: #FFFFAE;\nborder: 2px solid #FFFFAE;\nborder-bottom-left-radius: 10px;\n"
                                   "color: #000000; border-bottom-right-radius: 10px; padding-left: 5px; margin-left: 10px;")
        notes_layout.addWidget(self.etNotes)

        self.bExportToPdf = QPushButton(text="экспорт в PDF")
        self.bExportToPdf.setGeometry(QtCore.QRect(890, 570, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bExportToPdf.setFont(font)
        self.bExportToPdf.setStyleSheet("border: 2px solid #787878;\nborder-radius: 10px;\nbackground-color: #9B9B9B;\n"
                                        "margin-left: 300px; margin-top: 55px; width: 101px; height: 31px;")
        second_column_layout.addWidget(self.bExportToPdf)

        # Формирование разметки для кнопки начала приема и индикатора
        start_reception_and_indicator_layout = QHBoxLayout()
        second_column_layout.addLayout(start_reception_and_indicator_layout)

        self.recognitionIndicator = QPushButton()
        self.recognitionIndicator.setEnabled(False)
        self.recognitionIndicator.setGeometry(QtCore.QRect(820, 622, 21, 21))
        self.recognitionIndicator.setStyleSheet("border-radius: 10px;\nbackground-color: #00FF00;\nborder: 2px solid #000000;\n"
                                                "margin-left: 252px; margin-top: 12px; width: 21px; height: 21px;")
        self.recognitionIndicator.setText("")
        start_reception_and_indicator_layout.addWidget(self.recognitionIndicator)

        self.bStartStopReception = QPushButton(text="начать прием")
        self.bStartStopReception.setGeometry(QtCore.QRect(850, 610, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bStartStopReception.setFont(font)
        self.bStartStopReception.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.bStartStopReception.setStyleSheet("border: 2px solid #692FFF;\nborder-radius: 10px;\nbackground-color: #7945FF;\n"
                                               "width: 141px; height: 41px; margin-left: 4px; margin-top: 10px;")
        self.bStartStopReception.setIconSize(QtCore.QSize(32, 32))
        self.bStartStopReception.setFlat(True)
        self.bStartStopReception.clicked.connect(self.audio_processor.start_process)
        start_reception_and_indicator_layout.addWidget(self.bStartStopReception)

        self.bFinishReception = QPushButton(text="завершить прием")
        self.bFinishReception.setGeometry(QtCore.QRect(820, 660, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bFinishReception.setFont(font)
        self.bFinishReception.setStyleSheet("border: 2px solid #CD5656;\nborder-radius: 10px;\n"
                                            "background-color: #C53C3C;\nwidth: 171px;\nheight: 41px;\n"
                                            "margin-left: 250px; margin-top: 10px;")
        second_column_layout.addWidget(self.bFinishReception)

    def parse_entities(self, entities_dictionary: Dict):
        for ent_obj in entities_dictionary["entities"]["Drugclass"]:
            self.etDrugs.append("-" + ent_obj["text"] + "\n")

        for ent_obj in entities_dictionary["entities"]["Drugname"]:
            self.etDrugs.append("-" + ent_obj["text"] + "\n")

        for ent_obj in entities_dictionary["entities"]["Finding"]:
            self.etSymptoms.append("-" + ent_obj["text"] + "\n")
