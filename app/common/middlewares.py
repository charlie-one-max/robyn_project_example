import logging
from uuid import uuid4

from robyn import Request, Response, Robyn

logger = logging.getLogger(__name__)


def register_middleware(app: Robyn):
    @app.before_request()
    async def hello_before_request(request: Request):
        request_id = str(uuid4())
        request.headers["x-request-id"] = request_id
        logger.info(f"{request_id: <6} | {request.ip_addr: <6} | {request.url.path: <6} | {request.method: <6}")
        return request

    @app.after_request()
    async def hello_after_request(response: Response):
        response.headers["x-api-version"] = "0.1.1"
        response.headers["server"] = "Actix"
        return response
