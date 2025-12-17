from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.cart_model import Cart
from models.user_model import User
from schemas.cart_schema import CartCreate, CartSchema

router = APIRouter(
    prefix="/cart",
    tags=["Cart"]
)

@router.post("/", response_model=CartSchema)
def create_cart(cart: CartCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == cart.user_id).first()
    if not user:
        raise HTTPException(status_code=400, detail="User does not exist")

    new_cart = Cart(
        user_id=cart.user_id,
        delivery_type=cart.delivery_type,
        delivery_charge=cart.delivery_charge,
        street=cart.street,
        house=cart.house,
        floor=cart.floor,
        full_address=cart.full_address,
        tip_amount=cart.tip_amount,
        promo_code=cart.promo_code,
        promo_discount=cart.promo_discount,
        subtotal=cart.subtotal,
        total_amount=cart.total_amount
    )

    db.add(new_cart)
    db.commit()
    db.refresh(new_cart)
    return new_cart

@router.get("/", response_model=list[CartSchema])
def get_all_carts(db: Session = Depends(get_db)):
    return db.query(Cart).all()

@router.get("/{cart_id}", response_model=CartSchema)
def get_cart(cart_id: int, db: Session = Depends(get_db)):
    cart = db.query(Cart).filter(Cart.id == cart_id).first()
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")
    return cart

@router.put("/{cart_id}", response_model=CartSchema)
def update_cart(cart_id: int, data: CartCreate, db: Session = Depends(get_db)):
    cart = db.query(Cart).filter(Cart.id == cart_id).first()
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")

    cart.delivery_type = data.delivery_type
    cart.delivery_charge = data.delivery_charge
    cart.street = data.street
    cart.house = data.house
    cart.floor = data.floor
    cart.full_address = data.full_address
    cart.tip_amount = data.tip_amount
    cart.promo_code = data.promo_code
    cart.promo_discount = data.promo_discount
    cart.subtotal = data.subtotal
    cart.total_amount = data.total_amount

    db.commit()
    db.refresh(cart)
    return cart

@router.delete("/{cart_id}")
def delete_cart(cart_id: int, db: Session = Depends(get_db)):
    cart = db.query(Cart).filter(Cart.id == cart_id).first()
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")

    db.delete(cart)
    db.commit()
    return {"message": "Cart deleted successfully"}

