import os


"""项目根目录"""
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
"""fastapi_xiaojinli包根目录"""
PACKAGE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


"""安全警告: 不要在生产中打开调试运行!"""
DEBUG = False


"""项目配置"""
TITLE = "FastAPI Framework"
DESCRIPTION = "基于FastAPI的Web框架"
VERSION = "0.0.1"


"""
临时文件目录
TEMP_DIR：临时文件目录绝对路径
"""
TEMP_DIR = os.path.join(BASE_DIR, "temp")


"""
挂载静态目录，并添加路由访问，此路由不会在接口文档中显示
STATIC_ENABLE：是否启用静态目录访问
STATIC_URL：路由访问
STATIC_ROOT：静态文件目录绝对路径
官方文档：https://fastapi.tiangolo.com/tutorial/static-files/
"""
STATIC_ENABLE = True
STATIC_URL = "/static"
STATIC_DIR = "static"
STATIC_ROOT = os.path.join(BASE_DIR, STATIC_DIR)

# docs ui assets root
DOCS_URL = "/docs"
DOCS_ROOT = os.path.join(PACKAGE_DIR, STATIC_DIR)


"""
跨域解决
详细解释：https://cloud.tencent.com/developer/article/1886114
官方文档：https://fastapi.tiangolo.com/tutorial/cors/
"""
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


"""uvicorn"""
HOST = "0.0.0.0"  # 监听主机IP，默认开放给本网络所有主机
PORT = 9000  # 监听端口
WORKERS = 1  # 工作进程数


"""
中间件配置
"""
MIDDLEWARES = [
    "middleware.request_log_middleware.register_request_log_middleware",
]


"""
全局事件配置
"""
EVENTS = [

]


"""
数据库配置项
连接引擎官方文档：https://docs.sqlalchemy.org/en/20/core/engines.html
mysql配置说明：mysql+asyncmy://数据库用户名:数据库密码@数据库地址:数据库端口/数据库名称，需安装asyncmy
sqlite配置说明：sqlite+aiosqlite:///数据库路径，需安装aiosqlite
"""
SQLALCHEMY_DATABASE_URL = f"sqlite+aiosqlite:///{BASE_DIR}/info.db"


"""
数据库迁移
会将MIGRATE_MODELS里所有的model迁移到数据库表结构
"""
MIGRATE_MODELS = [
    "modules.quickstart.models.*"
]


"""
Redis 数据库配置
格式："redis://:密码@地址:端口/数据库名称"
"""
REDIS_DB_ENABLE = False
REDIS_DB_URL = "redis://:123456@177.8.0.5:6379/1"

"""
MongoDB 数据库配置
格式：mongodb://用户名:密码@地址:端口/?authSource=数据库名称
"""
MONGO_DB_ENABLE = False
MONGO_DB_NAME = "fastapi"
MONGO_DB_URL = f"mongodb://admin:123456@177.8.0.6:27017/?authSource={MONGO_DB_NAME}"


"""
Elasticsearch 配置
"""
ELASTICSEARCH_ENABLE = False
ELASTICSEARCH_USER = "elastic"
ELASTICSEARCH_PASSWORD = "gv3Z0Nnti2gdApgzLmUN"
ELASTICSEARCH_URL = "http://127.0.0.1:9200"
