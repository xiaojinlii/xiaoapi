from fastapi import APIRouter
from fastapi_xiaojinli.response import SuccessResponse, ErrorResponse

from . import schemas, models, crud
from .dependencies import *

router = APIRouter()


@router.get("/test", summary="测试接口")
def test():
    return SuccessResponse(data="hello world!")
