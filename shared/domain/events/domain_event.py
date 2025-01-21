from abc import ABC
from typing import Generic, TypeVar

# Define a type variable for the entity type
T = TypeVar("T")


class DomainEvent(ABC, Generic[T]):
    """
    Base class for domain events.
    Marks a class as a domain event and associates it with the entity type
    that will fire the event.

    Example: OrderCreatedEvent will set the generic type as Order,
    indicating the event originated from the Order entity.
    """

    pass
