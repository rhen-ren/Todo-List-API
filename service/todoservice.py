from sqlalchemy.orm import Session
from schema.todo import CreateToDo, GetToDo
from service.authservice import get_current_user
from model.todo import Todo
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse


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
            db.refresh(newItem)

            return GetToDo(
                id=newItem.id,
                title=newItem.title,
                description=newItem.description
            )
        else:
            return {"message" : "unauthorized"}
    except:
        raise HTTPException(status_code=401)
    
def update_todo_item(todo: CreateToDo, id: int, token: str, db: Session):
    try:
        current_user = get_current_user(token, db)
        current_todo = db.get(Todo, id)
        if current_todo.user_id == current_user.id:
            current_todo.title = todo.title
            current_todo.description = todo.description
            db.commit()
            db.refresh(current_todo)

            return GetToDo(
                id=current_todo.id,
                title=current_todo.title,
                description=current_todo.description
            )
        else:
            return {"message" : "forbidden"}
    except:
        raise HTTPException(status_code=401)

def delete_todo_item(todo: CreateToDo, id: int, token: str, db: Session):
    try:
        current_user = get_current_user(token, db)
        current_todo = db.get(Todo, id)
        if current_todo.user_id == current_user.id:
            db.delete(current_todo)
            db.commit()
            return JSONResponse(status_code=204)
        else:
            return {"message" : "forbidden"}
    except:
        raise HTTPException(status_code=401)