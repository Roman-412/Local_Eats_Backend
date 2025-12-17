from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.order_items_model import OrderItem
from schemas.order_items_schemas import OrderItemCreate, OrderItemSchema

router = APIRouter(prefix="/order_items")

@router.post("/", response_model=OrderItemSchema)
def create_item(item: OrderItemCreate, db: Session = Depends(get_db)):
    total_price = item.quantity * item.price

    new_item = OrderItem(
        order_id=item.order_id,
        product_id=item.product_id,
        quantity=item.quantity,
        price=item.price,
        total_price=total_price
    )

    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


@router.get("/", response_model=list[OrderItemSchema])
def all_items(db: Session = Depends(get_db)):
    return db.query(OrderItem).all()

@router.get("/{order_id}", response_model=list[OrderItemSchema])
def get_by_order(order_id: int, db: Session = Depends(get_db)):
    return db.query(OrderItem).filter(OrderItem.order_id == order_id).all()

@router.put("/{item_id}", response_model=OrderItemSchema)
def update_item(item_id: int, data: OrderItemCreate, db: Session = Depends(get_db)):
    item = db.query(OrderItem).filter(OrderItem.id == item_id).first()
    if not item:
        raise HTTPException(404, "Item not found")

    item.order_id = data.order_id
    item.product_id = data.product_id
    item.quantity = data.quantity
    item.price = data.price
    item.total_price = data.quantity * data.price

    db.commit()
    db.refresh(item)
    return item

@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(OrderItem).filter(OrderItem.id == item_id).first()
    if not item:
        raise HTTPException(404, "Item not found")
    db.delete(item)
    db.commit()
    return {"message": "Item deleted"}
