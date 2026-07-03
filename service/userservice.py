from sqlalchemy.orm import Session
from schema.user import CreateUser, LoginUser
from schema.token import Token,TokenData
from model.user import User
from fastapi.exceptions import HTTPException
from service.authservice import authenticate_user, create_access_token, get_current_user
from datetime import timedelta
from pwdlib import PasswordHash

ACCESS_TOKEN_EXPIRE_MINUTES = 30
password_hash = PasswordHash.recommended()

def create_user(user: CreateUser, db: Session) -> Token:
    try:
        newUser = User(
            name = user.name,
            email = user.email,
            password = password_hash.hash(user.password)
        )
        db.add(newUser)
        db.commit()

        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(data = {"email": newUser.email}, expires_delta=access_token_expires)

        return Token(access_token = access_token, token_type = "bearer")
    except Exception as e:
        raise HTTPException(status_code=400)
    
def user_login(user: LoginUser, db: Session) -> Token:
    authenticatedUser = authenticate_user(user.email, user.password, db)
    if not authenticatedUser:
        raise HTTPException(status_code=401)
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data = {"email": authenticatedUser.email}, expires_delta=access_token_expires)

    return Token(access_token = access_token, token_type = "bearer")