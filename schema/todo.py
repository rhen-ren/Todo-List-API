from pydantic import BaseModel


class CreateToDo(BaseModel):
    title: str
    description: str

class GetToDo(BaseModel):
    id: int
    title: str
    description: str