from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    password:str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    