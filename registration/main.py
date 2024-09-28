from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import Base
from database import SessionLocal, engine 
from .models import User
from .schemas import(
    ShowUserSchema,
    Usercreate
)
from .crud import(
    create_user
)
app = FastAPI()


Base.metadata.create_all(bind=engine)
# ডাটাবেজ সেশন ডিপেন্ডেন্সি
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=ShowUserSchema)
async def register_user(user: Usercreate, db: Session = Depends(get_db)):
    rgistration = create_user(db=db, user=user)
    return rgistration
