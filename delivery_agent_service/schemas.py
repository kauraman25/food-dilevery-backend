from pydantic import BaseModel

class DeliveryUpdate(BaseModel):
    status: str  # picked_up / delivered

class DeliveryOut(BaseModel):
    id: int
    status: str

    class Config:
        from_attributes = True
