from fastapi import APIRouter, Depends, HTTPException
from database import SessionLocal
from models.user import User
from passlib.hash import bcrypt
from sqlalchemy.orm import Session
import secrets

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register_user(username: str, password: str, db: Session = Depends(get_db)):
    hashed_password = bcrypt.hash(password)
    user = User(username=username, password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"id": user.id, "username": user.username}

@router.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user or not bcrypt.verify(password, user.password):
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    token = secrets.token_hex(16)
    user.token = token
    db.add(user)
    db.commit()
