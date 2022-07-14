from distutils.command.config import config
from . import app


@app.route("/")
def inicio():
    return (f"La ruta del archivo de datos es:"
            f"{app.config['RUTA']}<br>Secret Key: "
            f"{app.config['SECRET_KEY']}")
