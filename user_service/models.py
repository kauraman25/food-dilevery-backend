from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from database import Base
import enum

# Optional: Enum for rating type
class RatingType(str, enum.Enum):
    restaurant = "restaurant"
    agent = "agent"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    # Relationships
    orders = relationship("Order", back_populates="user")
    ratings = relationship("Rating", back_populates="user")


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    restaurant_id = Column(Integer, nullable=False)
    agent_id = Column(Integer, nullable=True)  # Assigned later
    status = Column(String, default="placed")

    # Relationships
    user = relationship("User", back_populates="orders")
    rating = relationship("Rating", back_populates="order", uselist=False)


class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    rating_for_type = Column(Enum(RatingType), nullable=False)  # 'restaurant' or 'agent'
    rating_value = Column(Integer, nullable=False)  # 1 to 5

    # Relationships
    user = relationship("User", back_populates="ratings")
    order = relationship("Order", back_populates="rating")
