from pydantic import BaseModel, EmailStr
from datetime import date

class UserCreate(BaseModel):
    user_name: str
    user_second_name: str
    phone_number: str
    email: EmailStr
    hashed_password: str
    date_of_birth: date
    gender: str
    role: str