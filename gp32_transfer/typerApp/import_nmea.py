import typer
from ..utils.serial_util import save_gps_to_gpx
import os
from typing import Optional

app = typer.Typer()


@app.command()
def save_all(
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
    typer.echo("\n" + "-" * 30)
    typer.echo("Press 'Sauve WP/RTE -> PC?'")
    typer.echo("and press 'Poursuivre'")

    save_gps_to_gpx(filename=filename, nmea_flag=nmea, csv_flag=csv)


if __name__ == "__main__":
    app()
