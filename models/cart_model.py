from sqlalchemy import Column, Integer, Float, String, ForeignKey
from database import Base


class Cart(Base):
    __tablename__ = "carts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    delivery_type = Column(String, default="home")   
    delivery_charge = Column(Float, default=30)
    street = Column(String)
    house = Column(String)
    floor = Column(String)
    full_address = Column(String)
    tip_amount = Column(Float, default=0)
    promo_code = Column(String, nullable=True)
    promo_discount = Column(Float, default=0)
    subtotal = Column(Float, nullable=False)
    total_amount = Column(Float, nullable=False)




