from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from passlib.context import CryptContext # type: ignore
from .schemas import (
    Usercreate
    )
from .models import(
    User
)

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

def create_user(db: Session, user: Usercreate):
    db_user = User(
        username=user.username,
        email=user.email,
        position=user.position,
    )
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except SQLAlchemyError as e:
        db.rollback()  # Rollback in case of any SQLAlchemy error
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database error.")
    return db_user
