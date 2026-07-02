from pydantic import BaseModel

class Token(BaseModel):
    token: str

class TokenData(BaseModel):
    email: str | None