from pydantic import BaseModel
from datetime import datetime

class CartBase(BaseModel):
    user_id: int

    delivery_type: str
    delivery_charge: float

    street: str | None = None
    house: str | None = None
    floor: str | None = None
    full_address: str | None = None

    tip_amount: float
    promo_code: str | None = None
    promo_discount: float

    subtotal: float
    total_amount: float


class CartCreate(CartBase):
    pass


class CartSchema(CartBase):
    id: int
    created_at: datetime


