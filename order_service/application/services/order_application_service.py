from domain.models.order import Order
from domain.exceptions import OrderNotFoundException


class OrderApplicationService:
    def __init__(self, order_repository=None):  # Inject repository or other dependencies
        self.order_repository = order_repository

    async def create_order(self, create_order_command):
        # Implement order creation logic
        # For example, validate the command, create the order, and save it to the database
        order = Order.create_from_command(create_order_command)
        await self.order_repository.save(order)
        return {
            "order_tracking_id": order.tracking_id,
            "message": "Order successfully created.",
        }

    async def track_order(self, track_order_query):
        # Implement order tracking logic
        order = await self.order_repository.find_by_tracking_id(track_order_query.order_tracking_id)
        if not order:
            raise OrderNotFoundException(f"Order with tracking ID {track_order_query.order_tracking_id} not found.")
        return {
            "order_tracking_id": order.tracking_id,
            "status": order.status,
            "message": "Order status retrieved successfully.",
        }
