from fastapi import APIRouter
from starlette.responses import JSONResponse


app = APIRouter()


@app.get("/test", summary="测试接口")
def test():
    return JSONResponse(content="hello world!")
