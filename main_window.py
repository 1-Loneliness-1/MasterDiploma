from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QWidget
from audio_processor import AudioProcessor


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.audio_processor = AudioProcessor()
        self.audio_processor.transcription_done.connect(self.update_ui)

        central_widget = QWidget()

        self.setCentralWidget(central_widget)

        self.setObjectName("mainWindow")
        self.resize(1000, 750)
        self.setBaseSize(QtCore.QSize(1700, 650))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/main_icon32.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.setWindowIcon(icon)
        self.setAutoFillBackground(False)
        self.setLocale(QtCore.QLocale(QtCore.QLocale.Language.Russian, QtCore.QLocale.Country.Russia))

        self.bStartStopRecord = QtWidgets.QPushButton(text="начать прием", parent=central_widget)
        self.bStartStopRecord.setGeometry(QtCore.QRect(850, 610, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bStartStopRecord.setFont(font)
        self.bStartStopRecord.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.bStartStopRecord.setStyleSheet("border: 2px solid #ABABAB;\nborder-radius: 10px;\nbackground-color: #DADADA;")
        self.bStartStopRecord.setIconSize(QtCore.QSize(32, 32))
        self.bStartStopRecord.setFlat(True)
        self.bStartStopRecord.setObjectName("bStartStopRecord")
        self.bStartStopRecord.clicked.connect(self.audio_processor.start_process)

        self.bFinishRecord = QtWidgets.QPushButton(text="остановить прием", parent=central_widget)
        self.bFinishRecord.setGeometry(QtCore.QRect(820, 660, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bFinishRecord.setFont(font)
        self.bFinishRecord.setStyleSheet("border: 2px solid #ABABAB;\nborder-radius: 10px;\nbackground-color: #DADADA;")
        self.bFinishRecord.setObjectName("bFinishRecord")

        self.etSymptoms = QtWidgets.QTextEdit(parent=central_widget)
        self.etSymptoms.setGeometry(QtCore.QRect(10, 320, 381, 400))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.etSymptoms.setFont(font)
        self.etSymptoms.setStyleSheet("border: 2px solid #ABABAB;\nborder-radius: 10px;")
        self.etSymptoms.setObjectName("etSymptoms")

        self.etDiagnose = QtWidgets.QTextEdit(parent=central_widget)
        self.etDiagnose.setGeometry(QtCore.QRect(400, 320, 271, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.etDiagnose.setFont(font)
        self.etDiagnose.setStyleSheet("border: 2px solid #ABABAB;\nborder-radius: 10px;")
        self.etDiagnose.setObjectName("etDiagnose")

        self.symptomLabel = QtWidgets.QLabel(text="симптомы", parent=central_widget)
        self.symptomLabel.setGeometry(QtCore.QRect(10, 293, 104, 29))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.symptomLabel.setFont(font)
        self.symptomLabel.setStyleSheet("border-top-left-radius: 10px;\nborder-top-right-radius: 10px;\n"
                                        "border: 2px solid #ABABAB;\nmin-height: 25px;\nmin-width: 100px;\nmax-height: 25px;\nmax-width: 100px;\n"
                                        "background-color: #DADADA;\n")
        self.symptomLabel.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.symptomLabel.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.symptomLabel.setLineWidth(1)
        self.symptomLabel.setMidLineWidth(1)
        self.symptomLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.symptomLabel.setObjectName("symptomLabel")

        self.label_2 = QtWidgets.QLabel(text="диагноз", parent=central_widget)
        self.label_2.setGeometry(QtCore.QRect(400, 293, 104, 29))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(
            "border-top-left-radius: 10px;\nborder-top-right-radius: 10px;\nborder: 2px solid #ABABAB;\n"
            "min-height: 25px;\nmin-width: 100px;\nmax-height: 25px;\nmax-width: 100px;\nbackground-color: #DADADA;")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.groupBox = QtWidgets.QGroupBox(parent=central_widget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 661, 261))
        self.groupBox.setStyleSheet("background-color: #FFFFFF;\nborder-radius: 10px;\nborder: 2px solid #ABABAB;\n")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")

        self.lName = QtWidgets.QLabel(text="ФИО: Иванов Иван Иванович", parent=self.groupBox)
        self.lName.setGeometry(QtCore.QRect(10, 12, 611, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lName.setFont(font)
        self.lName.setStyleSheet("border: 0px solid #FFFFFF;\n")
        self.lName.setObjectName("lName")

        self.lAgeBirthday = QtWidgets.QLabel(text="Возраст/дата рождения: 99 лет (12.12.1212)", parent=self.groupBox)
        self.lAgeBirthday.setGeometry(QtCore.QRect(10, 40, 411, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lAgeBirthday.setFont(font)
        self.lAgeBirthday.setStyleSheet("border: 0px;")
        self.lAgeBirthday.setObjectName("lAgeBirthday")

        self.lSex = QtWidgets.QLabel(text="Пол: Мужской", parent=self.groupBox)
        self.lSex.setGeometry(QtCore.QRect(10, 70, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lSex.setFont(font)
        self.lSex.setStyleSheet("border: 0px;")
        self.lSex.setObjectName("lSex")

        self.lCardNum = QtWidgets.QLabel(text="№ карты: 12345", parent=self.groupBox)
        self.lCardNum.setGeometry(QtCore.QRect(10, 95, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lCardNum.setFont(font)
        self.lCardNum.setStyleSheet("border: 0px;")
        self.lCardNum.setObjectName("lCardNum")

        self.lPolisNum = QtWidgets.QLabel(text="№ полиса: 123-123-00", parent=self.groupBox)
        self.lPolisNum.setGeometry(QtCore.QRect(10, 122, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lPolisNum.setFont(font)
        self.lPolisNum.setStyleSheet("border: 0px;")
        self.lPolisNum.setObjectName("lPolisNum")

        self.lAllergy = QtWidgets.QLabel(text="Аллергии: пыльца, белок", parent=self.groupBox)
        self.lAllergy.setGeometry(QtCore.QRect(10, 150, 311, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lAllergy.setFont(font)
        self.lAllergy.setStyleSheet("border: 0px;\nborder-radius: 5px;\nbackground-color: #FF8282;\n"
                                    "padding-left: 2px;\n")
        self.lAllergy.setObjectName("lAllergy")

        self.lBloodType = QtWidgets.QLabel(text="Группа крови: 1(+)", parent=self.groupBox)
        self.lBloodType.setGeometry(QtCore.QRect(10, 210, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lBloodType.setFont(font)
        self.lBloodType.setStyleSheet("border: 0px;")
        self.lBloodType.setObjectName("lBloodType")

        self.lChrDiseases = QtWidgets.QLabel(text="Хрон. болезни: Гипертония", parent=self.groupBox)
        self.lChrDiseases.setGeometry(QtCore.QRect(10, 180, 311, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lChrDiseases.setFont(font)
        self.lChrDiseases.setStyleSheet("border: 0px;")
        self.lChrDiseases.setObjectName("lChrDiseases")

        self.etDrugs = QtWidgets.QTextEdit(parent=central_widget)
        self.etDrugs.setGeometry(QtCore.QRect(400, 480, 271, 231))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.etDrugs.setFont(font)
        self.etDrugs.setStyleSheet("border: 2px solid #ABABAB;\nborder-radius: 10px;")
        self.etDrugs.setObjectName("etDrugs")

        self.label_7 = QtWidgets.QLabel(text="лекарства", parent=central_widget)
        self.label_7.setGeometry(QtCore.QRect(400, 453, 104, 29))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border-top-left-radius: 10px;\nborder-top-right-radius: 10px;\n"
                                   "border: 2px solid #ABABAB;\nmin-height: 25px;\nmin-width: 100px;\n"
                                   "max-height: 25px;\nmax-width: 100px;\nbackground-color: #DADADA;")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")

        self.lResDrugs = QtWidgets.QLabel(parent=central_widget)
        self.lResDrugs.setGeometry(QtCore.QRect(690, 46, 281, 225))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lResDrugs.setFont(font)
        self.lResDrugs.setStyleSheet("border: 2px solid #ABABAB;\nborder-top-right-radius: 10px;\n"
                                     "border-bottom-left-radius: 10px;\nborder-bottom-right-radius: 10px;\n"
                                     "background-color: #FFFFFF;")
        self.lResDrugs.setText("")
        self.lResDrugs.setObjectName("lResDrugs")

        self.lResMed = QtWidgets.QLabel(text="назнач. лекарства", parent=central_widget)
        self.lResMed.setGeometry(QtCore.QRect(690, 19, 174, 29))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lResMed.setFont(font)
        self.lResMed.setStyleSheet("border-top-left-radius: 10px;\nborder-top-right-radius: 10px;\n"
                                   "border: 2px solid #ABABAB;\nmin-height: 25px;\nmin-width: 170px;\n"
                                   "max-height: 25px;\nmax-width: 170px;\nbackground-color: #DADADA;")
        self.lResMed.setObjectName("lResMed")

        self.bTransfToPdf = QtWidgets.QPushButton(text="экспорт в PDF", parent=central_widget)
        self.bTransfToPdf.setGeometry(QtCore.QRect(890, 570, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bTransfToPdf.setFont(font)
        self.bTransfToPdf.setStyleSheet("border: 2px solid #FD9396;\nborder-radius: 10px;\nbackground-color: #FEC2C4;")
        self.bTransfToPdf.setObjectName("bTransfToPdf")

        self.etNotes = QtWidgets.QTextEdit(parent=central_widget)
        self.etNotes.setGeometry(QtCore.QRect(690, 320, 281, 221))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.etNotes.setFont(font)
        self.etNotes.setStyleSheet("background-color: #FFFFAE;\nborder: 2px solid #FFFFAE;\nborder-radius: 10px;\n"
                                   "padding-top: 20px;\npadding-left: 5px;")
        self.etNotes.setObjectName("etNotes")

        self.lNotes = QtWidgets.QLabel(text="Заметки", parent=central_widget)
        self.lNotes.setGeometry(QtCore.QRect(690, 325, 281, 16))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setUnderline(False)
        self.lNotes.setFont(font)
        self.lNotes.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lNotes.setObjectName("lNotes")

        self.recognIndicator = QtWidgets.QPushButton(parent=central_widget)
        self.recognIndicator.setEnabled(False)
        self.recognIndicator.setGeometry(QtCore.QRect(820, 622, 21, 21))
        self.recognIndicator.setStyleSheet("border-radius: 10px;\nbackground-color: #00FF00;\nborder: 2px solid #ABABAB;")
        self.recognIndicator.setText("")
        self.recognIndicator.setObjectName("recognIndicator")

        self.show()

    def update_ui(self, transcribed_text):
        self.etSymptoms.append(transcribed_text)