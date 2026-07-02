from fastapi import FastAPI
from db import Base, engine
import uvicorn
from router import todolist

app = FastAPI()
app.include_router(todolist.router)

Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)