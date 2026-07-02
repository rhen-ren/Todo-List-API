from sqlalchemy.orm import Session
from dependency import get_db
from schema.user import CreateUser
from model.user import User
from fastapi.exceptions import HTTPException



def create_user(user: CreateUser, db: Session):
    #createNew user
    #TODO: make password into a hash
    try:
        newUser = User(
            name = user.name,
            email = user.email,
            password = user.password
        )
        db.add(newUser)
        db.commit()
    except:
        raise HTTPException(status_code=400)