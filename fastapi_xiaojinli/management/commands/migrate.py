import asyncio

from typer import Typer


def register_command(shell: Typer):
    @shell.command()
    def create_tables():
        """
        初始化数据库
        需要迁移到数据库的模型 要在application/configs/database_config.py的MIGRATE_MODELS里配置
        """
        from fastapi_xiaojinli.db.migrate import create_tables as migrate_create_tables
        asyncio.run(migrate_create_tables())
        print("数据库表结构创建成功！")
