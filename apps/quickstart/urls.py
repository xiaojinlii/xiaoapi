from fastapi import APIRouter
from starlette.responses import JSONResponse
from core.response import SuccessResponse

app = APIRouter()


@app.get("/test", summary="测试接口")
def test():
    return SuccessResponse(data="hello world!")
