class DomainException(Exception):
    """
    Base exception class for domain-related errors.
    """

    def __init__(self, message: str, cause: Exception = None):
        super().__init__(message)
        self.cause = cause
