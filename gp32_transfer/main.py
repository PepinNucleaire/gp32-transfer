import typer
import os
import time
from .utils.serial_util import save_gps_to_gpx
from typing import Optional
from .utils.serial_util import from_gpx_to_gps
from pathlib import Path

help = "App used to import or export gpx with a Furuno GP32 gps"
app = typer.Typer(help=help)


@app.command("import")
def import_from_gps(
    filename: str = typer.Argument(..., help="Specify filename for gpx export"),
    output_dir: Optional[str] = typer.Argument(None, help="Specify output directory"),
    nmea: Optional[bool] = typer.Option(False, help="Get raw NMEA file"),
    csv: Optional[bool] = typer.Option(False, help="Get csv of waypoints"),
):
    """
    Import gps waypoints from GP32 to gpx
    """
    if output_dir:
        filename = os.path.join(output_dir, filename)
    else:
        output_dir = "here"
    typer.secho(f"File(s) will be exported to {output_dir}", fg=typer.colors.MAGENTA)
    time.sleep(1)

    typer.secho("\n" + "-" * 30 + "\n")

    typer.secho("Press 'Sauve WP/RTE -> PC?'", fg=typer.colors.BRIGHT_YELLOW)
    typer.secho("and press 'Poursuivre'", fg=typer.colors.BRIGHT_YELLOW)

    typer.secho("\n" + "-" * 30 + "\n")
    save_gps_to_gpx(filename=filename, nmea_flag=nmea, csv_flag=csv)


@app.command("export")
def export_to_gps(gpx_file: Path = typer.Argument(..., help="gpx file to upload")):
    """
    Export gps waypoints from gpx to GP32
    """
    if gpx_file is None:
        typer.echo("No file entered")
        raise typer.Abort()
    if gpx_file.is_file():
        typer.echo("\n" + "-" * 30)
        typer.echo(f"File {gpx_file} will be processed")
    elif not gpx_file.exists():
        typer.echo("The file doesn't exist")
        raise typer.Abort()

    typer.echo("\n" + "-" * 30)
    typer.echo("Connection to GP32 is good")
    typer.echo("Press 'Charge WP/RTE <- PC?'")
    typer.echo("and press 'Poursuivre'")

    typer.echo("\n" + "-" * 30)
    flag_start = typer.confirm("Is GP32 ready to receive data ?", default=True)
    if flag_start:
        from_gpx_to_gps(gpx_file)

    typer.echo("\n" + "-" * 30)
    typer.echo("End of program")
    raise typer.Exit()


# def main():
#     typer.echo("Hello World")


if __name__ == "__main__":
    app()
