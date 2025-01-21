from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, UUID4
from typing import Any
from application.services.order_application_service import OrderApplicationService
from api.schemas import (
    CreateOrderCommand,
    CreateOrderResponse,
    TrackOrderQuery,
    TrackOrderResponse,
)

router = APIRouter(
    prefix="/orders",
    tags=["orders"],
    responses={404: {"description": "Not Found"}},
)


# Dependency Injection for OrderApplicationService
def get_order_application_service() -> OrderApplicationService:
    return OrderApplicationService()


@router.post("/", response_model=CreateOrderResponse)
async def create_order(
    create_order_command: CreateOrderCommand,
    service: OrderApplicationService = Depends(get_order_application_service),
):
    """
    Create a new order.
    """
    try:
        response = await service.create_order(create_order_command)
        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{tracking_id}", response_model=TrackOrderResponse)
async def get_order_by_tracking_id(
    tracking_id: UUID4,
    service: OrderApplicationService = Depends(get_order_application_service),
):
    """
    Get order details by tracking ID.
    """
    try:
        query = TrackOrderQuery(order_tracking_id=tracking_id)
        response = await service.track_order(query)
        return response
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
