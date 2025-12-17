from pydantic import BaseModel

class VendorBase(BaseModel):
    cart_name: str
    food_type: str
    vendor_name: str
    phone: str  
    location: str
    menu_list: str| None = None
    open_time: str
    image_url: str
    close_time: str

class VendorCreate(VendorBase):
    pass


class VendorSchema(VendorCreate):
    id: int    
