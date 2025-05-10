from sqlalchemy import Column, Integer, String, Date, Enum, Text, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

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

    appointments = relationship("Appointment", back_populates="patient", cascade="all, delete-orphan")


class Appointment(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer, ForeignKey('patients.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)

    symptoms = Column(Text)
    diagnosis = Column(String(255))
    procedures = Column(Text)
    prescribed_medications = Column(Text)
    notes = Column(Text)

    patient = relationship("Patient", back_populates="appointments")
