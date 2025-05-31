from pydantic import BaseModel
from typing import Optional, List
from enum import Enum


# Rating type enum for validation
class RatingType(str, Enum):
    restaurant = "restaurant"
    agent = "agent"


# -------------------------------
# User schema
# -------------------------------
class UserBase(BaseModel):
    name: str

class UserCreate(UserBase):
    pass

class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True


# -------------------------------
# Order schema
# -------------------------------
class OrderBase(BaseModel):
    restaurant_id: int
    items: List[int]  # List of menu item IDs

class OrderCreate(OrderBase):
    user_id: int

class OrderOut(BaseModel):
    id: int
    user_id: int
    restaurant_id: int
    agent_id: Optional[int]
    status: str

    class Config:
        from_attributes = True


# -------------------------------
# Rating schema
# -------------------------------
class RatingCreate(BaseModel):
    user_id: int
    order_id: int
    rating_for_type: RatingType  # Enum
    rating_value: int  # 1 to 5

class RatingOut(BaseModel):
    id: int
    user_id: int
    order_id: int
    rating_for_type: RatingType
    rating_value: int

    class Config:
        from_attributes = True
