from sqlalchemy.orm import Session
from models import DeliveryOrder
from schemas import DeliveryUpdate

def update_delivery_status(db: Session, order_id: int, update: DeliveryUpdate):
    db_order = db.query(DeliveryOrder).filter(DeliveryOrder.id == order_id).first()
    if db_order:
        db_order.status = update.status
        db.commit()
        db.refresh(db_order)
    return db_order


def create_mock_order(db: Session, order_id: int):
    # For testing delivery updates independently
    order = DeliveryOrder(id=order_id, status="assigned")
    db.add(order)
    db.commit()
    db.refresh(order)
    return order
