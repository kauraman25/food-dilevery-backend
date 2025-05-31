from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, SessionLocal, Base

# Create all tables in database
Base.metadata.create_all(bind=engine)

app = FastAPI(title="User Service")

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------------------
# User Routes
# ---------------------------

@app.post("/users/", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)


# ---------------------------
# Order Routes
# ---------------------------

@app.post("/orders/", response_model=schemas.OrderOut)
def place_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db, order)


@app.get("/orders/{order_id}", response_model=schemas.OrderOut)
def get_order(order_id: int, db: Session = Depends(get_db)):
    db_order = crud.get_order(db, order_id)
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order


# ---------------------------
# Rating Routes
# ---------------------------

@app.post("/ratings/", response_model=schemas.RatingOut)
def rate_order_or_agent(rating: schemas.RatingCreate, db: Session = Depends(get_db)):
    return crud.create_rating(db, rating)


@app.get("/ratings/order/{order_id}", response_model=schemas.RatingOut)
def get_rating(order_id: int, db: Session = Depends(get_db)):
    rating = crud.get_rating_by_order(db, order_id)
    if not rating:
        raise HTTPException(status_code=404, detail="Rating not found")
    return rating
