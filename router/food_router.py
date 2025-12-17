from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.food_model import Food
from schemas.food_schema import FoodCreate, Food as FoodSchema

router = APIRouter(prefix="/foods")

@router.post("/", response_model=FoodSchema)
def create_food(food: FoodCreate, db: Session = Depends(get_db)):
    new_food = Food(
        name=food.name,
        price=food.price
    )
    db.add(new_food)
    db.commit()
    db.refresh(new_food)
    return new_food

@router.get("/", response_model=list[FoodSchema])
def get_foods(db: Session = Depends(get_db)):
    return db.query(Food).all()

@router.get("/{food_id}", response_model=FoodSchema)
def get_food(food_id: int, db: Session = Depends(get_db)):
    food = db.query(Food).filter(Food.id == food_id).first()
    if not food:
        raise HTTPException(404, "Food not found")
    return food

@router.put("/{food_id}", response_model=FoodSchema)
def update_food(food_id: int, data: FoodCreate, db: Session = Depends(get_db)):
    food = db.query(Food).filter(Food.id == food_id).first()
    if not food:
        raise HTTPException(404, "Food not found")
    food.name = data.name
    food.price = data.price
    db.commit()
    db.refresh(food)
    return food

@router.delete("/{food_id}")
def delete_food(food_id: int, db: Session = Depends(get_db)):
    food = db.query(Food).filter(Food.id == food_id).first()
    if not food:
        raise HTTPException(404, "Food not found")
    db.delete(food)
    db.commit()
    return {"message": "Food deleted"}
