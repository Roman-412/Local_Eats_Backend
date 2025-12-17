from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.order_model import Order
from schemas.order_schema import OrderCreate, Order as OrderSchema

router = APIRouter(prefix="/orders")

@router.post("/", response_model=OrderSchema)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    new_order = Order(
        user_id=order.user_id,
        food_id=order.food_id,
        quantity=order.quantity
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order


@router.get("/", response_model=list[OrderSchema])
def get_orders(db: Session = Depends(get_db)):
    return db.query(Order).all()

@router.get("/{order_id}", response_model=OrderSchema)
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(404, "Order not found")
    return order

@router.put("/{order_id}", response_model=OrderSchema)
def update_order(order_id: int, data: OrderCreate, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(404, "Order not found")
    order.user_id = data.user_id
    order.food_id = data.food_id
    order.quantity = data.quantity
    db.commit()
    db.refresh(order)
    return order

@router.delete("/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(404, "Order not found")
    db.delete(order)
    db.commit()
    return {"message": "Order deleted"}
