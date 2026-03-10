from pathlib import Path
import os


APP_NAME = "HordaRPG"


class Paths:

    def __init__(self):
        self.base_dir = self.get_user_data_dir()

        self.grids = self.base_dir / "grids"
        self.characters = self.base_dir / "characters"
        self.books = self.base_dir / "books"
        self.assets = self.base_dir / "assets"
        self.config = self.base_dir / "config"
        self.logs = self.base_dir / "logs"

        self.create_directories()

    def get_user_data_dir(self):
        """
        Retorna o diretório de dados do usuário dependendo do sistema.
        """

        home = Path.home()

        if os.name == "nt":  # Windows
            base = Path(os.getenv("LOCALAPPDATA")) / APP_NAME
        else:  # Linux / Mac
            base = home / f".{APP_NAME.lower()}"

        return base

    def create_directories(self):
        """
        Cria as pastas caso não existam.
        """

        directories = [
            self.base_dir,
            self.grids,
            self.characters,
            self.books,
            self.assets,
            self.config,
            self.logs
        ]

        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)


paths = Paths()