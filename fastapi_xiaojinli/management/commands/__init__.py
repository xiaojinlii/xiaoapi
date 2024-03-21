import os

from typer import Typer
from fastapi_xiaojinli.core.utils import import_functions


def register_commands(shell: Typer):
    module_dir = os.path.dirname(os.path.abspath(__file__))

    modules = []
    for filename in os.listdir(module_dir):
        if filename.endswith(".py"):
            module_name = filename[:-3]
            if module_name != "__init__":
                module = f"fastapi_xiaojinli.management.commands.{module_name}.register_command"
                modules.append(module)

    import_functions(modules, "commands", shell=shell)
