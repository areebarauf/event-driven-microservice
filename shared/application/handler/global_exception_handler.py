from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from typing import List
import logging

from shared.application.handler.error_DTO import ErrorDTO

# Setup logger
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)


# Custom ConstraintViolationException
class ConstraintViolationException(Exception):
    def __init__(self, violations: List[str]):
        self.violations = violations

    def __str__(self):
        return "--".join(self.violations)


# Initialize FastAPI app
app = FastAPI()


# Exception Handlers
@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    """
    Handle all unexpected exceptions.
    """
    logger.error("Unexpected error: %s", exc, exc_info=True)
    error_dto = ErrorDTO(code="Internal Server Error", message="Unexpected error!")
    return JSONResponse(status_code=500, content=error_dto.dict())


@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    """
    Handle validation exceptions.
    """
    logger.error("Validation error: %s", exc, exc_info=True)
    error_dto = ErrorDTO(code="Bad Request", message=str(exc))
    return JSONResponse(status_code=400, content=error_dto.dict())


@app.exception_handler(ConstraintViolationException)
async def constraint_violation_exception_handler(
    request: Request, exc: ConstraintViolationException
):
    """
    Handle constraint violations with detailed messages.
    """
    violations = str(exc)
    logger.error("Constraint violations: %s", violations, exc_info=True)
    error_dto = ErrorDTO(code="Bad Request", message=violations)
    return JSONResponse(status_code=400, content=error_dto.dict())


# Example Routes to Demonstrate Exceptions
@app.get("/generic-error")
async def generic_error():
    raise Exception("An unexpected error occurred!")


@app.get("/validation-error")
async def validation_error():
    raise ValidationError(
        [{"loc": ["field"], "msg": "Invalid input data!", "type": "value_error"}],
        model=ErrorDTO,
    )


@app.get("/constraint-violation-error")
async def constraint_violation_error():
    violations = ["Field 'name' is required", "Field 'age' must be positive"]
    raise ConstraintViolationException(violations)
