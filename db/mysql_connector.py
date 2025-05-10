from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.appointment_data_encryption import DataEncryptor
from db.db_classes import Patient, Appointment


class MySqlConnector:

    def __init__(self, host="localhost", user="dev", password="dev13_2", database="medical_center"):
        super().__init__()

        self.conn = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}", echo=True)
        sessionmkr = sessionmaker(bind=self.conn)
        self.session = sessionmkr()
        self.encryptor = DataEncryptor()

    def get_info_about_patient(self, patient_id):
        res = self.session.query(Patient).filter_by(id=patient_id).all()

        return res

    def save_appointment_data(self, patient_id: int, symptoms: str, diagnosis: str,
                              procedures: str, medications: str, notes: str):
        encrypted_data = Appointment(
            patient_id=patient_id,
            symptoms=self.encryptor.encrypt_data(symptoms),
            diagnosis=self.encryptor.encrypt_data(diagnosis),
            procedures=self.encryptor.encrypt_data(procedures),
            medications=self.encryptor.encrypt_data(medications),
            notes=self.encryptor.encrypt_data(notes)
        )
        self.session.add(encrypted_data)
        self.session.commit()

    def close_db_connection(self):
        self.session.close()
