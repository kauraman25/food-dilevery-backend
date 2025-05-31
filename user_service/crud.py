from sqlalchemy.orm import Session
from models import User, Order, Rating
from schemas import UserCreate, OrderCreate, RatingCreate


# -----------------------------
# User Logic
# -----------------------------

def create_user(db: Session, user: UserCreate):
    db_user = User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


# -----------------------------
# Order Logic
# -----------------------------

def create_order(db: Session, order: OrderCreate):
    db_order = Order(
        user_id=order.user_id,
        restaurant_id=order.restaurant_id,
        status="placed"
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def get_order(db: Session, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first()


# -----------------------------
# Rating Logic
# -----------------------------

def create_rating(db: Session, rating: RatingCreate):
    db_rating = Rating(
        user_id=rating.user_id,
        order_id=rating.order_id,
        rating_for_type=rating.rating_for_type,
        rating_value=rating.rating_value,
    )
    db.add(db_rating)
    db.commit()
    db.refresh(db_rating)
    return db_rating


def get_rating_by_order(db: Session, order_id: int):
    return db.query(Rating).filter(Rating.order_id == order_id).first()
