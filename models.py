

from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from database import Base

DATABASE_URL = "postgresql://postgres:amal1998@localhost/school"
engine = create_engine(DATABASE_URL)

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    subject = Column(String, index=True)

    students = relationship('Student', back_populates='teacher')


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))

    teacher = relationship('Student', back_populates='students')