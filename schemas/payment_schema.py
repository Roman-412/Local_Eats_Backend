from pydantic import BaseModel
from datetime import datetime

class PaymentCreate(BaseModel):
    order_id: int
    user_name: str
    phone: str
    payment_method: str
    amount: float


class PaymentUpdate(BaseModel):
    payment_status: str


class PaymentSchema(PaymentCreate):
    id: int
    payment_status: str





