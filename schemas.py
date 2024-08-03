from pydantic import BaseModel
from typing import List, Optional

class StudentBase(BaseModel):
    name: str
    age: int
    teacher_id: Optional[int] = None

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int

    class Config:
        orm_mode = True

class TeacherBase(BaseModel):
    name: str
    subject: str

class TeacherCreate(TeacherBase):
    pass

class Teacher(TeacherBase):
    id: int
    students: List[Student] = []

    class Config:
        orm_mode = True
