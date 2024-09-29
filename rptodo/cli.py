from typing import Optional
import typer
from rptodo import __app_name__, __version__

app = typer.Typer()

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()

@app.callback()

def main(
    version: Optional(bool) = typer.opcional( # type: ignore
        None,
        "--version",
        "-v",
        help = "Mostrar a versão do app",
        callback= _version_callback,
        is_eager = True,

    )
) -> None:
    return