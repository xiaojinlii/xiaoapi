import typer
import uvicorn
from typer import Typer

from ...conf import settings


def register_command(shell: Typer):

    @shell.command()
    def run_server(
            host: str = typer.Option(default=settings.HOST, help='监听主机IP，默认开放给本网络所有主机'),
            port: int = typer.Option(default=settings.PORT, help='监听端口'),
            workers: int = typer.Option(default=settings.WORKERS, help='工作进程数')
    ):
        """
        启动项目

        factory: 在使用 uvicorn.run() 启动 ASGI 应用程序时，可以通过设置 factory 参数来指定应用程序工厂。
        应用程序工厂是一个返回 ASGI 应用程序实例的可调用对象，它可以在启动时动态创建应用程序实例。
        """
        uvicorn.run(app='fastapi_xiaojinli:get_fastapi_application', host=host, port=port, lifespan="on", factory=True, workers=workers)
