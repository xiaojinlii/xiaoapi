import typer

from ..management.commands import register_manage_commands, register_admin_commands

manage_commands = typer.Typer(no_args_is_help=True, add_completion=False)
register_manage_commands(manage_commands)


admin_commands = typer.Typer(no_args_is_help=True, add_completion=False)
register_admin_commands(admin_commands)

manage_commands.add_typer(admin_commands, name="admin", help="admin命令")
