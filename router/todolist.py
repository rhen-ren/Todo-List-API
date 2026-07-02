from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schema.user import CreateUser
from dependency import get_db


router = APIRouter()

@router.post("/register")
def user_register(user: CreateUser, db: Session = Depends(get_db)):
    pass