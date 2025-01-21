from pydantic import BaseModel, UUID4
from typing import Optional


class CreateOrderCommand(BaseModel):
    customer_id: UUID4
    restaurant_id: UUID4
    items: list[dict]  # Add specific schema for items if necessary
    price: float


class CreateOrderResponse(BaseModel):
    order_tracking_id: UUID4
    message: str


class TrackOrderQuery(BaseModel):
    order_tracking_id: UUID4


class TrackOrderResponse(BaseModel):
    order_tracking_id: UUID4
    status: str
    message: Optional[str]
