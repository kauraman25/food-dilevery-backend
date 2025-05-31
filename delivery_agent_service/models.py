from sqlalchemy import Column, Integer, String
from database import Base

class DeliveryOrder(Base):
    __tablename__ = "delivery_orders"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, default="assigned")  # assigned / picked_up / delivered
