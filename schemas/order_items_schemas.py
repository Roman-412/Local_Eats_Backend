from pydantic import BaseModel

class OrderItemCreate(BaseModel):
    order_id: int
    product_id: int
    quantity: int
    price: float
    description: str

class OrderItemSchema(OrderItemCreate):
    id: int
    total_price: float

