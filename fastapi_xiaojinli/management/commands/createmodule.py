import os
import shutil

import typer
from typer import Typer


def register_command(shell: Typer):

    def copy_module_template(target):
        root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        module_template_path = os.path.join(root_path, "conf", "module_template")

        try:
            shutil.copytree(src=module_template_path, dst=target, dirs_exist_ok=True)
        except FileExistsError:
            print(f"{target} 已经存在，无法自动创建，请删除后，重新执行。")
            return
        except OSError as e:
            print(f"创建失败！message: {e}")
            return

    @shell.command()
    def create_module(
            name: str = typer.Option(help='模块名称')
    ):
        """
        创建模块
        """
        from fastapi_xiaojinli.conf import settings

        module_path = os.path.join(settings.BASE_DIR, "modules", name)
        if os.path.exists(module_path):
            print(f"{module_path} 已经存在，无法自动创建，请删除后，重新执行。")
            return

        copy_module_template(module_path)
        print(f"模块创建成功！module_path: {module_path}")
