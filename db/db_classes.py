from sqlalchemy import Column, Integer, String, Date, Enum, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(100), nullable=False)
    birth_date = Column(Date, nullable=False)
    gender = Column(Enum('М', 'Ж'), nullable=False)
    medical_card_number = Column(String(20), unique=True, nullable=False)
    insurance_policy_number = Column(String(16), unique=True)
    allergies = Column(Text)
    chronic_diseases = Column(Text)
    blood_type = Column(Enum('1(+)', '1(-)', '2(+)', '2(-)', '3(+)', '3(-)', '4(+)', '4(-)'))
    prescribed_medications = Column(Text)