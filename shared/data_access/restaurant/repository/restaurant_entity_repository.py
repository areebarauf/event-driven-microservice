from sqlalchemy.orm import Session
from sqlalchemy import and_
from typing import List, Optional
from uuid import UUID
from restaurant.entity.restaurant_entity import RestaurantEntity
from shared.data_access.restaurant.entity.resurant_entity_id import RestaurantEntityId


class RestaurantRepository:
    def __init__(self, session: Session):
        self.session = session

    def find_by_restaurant_id_and_product_ids(
        self, restaurant_entity_id: RestaurantEntityId, product_ids: List[UUID]
    ) -> Optional[List[RestaurantEntity]]:
        """
        Retrieve RestaurantEntity records by a composite key and a list of product_ids.
        """
        query = self.session.query(RestaurantEntity).filter(
            and_(
                RestaurantEntity.restaurant_id == restaurant_entity_id.restaurant_id,
                RestaurantEntity.product_id.in_(product_ids),
            )
        )

        result = query.all()
        return result if result else None
