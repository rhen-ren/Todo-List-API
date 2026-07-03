from pydantic import BaseModel, ConfigDict

class CreateToDo(BaseModel):
    title: str
    description: str

class GetToDo(BaseModel):
    id: int
    title: str
    description: str

    model_config = ConfigDict(from_attributes=True)

class GetToDoPaginated(BaseModel):
    data: list[GetToDo]
    page: int
    limit: int
    total: int