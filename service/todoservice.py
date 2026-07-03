from sqlalchemy.orm import Session
from schema.todo import CreateToDo
from service.authservice import get_current_user
from model.todo import Todo
from fastapi.exceptions import HTTPException


def create_todo_item(todo: CreateToDo, token: str, db: Session):
    try:
        current_user = get_current_user(token, db)
        if current_user:
            newItem = Todo(
                user_id = current_user.id,
                title = todo.title,
                description = todo.description
            )
            db.add(newItem)
            db.commit()
        else:
            return {"message" : "unauthorized"}
    except:
        raise HTTPException(status_code=401)