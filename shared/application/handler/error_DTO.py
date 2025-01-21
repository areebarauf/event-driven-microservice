from dataclasses import dataclass


@dataclass(frozen=True)
class ErrorDTO:
    code: str
    message: str
