from sqlalchemy import Column, Integer, String, Float,ForeignKey
from database import Base


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    user_name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    payment_method = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    payment_status = Column(String, default="pending")


