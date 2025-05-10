from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.db_classes import Patient


class MySqlConnector:

    def __init__(self, host="localhost", user="dev", password="dev13_2", database="medical_center"):
        super().__init__()

        self.conn = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}", echo=True)
        sessionmkr = sessionmaker(bind=self.conn)
        self.session = sessionmkr()

    def get_info_about_patient(self, patient_id):
        res = self.session.query(Patient).filter_by(id=patient_id).all()

        return res

    def close_db_connection(self):
        self.session.close()
