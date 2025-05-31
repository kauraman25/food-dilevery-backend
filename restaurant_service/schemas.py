from pydantic import BaseModel
from typing import Optional, List


# -----------------------------
# Restaurant Schemas
# -----------------------------

class RestaurantBase(BaseModel):
    name: str

class RestaurantCreate(RestaurantBase):
    pass

class RestaurantOut(RestaurantBase):
    id: int
    is_online: bool

    class Config:
        from_attributes = True


# -----------------------------
# Menu Item Schemas
# -----------------------------

class MenuItemBase(BaseModel):
    name: str
    price: int

class MenuItemCreate(MenuItemBase):
    restaurant_id: int

class MenuItemOut(MenuItemBase):
    id: int
    restaurant_id: int

    class Config:
        from_attributes = True


# -----------------------------
# Order Schemas
# -----------------------------

class OrderBase(BaseModel):
    restaurant_id: int

class OrderUpdate(BaseModel):
    status: str  # accepted / rejected / preparing
    agent_id: Optional[int] = None  # set only if accepted

class OrderOut(BaseModel):
    id: int
    restaurant_id: int
    status: str
    agent_id: Optional[int] = None

    class Config:
        from_attributes = True
