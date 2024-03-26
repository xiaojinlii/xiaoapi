import os
import shutil

import typer
from typer import Typer


def register_command(shell: Typer):

    def copy_project_template(target):
        root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        project_template_path = os.path.join(root_path, "conf", "project_template")

        try:
            shutil.copytree(src=project_template_path, dst=target, dirs_exist_ok=True)
        except FileExistsError:
            print(f"{target} 已经存在，无法自动创建，请删除后，重新执行。")
            return
        except OSError as e:
            print(f"创建失败！message: {e}")
            return

    @shell.command()
    def create_project_files():
        """
        创建项目文件，在当前cwd路径创建项目文件，如果当前路径存在项目文件则会被覆盖
        """
        copy_project_template(os.getcwd())

    @shell.command()
    def create_project(
            name: str = typer.Option(help='项目名称')
    ):
        """
        创建项目
        """
        project_path = os.path.join(os.getcwd(), name)
        if os.path.exists(project_path):
            print(f"{project_path} 已经存在，无法自动创建，请删除后，重新执行。")
            return

        copy_project_template(project_path)
