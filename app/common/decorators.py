import logging
from functools import wraps
from pydantic import ValidationError
from robyn import Response

from app.common.exceptions import BaseExceptionMixin

logger = logging.getLogger(__name__)


def handle_exceptions(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        x_request_id = None
        try:
            request = kwargs.get("request")
            if request and hasattr(request, "headers"):
                x_request_id = getattr(request.headers, "get", lambda key: None)("x-request-id")  # noqa
            response_result = await func(*args, **kwargs)
            if isinstance(response_result, dict):
                response_result.update({"x-request-id": x_request_id})
            return response_result
        except BaseExceptionMixin as exc:
            logger.error(f"{x_request_id if x_request_id else ''} custom error | {exc}", exc_info=True)
            error_message = exc.msg
            Response.status_code = exc.code
            return {"error": error_message, "x-request-id": x_request_id}
        except (ValidationError,) as va_err:
            logger.error(f"{x_request_id if x_request_id else ''} DataValidation error | {va_err}", exc_info=True)
            error_message = [{"field": err["loc"][-1], "message": err["msg"]} for err in va_err.errors()]
            Response.status_code = 422
            return {"error": error_message, "x-request-id": x_request_id}
        except Exception as e:
            logger.error(f"{x_request_id if x_request_id else ''} server error | {e}", exc_info=True)
            error_message = "An error occurred"
            Response.status_code = 500
            return {"error": error_message, "x-request-id": x_request_id}

    return wrapper
