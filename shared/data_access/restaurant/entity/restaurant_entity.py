from sqlalchemy import Column, String, Boolean, Numeric
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
import uuid

Base = declarative_base()


class RestaurantEntity(Base):
    __tablename__ = "order_restaurant_m_view"
    __table_args__ = {"schema": "restaurant"}

    restaurant_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    restaurant_name = Column(String, nullable=False)
    restaurant_active = Column(Boolean, nullable=False)
    product_name = Column(String, nullable=False)
    product_price = Column(Numeric(precision=10, scale=2), nullable=False)
    product_available = Column(Boolean, nullable=False)

    def __eq__(self, other):
        """
        Compare equality based on restaurant_id and product_id.
        """
        if not isinstance(other, RestaurantEntity):
            return False
        return (
            self.restaurant_id == other.restaurant_id
            and self.product_id == other.product_id
        )

    def __hash__(self):
        """
        Compute hash based on restaurant_id and product_id.
        """
        return hash((self.restaurant_id, self.product_id))
