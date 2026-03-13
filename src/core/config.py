import json
import os
from core.constants import DEFAULT_LANGUAGE, DEFAULT_THEME


class Config:
    def __init__(self, paths):
        """
        Sistema de configuração do software.
        """

        self.paths = paths
        self.config_file = os.path.join(self.paths.config_dir, "config.json")

        self.data = {}

        self.load()

    def load(self):
        """
        Carrega configurações ou cria padrão.
        """

        if not os.path.exists(self.config_file):
            self.create_default()

        with open(self.config_file, "r", encoding="utf-8") as file:
            self.data = json.load(file)

    def create_default(self):
        """
        Cria arquivo de configuração padrão.
        """

        default_config = {
            "language": DEFAULT_LANGUAGE,
            "theme": DEFAULT_THEME,
            "auto_update": True
        }

        with open(self.config_file, "w", encoding="utf-8") as file:
            json.dump(default_config, file, indent=4)

    def save(self):
        """
        Salva alterações na configuração.
        """

        with open(self.config_file, "w", encoding="utf-8") as file:
            json.dump(self.data, file, indent=4)