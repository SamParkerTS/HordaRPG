import os
from pathlib import Path


class Paths:

    def __init__(self):

        # Diretório base do projeto
        self.base_dir = Path.home() / "HordaRPG"

        # Subdiretórios
        self.config_dir = self.base_dir / "config"
        self.grids_dir = self.base_dir / "grids"
        self.characters_dir = self.base_dir / "characters"
        self.books_dir = self.base_dir / "books"
        self.assets_dir = self.base_dir / "assets"
        self.logs_dir = self.base_dir / "logs"

        # Criar diretórios
        self.create_directories()

    def create_directories(self):

        directories = [
            self.base_dir,
            self.config_dir,
            self.grids_dir,
            self.characters_dir,
            self.books_dir,
            self.assets_dir,
            self.logs_dir
        ]

        for directory in directories:
            os.makedirs(directory, exist_ok=True)