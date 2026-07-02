from sqlalchemy.orm import Session
from dependency import get_db
from schema.user import CreateUser, LoginUser
from schema.token import Token,TokenData
from model.user import User
from fastapi.exceptions import HTTPException
from service.authservice import authenticate_user, create_access_token
from datetime import timedelta
from pwdlib import PasswordHash

ACCESS_TOKEN_EXPIRE_MINUTES = 30
password_hash = PasswordHash.recommended()

def create_user(user: CreateUser, db: Session):
    try:
        newUser = User(
            name = user.name,
            email = user.email,
            password = password_hash.hash(user.password)
        )
        db.add(newUser)
        db.commit()
    except:
        raise HTTPException(status_code=400)
    
def user_login(user: LoginUser, db: Session) -> Token:
    authenticatedUser = authenticate_user(user.email, user.password, db)
    if not user:
        pass
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data = TokenData(email=authenticatedUser.email), expires_delta=access_token_expires)

    return Token(token = access_token)