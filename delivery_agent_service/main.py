from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import Base, engine, SessionLocal

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Delivery Agent Service")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.patch("/delivery/{order_id}", response_model=schemas.DeliveryOut)
def update_status(order_id: int, update: schemas.DeliveryUpdate, db: Session = Depends(get_db)):
    order = crud.update_delivery_status(db, order_id, update)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@app.post("/delivery/{order_id}", response_model=schemas.DeliveryOut)
def create_mock(order_id: int, db: Session = Depends(get_db)):
    return crud.create_mock_order(db, order_id)
