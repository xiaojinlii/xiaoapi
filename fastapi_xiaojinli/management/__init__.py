import typer

from fastapi_xiaojinli.management.commands import register_commands

shell = typer.Typer()


register_commands(shell)
