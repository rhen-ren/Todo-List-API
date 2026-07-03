from datetime import datetime, timedelta, timezone
from typing import Annotated
from fastapi import Depends
import jwt
from model.user import User
from schema.token import TokenData
from secret import secret_key
from fastapi.security import OAuth2PasswordBearer
from pwdlib import PasswordHash
from sqlalchemy.orm import Session
from sqlalchemy import select
from dependency import oauth2_scheme
from secret import secret_key

SECRET_KEY = secret_key
ALGORITHM = "HS256"
password_hash = PasswordHash.recommended()
def authenticate_user(email: str, password: str, db: Session):
    user = db.execute(select(User).where(User.email == email)).scalars().one_or_none()
    if not user:
        return False
    if not password_hash.verify(password, user.password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta | None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=20)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)
    return encoded_jwt

def get_current_user(token: str, db: Session):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("email")
        if email is None:
            return None
        token_data = TokenData(email = email)
        user = db.execute(select(User).where(User.email == token_data.email)).scalars().one_or_none()
        if not user:
            return None
        return user
    except Exception as e:
        raise e