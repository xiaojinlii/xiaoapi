"""
Default FastAPI settings. Override these with settings in the module pointed to
by the XIAOAPI_SETTINGS_MODULE environment variable.
"""

import os
from pathlib import Path

# Package根目录
PACKAGE_DIR = Path(__file__).resolve().parent.parent

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
SWAGGER_UI_ENABLE = True
# docs ui assets root
DOCS_URL = "/docs"
DOCS_ROOT = os.path.join(PACKAGE_DIR, "static")

MEDIA_ENABLE = False
# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ""
# URL that handles the media served from MEDIA_ROOT.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ""

STATIC_ENABLE = False
# Absolute path to the directory static files should be collected to.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = None
# URL that handles the static files served from STATIC_ROOT.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = None


##############
# MIDDLEWARE #
##############
# List of middleware to use. Order is important; in the request phase, these
# middleware will be applied in the order given, and in the response
# phase the middleware will be applied in reverse order.
MIDDLEWARE = []


############
# LIFESPAN #
############
EVENTS = []


#############
# DATABASES #
#############
# 数据库配置项
# 连接引擎官方文档：https://docs.sqlalchemy.org/en/20/core/engines.html
# mysql配置说明：mysql+asyncmy://数据库用户名:数据库密码@数据库地址:数据库端口/数据库名称，需安装asyncmy
# sqlite配置说明：sqlite+aiosqlite:///数据库路径，需安装aiosqlite
SQLALCHEMY_DATABASE_URL = ""
# 数据库迁移
# 会将MIGRATE_MODELS里所有的model迁移到数据库表结构
MIGRATE_MODELS = []


##############
# EXTENSIONS #
##############
# Redis 数据库配置
# 格式："redis://:密码@地址:端口/数据库名称"
REDIS_DB_ENABLE = False
REDIS_DB_URL = "redis://:123456@177.8.0.5:6379/1"

# MongoDB 数据库配置
# 格式：mongodb://用户名:密码@地址:端口/?authSource=数据库名称
MONGO_DB_ENABLE = False
MONGO_DB_NAME = "fastapi"
MONGO_DB_URL = f"mongodb://admin:123456@177.8.0.6:27017/?authSource={MONGO_DB_NAME}"

# Elasticsearch 配置
ELASTICSEARCH_ENABLE = False
ELASTICSEARCH_USER = "elastic"
ELASTICSEARCH_PASSWORD = "gv3Z0Nnti2gdApgzLmUN"
ELASTICSEARCH_URL = "http://127.0.0.1:9200"
