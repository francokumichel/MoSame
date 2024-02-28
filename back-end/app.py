from src.web import create_app
from pathlib import Path

static_folder = Path(__file__).parent.joinpath("public")

app = create_app(env="production", static_folder=static_folder)
print("Ruta absoluta de la carpeta estática:", static_folder.resolve())

if __name__ == "__main__":
    app.run()
