from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.vendor_model import Vendor
from schemas.vendor_schema import VendorSchema, VendorCreate, VendorBase

router = APIRouter(prefix="/vendors")

@router.post("/", response_model=VendorSchema)
def create_vendor(vendor: VendorCreate, db: Session = Depends(get_db)):
    new_vendor = Vendor(
        cart_name=vendor.cart_name,
        food_type=vendor.food_type,
        vendor_name=vendor.vendor_name,
        phone=vendor.phone,
        location=vendor.location,
        image_url=vendor.image_url,
        menu_list=vendor.menu_list,
        open_time=vendor.open_time,
        close_time=vendor.close_time
    )
    db.add(new_vendor)
    db.commit()
    db.refresh(new_vendor)
    return new_vendor


@router.get("/", response_model=list[VendorSchema])
def get_vendors(db: Session = Depends(get_db)):
    return db.query(Vendor).all()

@router.put("/{vendor_id}", response_model=VendorSchema)
def update_vendor(
    vendor_id: int,
    vendor: VendorCreate,
    db: Session = Depends(get_db)
):
    db_vendor = db.query(Vendor).filter(Vendor.id == vendor_id).first()
    if not db_vendor:
        raise HTTPException(status_code=404, detail="Vendor not found")

    db_vendor.cart_name = vendor.cart_name
    db_vendor.food_type = vendor.food_type
    db_vendor.vendor_name = vendor.vendor_name
    db_vendor.phone = vendor.phone
    db_vendor.location = vendor.location
    db_vendor.image_url = vendor.image_url
    db_vendor.menu_list = vendor.menu_list
    db_vendor.open_time = vendor.open_time
    db_vendor.close_time = vendor.close_time

    db.commit()
    db.refresh(db_vendor)
    return db_vendor

@router.delete("/{vendor_id}")
def delete_vendor(vendor_id: int, db: Session = Depends(get_db)):
    vendor = db.query(Vendor).filter(Vendor.id == vendor_id).first()
    if not vendor:
        raise HTTPException(status_code=404, detail="Vendor not found")

    db.delete(vendor)
    db.commit()
    return {"message": "Vendor deleted successfully"}
