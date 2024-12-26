import asyncio

from robyn import SubRouter, Request

from app.api.user import service
from app.api.user.schemas import BodyReq
from app.common.decorators import handle_exceptions
from app.common.exceptions import NotFoundError

user_router = SubRouter(__name__, prefix="/user")


@user_router.get("")
@handle_exceptions
async def hello(request: Request):
    await asyncio.sleep(1)
    return {"hello": "world"}


@user_router.post("/:id")
@handle_exceptions
async def world(request: Request):
    user = await service.fetch_user(int(request.path_params.get("id")))
    if not user:
        raise NotFoundError()
    return {"name": user.account}


@user_router.post("")
@handle_exceptions
async def post(request: Request):
    req = BodyReq(**request.json())
    return req.model_dump()
