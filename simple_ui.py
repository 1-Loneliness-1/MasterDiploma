from typing import Dict

from PyQt6 import QtGui, QtCore
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QTextEdit,
    QLabel, QGroupBox, QHBoxLayout
)
from audio_processor import AudioProcessor
from db.mysql_connector import MySqlConnector
from toast_widget import ToastWidget


class SimpleUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.patient_id = 2

        self.audio_processor = AudioProcessor()
        self.audio_processor.entities_recognition_done.connect(self.parse_entities)
        self.database = MySqlConnector()

        self.setWindowTitle("Новый прием")
        self.setFixedSize(1200, 750)
        self.setStyleSheet("background-color: #F4F4F4;")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/main_icon32.ico"))
        self.setWindowIcon(icon)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        left_column = QVBoxLayout()
        main_layout.addLayout(left_column, stretch=3)

        self.gbPatientInfo = QGroupBox()
        self.gbPatientInfo.setStyleSheet(
            "QGroupBox { border: 1px solid #CCCCCC; border-radius: 12px; background-color: #F4F4F4; }")
        patient_info_layout = QVBoxLayout()
        patient_info_layout.setContentsMargins(16, 16, 16, 16)
        self.gbPatientInfo.setLayout(patient_info_layout)

        self.lName = QLabel("ФИО: Иванов Иван Иванович")
        self.lAgeBirthday = QLabel("Возраст/дата рождения: 99 лет (12.12.1212)")
        self.lSex = QLabel("Пол: Мужской")
        self.lCardNum = QLabel("№ карты: 12345")
        self.lPolisNum = QLabel("№ полиса: 123-123-00")
        self.lAllergy = QLabel("Аллергии: пыльца, белок")
        self.lBloodType = QLabel("Группа крови: 1(+)")
        self.lChrDiseases = QLabel("Хрон. болезни: Гипертония")

        for label in [self.lName, self.lAgeBirthday, self.lSex, self.lCardNum, self.lPolisNum,
                      self.lAllergy, self.lBloodType, self.lChrDiseases]:
            label.setStyleSheet("font-size: 14px; color: #333333;")
            patient_info_layout.addWidget(label)

        self.lAllergy.setStyleSheet(
            "font-size: 14px; color: #333333; background-color: #FFE5E5; border-radius: 6px; padding: 4px 6px;")

        left_column.addWidget(self.gbPatientInfo)

        text_blocks_layout = QVBoxLayout()
        text_blocks_layout.setSpacing(0)
        left_column.addLayout(text_blocks_layout)

        def create_text_block(title, placeholder):
            block = QVBoxLayout()
            block.setSpacing(0)
            block_label = QLabel(title)
            block_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            block_label.setStyleSheet(
                "background-color: #DDDDDD; color: black; font-size: 16px; border-top-left-radius: 10px; "
                "border-top-right-radius: 10px; padding: 6px; margin-top: 10px;")

            block_text_edit = QTextEdit()
            block_text_edit.setPlaceholderText(placeholder)
            block_text_edit.setStyleSheet(
                "font-size: 14px; color: black; padding: 8px; background-color: white; border: 1px solid #DDDDDD; "
                "border-bottom-left-radius: 10px; border-bottom-right-radius: 10px;")

            block.addWidget(block_label)
            block.addWidget(block_text_edit)
            return block, block_text_edit

        symptoms_block, self.etSymptoms = create_text_block("Симптомы", "Начинайте записывать симптомы...")
        text_blocks_layout.addLayout(symptoms_block, stretch=1)

        horizontal_layout = QHBoxLayout()
        horizontal_layout.setSpacing(0)
        text_blocks_layout.addLayout(horizontal_layout, stretch=1)

        diagnosis_and_drugs_layout = QVBoxLayout()
        diagnosis_and_drugs_layout.setSpacing(0)
        horizontal_layout.addLayout(diagnosis_and_drugs_layout)

        diagnose_block, self.etDiagnose = create_text_block("Диагноз", "Введите диагноз...")
        diagnosis_and_drugs_layout.addLayout(diagnose_block)

        drugs_block, self.etDrugs = create_text_block("Лекарства", "Введите назначаемые лекарства...")
        diagnosis_and_drugs_layout.addLayout(drugs_block)

        procedure_block = QVBoxLayout()
        procedure_block.setSpacing(0)
        self.lProcedures = QLabel("Процедуры")
        self.lProcedures.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lProcedures.setStyleSheet(
            "background-color: #DDDDDD; color: black; font-size: 16px; border-top-left-radius: 10px; "
            "border-top-right-radius: 10px; padding: 6px; margin-top: 10px; margin-left: 10px;")

        self.etProcedures = QTextEdit()
        self.etProcedures.setPlaceholderText("Введите необходимые процедуры...")
        self.etProcedures.setStyleSheet("font-size: 14px; color: black; padding: 8px; background-color: white; "
                                        "border: 1px solid #DDDDDD; border-bottom-left-radius: 10px; border-bottom-right-radius: 10px;"
                                        "margin-left: 10px;")
        procedure_block.addWidget(self.lProcedures)
        procedure_block.addWidget(self.etProcedures)

        horizontal_layout.addLayout(procedure_block)

        right_column = QVBoxLayout()
        right_column.setSpacing(0)
        main_layout.addLayout(right_column, stretch=2)

        self.lReservedDrugs = QLabel("Назначенные лекарства")
        self.lReservedDrugs.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lReservedDrugs.setStyleSheet(
            "background-color: #DDDDDD; color: black; font-size: 16px; border-top-left-radius: 10px; border-top-right-radius: 10px; "
            "padding: 6px; margin-left: 10px;")

        self.lResDrugBody = QLabel()
        self.lResDrugBody.setStyleSheet(
            "background-color: white; border: 1px solid #DDDDDD; border-bottom-left-radius: 10px; "
            "border-bottom-right-radius: 10px; font-size: 13px; padding: 10px; margin-left: 10px;")
        self.lResDrugBody.setWordWrap(True)

        right_column.addWidget(self.lReservedDrugs)
        right_column.addWidget(self.lResDrugBody, stretch=1)

        notes_label = QLabel("Заметки")
        notes_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        notes_label.setFont(font)
        notes_label.setStyleSheet(
            "background-color: #FFFFCC; color: black; border-top-left-radius: 10px; border-top-right-radius: 10px; "
            "padding: 6px; margin-left: 10px; margin-top: 35px;")

        self.etNotes = QTextEdit()
        self.etNotes.setStyleSheet(
            "background-color: #FFFFCC; color: black; font-size: 15px; border-bottom-left-radius: 10px;"
            "border-bottom-right-radius: 10px; padding: 8px; margin-left: 10px;")

        right_column.addWidget(notes_label)
        right_column.addWidget(self.etNotes, stretch=1)

        bottom_button_layout = QHBoxLayout()

        self.bStartStopReception = QPushButton("Начать прием")
        self.bStartStopReception.setStyleSheet(
            "font-size: 14px; background-color: #6D91FA; color: white; border-radius: 10px; padding: 8px 16px;"
            "margin-left: 10px; margin-right: 5px; margin-top: 25px;")
        self.bStartStopReception.clicked.connect(self.toggle_recording)
        bottom_button_layout.addWidget(self.bStartStopReception)

        self.bFinishReception = QPushButton("Завершить прием")
        self.bFinishReception.setStyleSheet(
            "font-size: 14px; color: white; background-color: #FF8080; border-radius: 10px; padding: 8px 16px;"
            "margin-left: 5px; margin-right: 10px; margin-top: 25px;")
        self.bFinishReception.clicked.connect(self.finish_appointment)
        bottom_button_layout.addWidget(self.bFinishReception)

        right_column.addLayout(bottom_button_layout)

        self.get_info_by_database(2)

    def closeEvent(self, event):
        self.database.close_db_connection()

    def toggle_recording(self):
        if self.audio_processor.recording_active:
            self.display_toast("Запись остановлена", duration=1500)
            self.audio_processor.stop_process()
            self.bStartStopReception.setText("Начать прием")
        else:
            self.display_toast("Запись начата", duration=1500)
            self.audio_processor.start_process()
            self.bStartStopReception.setText("Остановить прием")

    def parse_entities(self, entities_dictionary: Dict):

        for ent_obj in entities_dictionary["entities"]["Drugname"]:
            self.etDrugs.append("-" + ent_obj["text"] + "\n")

        for ent_obj in entities_dictionary["entities"]["symptom"]:
            self.etSymptoms.append("-" + ent_obj["text"] + "\n")

        for ent_obj in entities_dictionary["entities"]["procedure"]:
            self.etProcedures.append("-" + ent_obj["text"] + "\n")

    def get_info_by_database(self, patient_id):
        patients = self.database.get_info_about_patient(patient_id)

        for patient in patients:
            self.patient_id = patient.id

            self.lName.setText(f"ФИО: {patient.full_name}")
            self.lAgeBirthday.setText(f"Дата рождения: {patient.birth_date}")
            self.lSex.setText(f"Пол: {patient.gender}")
            self.lCardNum.setText(f"Номер медицинской карты: {patient.medical_card_number}")
            self.lPolisNum.setText(f"Номер полиса: {patient.insurance_policy_number}")
            if patient.allergies is None:
                self.lAllergy.setText("Аллергии: -")
            else:
                self.lAllergy.setText(f"Аллергии: {patient.allergies}")
            self.lBloodType.setText(f"Группа крови: {patient.blood_type}")
            if patient.chronic_diseases is None:
                self.lChrDiseases.setText("Хронические болезни: -")
            else:
                self.lChrDiseases.setText(f"Хронические болезни: {patient.chronic_diseases}")
            if patient.prescribed_medications is not None:
                self.lResDrugBody.setText(f"{patient.prescribed_medications}")

    def display_toast(self, message: str, duration: int = 1500):
        QTimer.singleShot(0, lambda: ToastWidget(self, message, duration))

    def finish_appointment(self):
        self.display_toast("Шифрование и сохранение\nданных", duration=1500)
        self.database.save_appointment_data(
            patient_id=self.patient_id,
            symptoms=self.etSymptoms.toPlainText(),
            diagnosis=self.etDiagnose.toPlainText(),
            procedures=self.etProcedures.toPlainText(),
            medications=self.etDrugs.toPlainText(),
            notes=self.etNotes.toPlainText()
        )
