from pydantic import BaseModel
from typing import Optional
import models

class StudentBase(BaseModel):
    firstname: str
    middlename: str
    lastname: str
    course: str
    email: str
    password: str

class StudentCreate(StudentBase):
    pass

class StudentUpdate(StudentBase):
    firstname: Optional[str]
    middlename: Optional[str]
    lastname: Optional[str]
    course: Optional[str]
    email: Optional[str]
    password: Optional[str]
class StudentInDB(StudentBase):
    id: uuid.UUID

class StudentOut(StudentInDB):
    pass