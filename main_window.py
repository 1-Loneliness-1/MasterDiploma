from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):

        def __init__(self):
            super().__init__()
            self.ui = Ui_mainWindow()
            self.ui.setupUi(self)
            self.show()


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1000, 750)
        mainWindow.setBaseSize(QtCore.QSize(1700, 650))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/main_icon32.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setAutoFillBackground(False)
        mainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Language.Russian, QtCore.QLocale.Country.Russia))
        self.centralwidget = QtWidgets.QWidget(parent=mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bStartStopRecord = QtWidgets.QPushButton(parent=self.centralwidget)
        self.bStartStopRecord.setGeometry(QtCore.QRect(850, 610, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bStartStopRecord.setFont(font)
        self.bStartStopRecord.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.bStartStopRecord.setStyleSheet("border: 2px solid #ABABAB;\n"
"border-radius: 10px;\n"
"background-color: #DADADA;")
        self.bStartStopRecord.setIconSize(QtCore.QSize(32, 32))
        self.bStartStopRecord.setFlat(True)
        self.bStartStopRecord.setObjectName("bStartStopRecord")
        self.bFinishRecord = QtWidgets.QPushButton(parent=self.centralwidget)
        self.bFinishRecord.setGeometry(QtCore.QRect(820, 660, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bFinishRecord.setFont(font)
        self.bFinishRecord.setStyleSheet("border: 2px solid #ABABAB;\n"
"border-radius: 10px;\n"
"background-color: #DADADA;")
        self.bFinishRecord.setObjectName("bFinishRecord")
        self.etSymptoms = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.etSymptoms.setGeometry(QtCore.QRect(10, 320, 381, 400))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.etSymptoms.setFont(font)
        self.etSymptoms.setStyleSheet("border: 2px solid #ABABAB;\n"
"border-radius: 10px;")
        self.etSymptoms.setObjectName("etSymptoms")
        self.etDiagnose = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.etDiagnose.setGeometry(QtCore.QRect(400, 320, 271, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.etDiagnose.setFont(font)
        self.etDiagnose.setStyleSheet("border: 2px solid #ABABAB;\n"
"border-radius: 10px;")
        self.etDiagnose.setObjectName("etDiagnose")
        self.symptomLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.symptomLabel.setGeometry(QtCore.QRect(10, 293, 104, 29))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.symptomLabel.setFont(font)
        self.symptomLabel.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border: 2px solid #ABABAB;\n"
"min-height: 25px;\n"
"min-width: 100px;\n"
"max-height: 25px;\n"
"max-width: 100px;\n"
"background-color: #DADADA;\n"
"")
        self.symptomLabel.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.symptomLabel.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.symptomLabel.setLineWidth(1)
        self.symptomLabel.setMidLineWidth(1)
        self.symptomLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.symptomLabel.setObjectName("symptomLabel")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 293, 104, 29))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border: 2px solid #ABABAB;\n"
"min-height: 25px;\n"
"min-width: 100px;\n"
"max-height: 25px;\n"
"max-width: 100px;\n"
"background-color: #DADADA;")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 661, 261))
        self.groupBox.setStyleSheet("background-color: #FFFFFF;\n"
"border-radius: 10px;\n"
"border: 2px solid #ABABAB;\n"
"")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.lName = QtWidgets.QLabel(parent=self.groupBox)
        self.lName.setGeometry(QtCore.QRect(10, 12, 611, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lName.setFont(font)
        self.lName.setStyleSheet("border: 0px solid #FFFFFF;\n"
"")
        self.lName.setObjectName("lName")
        self.lAgeBirthday = QtWidgets.QLabel(parent=self.groupBox)
        self.lAgeBirthday.setGeometry(QtCore.QRect(10, 40, 411, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lAgeBirthday.setFont(font)
        self.lAgeBirthday.setStyleSheet("border: 0px;")
        self.lAgeBirthday.setObjectName("lAgeBirthday")
        self.lSex = QtWidgets.QLabel(parent=self.groupBox)
        self.lSex.setGeometry(QtCore.QRect(10, 70, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lSex.setFont(font)
        self.lSex.setStyleSheet("border: 0px;")
        self.lSex.setObjectName("lSex")
        self.lCardNum = QtWidgets.QLabel(parent=self.groupBox)
        self.lCardNum.setGeometry(QtCore.QRect(10, 95, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lCardNum.setFont(font)
        self.lCardNum.setStyleSheet("border: 0px;")
        self.lCardNum.setObjectName("lCardNum")
        self.lPolisNum = QtWidgets.QLabel(parent=self.groupBox)
        self.lPolisNum.setGeometry(QtCore.QRect(10, 122, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lPolisNum.setFont(font)
        self.lPolisNum.setStyleSheet("border: 0px;")
        self.lPolisNum.setObjectName("lPolisNum")
        self.lAllergy = QtWidgets.QLabel(parent=self.groupBox)
        self.lAllergy.setGeometry(QtCore.QRect(10, 150, 311, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lAllergy.setFont(font)
        self.lAllergy.setStyleSheet("border: 0px;\n"
"border-radius: 5px;\n"
"background-color: #FF8282;\n"
"padding-left: 2px;\n"
"\n"
"")
        self.lAllergy.setObjectName("lAllergy")
        self.lBloodType = QtWidgets.QLabel(parent=self.groupBox)
        self.lBloodType.setGeometry(QtCore.QRect(10, 210, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lBloodType.setFont(font)
        self.lBloodType.setStyleSheet("border: 0px;")
        self.lBloodType.setObjectName("lBloodType")
        self.lChrDiseases = QtWidgets.QLabel(parent=self.groupBox)
        self.lChrDiseases.setGeometry(QtCore.QRect(10, 180, 311, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lChrDiseases.setFont(font)
        self.lChrDiseases.setStyleSheet("border: 0px;")
        self.lChrDiseases.setObjectName("lChrDiseases")
        self.etDrugs = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.etDrugs.setGeometry(QtCore.QRect(400, 480, 271, 231))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.etDrugs.setFont(font)
        self.etDrugs.setStyleSheet("border: 2px solid #ABABAB;\n"
"border-radius: 10px;")
        self.etDrugs.setObjectName("etDrugs")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(400, 453, 104, 29))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border: 2px solid #ABABAB;\n"
"min-height: 25px;\n"
"min-width: 100px;\n"
"max-height: 25px;\n"
"max-width: 100px;\n"
"background-color: #DADADA;")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.lResDrugs = QtWidgets.QLabel(parent=self.centralwidget)
        self.lResDrugs.setGeometry(QtCore.QRect(690, 46, 281, 225))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lResDrugs.setFont(font)
        self.lResDrugs.setStyleSheet("border: 2px solid #ABABAB;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"background-color: #FFFFFF;")
        self.lResDrugs.setText("")
        self.lResDrugs.setObjectName("lResDrugs")
        self.lResMed = QtWidgets.QLabel(parent=self.centralwidget)
        self.lResMed.setGeometry(QtCore.QRect(690, 19, 174, 29))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lResMed.setFont(font)
        self.lResMed.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border: 2px solid #ABABAB;\n"
"min-height: 25px;\n"
"min-width: 170px;\n"
"max-height: 25px;\n"
"max-width: 170px;\n"
"background-color: #DADADA;")
        self.lResMed.setObjectName("lResMed")
        self.bTransfToPdf = QtWidgets.QPushButton(parent=self.centralwidget)
        self.bTransfToPdf.setGeometry(QtCore.QRect(890, 570, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bTransfToPdf.setFont(font)
        self.bTransfToPdf.setStyleSheet("border: 2px solid #FD9396;\n"
"border-radius: 10px;\n"
"background-color: #FEC2C4;")
        self.bTransfToPdf.setObjectName("bTransfToPdf")
        self.etNotes = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.etNotes.setGeometry(QtCore.QRect(690, 320, 281, 221))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.etNotes.setFont(font)
        self.etNotes.setStyleSheet("background-color: #FFFFAE;\n"
"border: 2px solid #FFFFAE;\n"
"border-radius: 10px;\n"
"padding-top: 20px;\n"
"padding-left: 5px;")
        self.etNotes.setObjectName("etNotes")
        self.lNotes = QtWidgets.QLabel(parent=self.centralwidget)
        self.lNotes.setGeometry(QtCore.QRect(690, 325, 281, 16))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setUnderline(False)
        self.lNotes.setFont(font)
        self.lNotes.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lNotes.setObjectName("lNotes")
        self.recognIndicator = QtWidgets.QPushButton(parent=self.centralwidget)
        self.recognIndicator.setEnabled(False)
        self.recognIndicator.setGeometry(QtCore.QRect(820, 622, 21, 21))
        self.recognIndicator.setStyleSheet("border-radius: 10px;\n"
"background-color: #00FF00;\n"
"border: 2px solid #ABABAB;")
        self.recognIndicator.setText("")
        self.recognIndicator.setObjectName("recognIndicator")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 22))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Новый прием"))
        self.bStartStopRecord.setText(_translate("mainWindow", "Начать прием"))
        self.bFinishRecord.setText(_translate("mainWindow", "Закончить прием"))
        self.symptomLabel.setText(_translate("mainWindow", "симптомы"))
        self.label_2.setText(_translate("mainWindow", "диагноз"))
        self.lName.setText(_translate("mainWindow", "ФИО: Иванов Иван Иванович"))
        self.lAgeBirthday.setText(_translate("mainWindow", "Возраст/дата рождения: 99 лет (12.12.1212)"))
        self.lSex.setText(_translate("mainWindow", "Пол: Мужской"))
        self.lCardNum.setText(_translate("mainWindow", "Номер карты: 12345"))
        self.lPolisNum.setText(_translate("mainWindow", "№ полиса: 123-123-00"))
        self.lAllergy.setText(_translate("mainWindow", "Аллергии: Пыльца; Белок;"))
        self.lBloodType.setText(_translate("mainWindow", "Группа крови: 1(+)"))
        self.lChrDiseases.setText(_translate("mainWindow", "Хрон. болезни: Гипертония"))
        self.label_7.setText(_translate("mainWindow", "лекарства"))
        self.lResMed.setText(_translate("mainWindow", "Назнач. лекарства"))
        self.bTransfToPdf.setText(_translate("mainWindow", "Экспорт в PDF"))
        self.lNotes.setText(_translate("mainWindow", "Заметки"))
