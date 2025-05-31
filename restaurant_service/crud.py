from sqlalchemy.orm import Session
from models import Restaurant, MenuItem, Order
from schemas import (
    RestaurantCreate,
    MenuItemCreate,
    OrderUpdate
)


# ---------------------------
# Restaurant Functions
# ---------------------------

def create_restaurant(db: Session, restaurant: RestaurantCreate):
    db_restaurant = Restaurant(name=restaurant.name)
    db.add(db_restaurant)
    db.commit()
    db.refresh(db_restaurant)
    return db_restaurant


def set_restaurant_status(db: Session, restaurant_id: int, is_online: bool):
    db_restaurant = db.query(Restaurant).filter(Restaurant.id == restaurant_id).first()
    if db_restaurant:
        db_restaurant.is_online = is_online
        db.commit()
        db.refresh(db_restaurant)
    return db_restaurant


def get_online_restaurants(db: Session):
    return db.query(Restaurant).filter(Restaurant.is_online == True).all()


# ---------------------------
# Menu Item Functions
# ---------------------------

def add_menu_item(db: Session, item: MenuItemCreate):
    db_item = MenuItem(
        name=item.name,
        price=item.price,
        restaurant_id=item.restaurant_id
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_menu_by_restaurant(db: Session, restaurant_id: int):
    return db.query(MenuItem).filter(MenuItem.restaurant_id == restaurant_id).all()


# ---------------------------
# Order Functions
# ---------------------------

def update_order_status(db: Session, order_id: int, order_update: OrderUpdate):
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if db_order:
        db_order.status = order_update.status
        db_order.agent_id = order_update.agent_id
        db.commit()
        db.refresh(db_order)
    return db_order
