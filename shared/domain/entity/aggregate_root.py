from shared.domain.entity.base_entity import ID, BaseEntity


class AggregateRoot(BaseEntity[ID]):
    """
    Marker class to distinguish aggregate root objects from base entities.
    Inherits functionality from BaseEntity.
    """

    pass
