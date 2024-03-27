import typer
import importlib

from ..management.commands import register_manage_commands, register_admin_commands

manage_typer = typer.Typer(no_args_is_help=True, add_completion=False)
register_manage_commands(manage_typer)


admin_typer = typer.Typer(no_args_is_help=True, add_completion=False)
register_admin_commands(admin_typer)

# manage_commands.add_typer(admin_typer, name="admin", help="admin命令")


extension_typer = [
    {
        "module": "xiaoapi.management.admin_typer",
        "name": "admin",
        "help": "admin命令"
    },
    {
        "module": "xiaoapi_sqlalchemy.commands.sqlalchemy_typer",
        "name": "sqlalchemy",
        "help": "sqlalchemy命令"
    }
]

for ext in extension_typer:
    try:
        module = ext["module"]
        module_name = module[0:module.rindex(".")]
        module_attr = module[module.rindex(".") + 1:]

        module_pag = importlib.import_module(module_name)
        sub_typer = getattr(module_pag, module_attr)
        manage_typer.add_typer(sub_typer, name=ext["name"], help=ext["help"])
    except ModuleNotFoundError as e:
        continue
    except AttributeError as e:
        continue
