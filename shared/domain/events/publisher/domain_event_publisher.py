from abc import ABC, abstractmethod
from typing import Generic

from shared.domain.events.domain_event import T


class DomainEventPublisher(ABC, Generic[T]):
    """
    Abstract base class for publishing domain events.
    """

    @abstractmethod
    def publish(self, domain_event: T) -> None:
        """
        Publish the given domain event.
        :param domain_event: The domain event to publish
        """
        pass
