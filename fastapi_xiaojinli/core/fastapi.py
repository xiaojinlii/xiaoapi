from fastapi import FastAPI


def get_fastapi_application():
    """
    启动项目

    docs_url：配置交互文档的路由地址，如果禁用则为None，默认为 /docs
    redoc_url： 配置 Redoc 文档的路由地址，如果禁用则为None，默认为 /redoc
    openapi_url：配置接口文件json数据文件路由地址，如果禁用则为None，默认为/openapi.json
    """
    application = FastAPI(
        # title=settings.TITLE,
        # description=settings.DESCRIPTION,
        # version=settings.VERSION,
        # lifespan=lifespan,
        # docs_url=None,
        # redoc_url=None
    )

    # # 注册中间件
    # register_middlewares(application)
    # # 全局异常捕捉处理
    # register_exception(application)
    # # 注册路由
    # register_routes(application)
    # # 配置接口文档静态资源
    # custom_api_docs(application)
    # # 挂载文件目录
    # register_mounting(application)

    return application
