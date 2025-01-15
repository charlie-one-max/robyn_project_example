from robyn.robyn import QueryParams
from robyn.types import Body


class PaginationItemReq(QueryParams):
    page: int
    page_size: int


class PaginationItemSchema(PaginationItemReq):
    total_count: int


class GetReq(PaginationItemReq):
    name: str


class BodyReqEg(Body):
    name: str
    age: int
