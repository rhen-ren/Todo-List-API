from typing import Annotated
from fastapi import APIRouter, Depends, Header, Query
from sqlalchemy.orm import Session
from schema.user import CreateUser, LoginUser
from schema.todo import CreateToDo
from dependency import get_db, oauth2_scheme
from fastapi.security import OAuth2PasswordRequestForm
from service import userservice, todoservice


router = APIRouter()

@router.post("/register")
def user_register(user: CreateUser, db: Session = Depends(get_db)):
    return userservice.create_user(user, db)

@router.post("/login")
def user_login(user: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    login = LoginUser(
        email=user.username,
        password=user.password
    )
    return userservice.user_login(login, db)

@router.post("/todos")
def create_todo_item(todo: CreateToDo, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    return todoservice.create_todo_item(todo, token, db)

@router.put("/todos/{id}")
def update_todo_item(todo: CreateToDo, id: int = id, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    return todoservice.update_todo_item(todo, id, token, db)

@router.get("/todos/")
def get_todos(page: int = Query(ge=1), limit: int = Query(ge=1), token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    return todoservice.get_todos(page, limit, token, db)

