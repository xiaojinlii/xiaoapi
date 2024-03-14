from fastapi import FastAPI

from modules.quickstart.routes import route as quickstart_route


def register_routes(app: FastAPI):
    """
    注册路由
    """

    app.include_router(quickstart_route, prefix="/quickstart", tags=["快速开始"])
