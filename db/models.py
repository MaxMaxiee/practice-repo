import uuid
from sqlalchemy import Column, String
from db.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    firstname = Column(String)
    middlename = Column(String)
    lastname = Column(String)
    course = Column(String)  # Store courses as a serialized string
    email = Column(String, unique=True, index=True)
    password = Column(String)