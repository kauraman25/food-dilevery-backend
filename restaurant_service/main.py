from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, SessionLocal, Base

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Restaurant Service")


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Restaurant Routes

@app.post("/restaurants/", response_model=schemas.RestaurantOut)
def create_restaurant(restaurant: schemas.RestaurantCreate, db: Session = Depends(get_db)):
    return crud.create_restaurant(db, restaurant)


@app.patch("/restaurants/{restaurant_id}/status", response_model=schemas.RestaurantOut)
def update_status(restaurant_id: int, is_online: bool, db: Session = Depends(get_db)):
    restaurant = crud.set_restaurant_status(db, restaurant_id, is_online)
    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return restaurant


@app.get("/restaurants/online", response_model=list[schemas.RestaurantOut])
def get_online_restaurants(db: Session = Depends(get_db)):
    return crud.get_online_restaurants(db)


# Menu Item Routes

@app.post("/menu/", response_model=schemas.MenuItemOut)
def add_menu_item(item: schemas.MenuItemCreate, db: Session = Depends(get_db)):
    return crud.add_menu_item(db, item)


@app.get("/menu/{restaurant_id}", response_model=list[schemas.MenuItemOut])
def get_menu(restaurant_id: int, db: Session = Depends(get_db)):
    return crud.get_menu_by_restaurant(db, restaurant_id)



# Order Routes

@app.patch("/orders/{order_id}", response_model=schemas.OrderOut)
def update_order(order_id: int, order_update: schemas.OrderUpdate, db: Session = Depends(get_db)):
    order = crud.update_order_status(db, order_id, order_update)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

