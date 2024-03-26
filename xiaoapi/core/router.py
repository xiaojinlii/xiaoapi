import os
from fastapi import FastAPI
from .utils import import_functions


def register_routes(app: FastAPI):
    """
    注册路由
    """

    routers_module = os.environ.get('FASTAPI_ROUTES_MODULE')
    if not routers_module:
        raise ValueError(
            "Requested routers, but routers are not configured. "
            "You must define the environment variable FASTAPI_ROUTES_MODULE "
            "before accessing settings."
        )

    import_functions([routers_module], "router", app=app)
