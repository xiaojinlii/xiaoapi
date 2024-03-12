from apps.quickstart.urls import app as quickstart_app


# 引入应用中的路由
urlpatterns = [
    {"ApiRouter": quickstart_app, "prefix": "/quickstart", "tags": ["快速开始"]},
]
