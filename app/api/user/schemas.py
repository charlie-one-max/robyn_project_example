from pydantic import BaseModel
from typing import Literal


class BodyReq(BaseModel):
    name: str
    age: int
    status: Literal["error", "success"]

    class Config:
        from_attributes = True
        validate_assignment = True
