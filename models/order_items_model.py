from sqlalchemy import Column, Integer,Float,String
from database import Base


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, nullable=False)
    product_id = Column(Integer, nullable=False)
    quantity = Column(Integer, default=1)
    price = Column(Float, nullable=False)
    description=Column(String)
    total_price = Column(Float, nullable=False)



