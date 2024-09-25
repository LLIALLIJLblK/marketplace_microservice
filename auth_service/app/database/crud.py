from sqlalchemy.orm import Session
from . import models, schemas
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


get_passowrd_hash = lambda password: pwd_context.hash(password)

def create_user(db: Session,user: schemas.UserCreate):
    hashed_password = get_passowrd_hash(user.hashed_password)
    db_user = models.User(
        user_name=user.user_name,
        user_second_name=user.user_second_name,
        phone_number=user.phone_number,
        email=user.email,
        hashed_password=hashed_password,
        date_of_birth=user.date_of_birth,
        gender=user.gender,
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

