import typer

from fastapi_xiaojinli.management.commands import register_manage_commands, register_admin_commands

manage_commands = typer.Typer()
register_manage_commands(manage_commands)


admin_commands = typer.Typer()
register_admin_commands(admin_commands)

manage_commands.add_typer(admin_commands, name="admin", help="admin命令")
