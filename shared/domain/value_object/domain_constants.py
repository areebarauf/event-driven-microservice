class DomainConstants:
    """
    DomainConstants holds application-wide constants.
    This class is not meant to be instantiated.
    It uses class level attributes which are equivalent to Java static constants.
    """

    TIMEZONE = "UTC"

    def __new__(cls, *args, **kwargs):
        raise TypeError(f"{cls.__name__} is a utility class and cannot be instantiated.")
