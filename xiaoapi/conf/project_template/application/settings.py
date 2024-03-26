"""
FastAPI settings for project.
"""

import os
from pathlib import Path

# 项目根目录
BASE_DIR = Path(__file__).resolve().parent.parent

# 注意：不要在生产中打开调试运行!
DEBUG = False

####################
# PROJECT SETTINGS #
####################
TITLE = "FastAPI Framework"
DESCRIPTION = "基于FastAPI的Web框架"
VERSION = "0.0.1"


############
# UVICORN #
############
# 监听主机IP，默认开放给本网络所有主机
HOST = "0.0.0.0"
# 监听端口
PORT = 9000
# 工作进程数
WORKERS = 1


########
# CORS #
########
# 跨域解决
# 详细解释：https://cloud.tencent.com/developer/article/1886114
# 官方文档：https://fastapi.tiangolo.com/tutorial/cors/
# 是否启用跨域
CORS_ORIGIN_ENABLE = True
# 只允许访问的域名列表，* 代表所有
ALLOW_ORIGINS = ["*"]
# 是否支持携带 cookie
ALLOW_CREDENTIALS = True
# 设置允许跨域的http方法，比如 get、post、put等。
ALLOW_METHODS = ["*"]
# 允许携带的headers，可以用来鉴别来源等作用。
ALLOW_HEADERS = ["*"]


############
# MOUNTING #
############
MEDIA_ENABLE = False
# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
# URL that handles the media served from MEDIA_ROOT.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = "/media"

STATIC_ENABLE = False
# Absolute path to the directory static files should be collected to.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
# URL that handles the static files served from STATIC_ROOT.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = "/static"


##############
# MIDDLEWARE #
##############
# List of middleware to use. Order is important; in the request phase, these
# middleware will be applied in the order given, and in the response
# phase the middleware will be applied in reverse order.
MIDDLEWARES = [
    "xiaoapi.middleware.register_request_log_middleware",
]


############
# LIFESPAN #
############
EVENTS = [
    # "xiaoapi.extensions.redis.connect_redis",
]


#############
# DATABASES #
#############

# 数据库配置项
# 连接引擎官方文档：https://docs.sqlalchemy.org/en/20/core/engines.html
# mysql配置说明：mysql+asyncmy://数据库用户名:数据库密码@数据库地址:数据库端口/数据库名称，需安装asyncmy
# sqlite配置说明：sqlite+aiosqlite:///数据库路径，需安装aiosqlite
SQLALCHEMY_DATABASE_URL = f"sqlite+aiosqlite:///{BASE_DIR}/db.sqlite3"

# 数据库迁移
# 会将MIGRATE_MODELS里所有的model迁移到数据库表结构
MIGRATE_MODELS = [
    # "modules.quickstart.models"
]
