import uuid


class RestaurantEntityId:
    def __init__(self, restaurant_id: uuid.UUID, product_id: uuid.UUID):
        self.restaurant_id = restaurant_id
        self.product_id = product_id

    def __eq__(self, other):
        if not isinstance(other, RestaurantEntityId):
            return False
        return (
            self.restaurant_id == other.restaurant_id
            and self.product_id == other.product_id
        )

    def __hash__(self):
        return hash((self.restaurant_id, self.product_id))
