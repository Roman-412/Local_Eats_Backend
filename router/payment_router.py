from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.payment_model import Payment
from schemas.payment_schema import PaymentUpdate,PaymentCreate,PaymentSchema

router = APIRouter(prefix="/payments", tags=["Payments"])

@router.post("/", response_model=PaymentSchema)
def create_payment(payment: PaymentCreate, db: Session = Depends(get_db)):
    new_payment = Payment(
        order_id=payment.order_id,
        user_name=payment.user_name,
        phone=payment.phone,
        payment_method=payment.payment_method,
        amount=payment.amount
    )
    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)
    return new_payment


@router.get("/", response_model=list[PaymentSchema])
def get_payments(db: Session = Depends(get_db)):
    return db.query(Payment).all()


@router.get("/{payment_id}", response_model=PaymentSchema)
def get_payment(payment_id: int, db: Session = Depends(get_db)):
    payment = db.query(Payment).filter(Payment.id == payment_id).first()
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment
@router.put("/{payment_id}", response_model=PaymentUpdate)
def update_payment(
    payment_id: int,data: PaymentUpdate,db: Session = Depends(get_db)):
    payment = db.query(Payment).filter(Payment.id == payment_id).first()
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")

    payment.payment_status = data.payment_status

    db.commit()
    db.refresh(payment)
    return payment

@router.delete("/{payment_id}")
def delete_payment(payment_id: int, db: Session = Depends(get_db)):
    payment = db.query(Payment).filter(Payment.id == payment_id).first()
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")

    db.delete(payment)
    db.commit()
    return {"message": "Payment deleted successfully"}

