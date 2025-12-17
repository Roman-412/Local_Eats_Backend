from sqlalchemy import Column, Integer, String
from database import Base

class Vendor(Base):
    __tablename__ = "vendors"

    id = Column(Integer, primary_key=True, index=True)
    cart_name = Column(String)
    food_type = Column(String)
    vendor_name = Column(String)
    phone = Column(String)
    location = Column(String)
    image_url = Column(String)
    menu_list = Column(String)
    open_time = Column(String)
    close_time = Column(String)
