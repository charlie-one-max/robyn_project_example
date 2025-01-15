import asyncio

from robyn import SubRouter, Request

from app.api.user import service
from app.api.user.schemas import GetReq, BodyReqEg
from app.common.decorators import handle_exceptions
from app.common.exceptions import NotFoundError

user_router = SubRouter(__name__, prefix="/user")


@user_router.get("/health")
@handle_exceptions
async def hello(request: Request):
    await asyncio.sleep(1)
    return {"hello": "world"}


@user_router.get("/detail/:id")
@handle_exceptions
async def world(request: Request):
    # 路径参数取数据
    user = await service.fetch_user(int(request.path_params.get("id")))
    if not user:
        raise NotFoundError()
    return {"name": user.account}


@user_router.post("")
@handle_exceptions
async def post(request: Request, body: BodyReqEg):
    # 请求体取数据
    print(request.body, type(request.body), request.json(), type(request.json()))
    return request.body  # 字符串类型


@user_router.get("/query_params")
@handle_exceptions
async def get_query_params(request: Request, query_params: GetReq):
    # 查询参数取数据
    print(request.query_params, type(request.query_params))
    return request.query_params  # QueryParams类型
