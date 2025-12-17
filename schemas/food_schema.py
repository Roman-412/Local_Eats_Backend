from pydantic import BaseModel

class FoodBase(BaseModel):
    name: str
    price: int

class FoodCreate(FoodBase):
    pass

class Food(FoodBase):
    id: int
