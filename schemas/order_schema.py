from pydantic import BaseModel

class OrderBase(BaseModel):
    user_id: int
    food_id: int
    quantity: int

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int


