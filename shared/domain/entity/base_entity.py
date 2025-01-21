from typing import Generic, TypeVar

# Define a type variable for the ID type
ID = TypeVar("ID")


class BaseEntity(Generic[ID]):
    """
    Base class for entities with a unique identifier.
    Provides basic equality and hashing functionality.
    """

    def __init__(self, entity_id: ID = None):
        self.id = entity_id

    def get_id(self) -> ID:
        """
        Get the entity's ID.
        """
        return self.id

    def set_id(self, entity_id: ID) -> None:
        """
        Set the entity's ID.
        """
        self.id = entity_id

    def __eq__(self, other):
        """
        Check equality based on the ID.
        """
        if not isinstance(other, BaseEntity):
            return False
        return self.id == other.id

    def __hash__(self):
        """
        Compute a hash based on the ID.
        """
        return hash(self.id)
