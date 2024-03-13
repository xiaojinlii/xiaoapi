"""
FastApi 更新文档：https://github.com/tiangolo/fastapi/releases
FastApi Github：https://github.com/tiangolo/fastapi
Typer 官方文档：https://typer.tiangolo.com/
"""

import asyncio
from fastapi import FastAPI
import uvicorn
from starlette.middleware.cors import CORSMiddleware
from application import settings
from application import urls
from starlette.staticfiles import StaticFiles  # 依赖安装：pip install aiofiles
from core.docs import custom_api_docs
from core.exception import register_exception
import typer
from core.event import lifespan
from core.utils import import_modules
from db.migrate import create_tables

shell_app = typer.Typer()


def create_app():
    """
    启动项目

    docs_url：配置交互文档的路由地址，如果禁用则为None，默认为 /docs
    redoc_url： 配置 Redoc 文档的路由地址，如果禁用则为None，默认为 /redoc
    openapi_url：配置接口文件json数据文件路由地址，如果禁用则为None，默认为/openapi.json
    """
    app = FastAPI(
        title=settings.TITLE,
        description=settings.DESCRIPTION,
        version=settings.VERSION,
        lifespan=lifespan,
        docs_url=None,
        redoc_url=None
    )
    import_modules(settings.MIDDLEWARES, "中间件", app=app)
    # 全局异常捕捉处理
    register_exception(app)
    # 跨域解决
    if settings.CORS_ORIGIN_ENABLE:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=settings.ALLOW_ORIGINS,
            allow_credentials=settings.ALLOW_CREDENTIALS,
            allow_methods=settings.ALLOW_METHODS,
            allow_headers=settings.ALLOW_HEADERS
        )
    # 挂在静态目录
    if settings.STATIC_ENABLE:
        app.mount(settings.STATIC_URL, app=StaticFiles(directory=settings.STATIC_ROOT))
    # 引入应用中的路由
    for url in urls.urlpatterns:
        app.include_router(url["ApiRouter"], prefix=url["prefix"], tags=url["tags"])
    # 配置接口文档静态资源
    custom_api_docs(app)
    return app


@shell_app.command()
def run(
        host: str = typer.Option(default='0.0.0.0', help='监听主机IP，默认开放给本网络所有主机'),
        port: int = typer.Option(default=9000, help='监听端口')
):
    """
    启动项目

    factory: 在使用 uvicorn.run() 启动 ASGI 应用程序时，可以通过设置 factory 参数来指定应用程序工厂。
    应用程序工厂是一个返回 ASGI 应用程序实例的可调用对象，它可以在启动时动态创建应用程序实例。
    """
    uvicorn.run(app='main:create_app', host=host, port=port, lifespan="on", factory=True, workers=1)


@shell_app.command()
def init():
    """
    初始化数据库
    需要迁移到数据库的模型 要在application/configs/database_config.py的MIGRATE_MODELS里配置
    """
    asyncio.run(create_tables())
    print("数据库初始化完成！")


if __name__ == '__main__':
    shell_app()
