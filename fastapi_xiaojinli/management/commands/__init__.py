import os

from typer import Typer
from ...core import import_functions

MODULE_TEMPLATE = "xiaoapi.management.commands.{module}.register_command"

ignore_file = [
    "__init__.py"
]

admin_commands = [
    "createproject",
]


def register_admin_commands(shell: Typer):
    modules = [
        MODULE_TEMPLATE.format(module=module) for module in admin_commands
    ]
    import_functions(modules, "commands", shell=shell)


def register_manage_commands(shell: Typer):
    module_dir = os.path.dirname(os.path.abspath(__file__))

    modules = []
    for filename in os.listdir(module_dir):
        if filename.endswith(".py") and filename not in ignore_file:
            module_name = filename[:-3]
            if module_name not in admin_commands:
                module = MODULE_TEMPLATE.format(module=module_name)
                modules.append(module)

    import_functions(modules, "commands", shell=shell)



