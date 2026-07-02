from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schema.user import CreateUser
from dependency import get_db
from service.userservice import create_user


router = APIRouter()

@router.post("/register")
def user_register(user: CreateUser, db: Session = Depends(get_db)):
    return create_user(user, db)