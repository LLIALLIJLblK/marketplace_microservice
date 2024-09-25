from sqlalchemy import Column, Integer, String, Date,TypeDecorator
from .database import Base
from datetime import datetime



class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, unique=True, index=True)
    user_second_name = Column(String, index=True)
    phone_number = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    date_of_birth = Column(Date)
    gender = Column(String)
    role = Column(String)

