import json
import os


class FileManager:

    def __init__(self, paths, logger):
        """
        Gerenciador global de arquivos do sistema.
        """

        self.paths = paths
        self.logger = logger


    def save_json(self, directory, filename, data):
        """
        Salva um arquivo JSON.
        """

        file_path = os.path.join(directory, filename)

        try:
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)

            self.logger.info(f"Arquivo salvo: {file_path}")

        except Exception as error:
            self.logger.error(f"Erro ao salvar arquivo: {error}")


    def load_json(self, directory, filename):
        """
        Carrega um arquivo JSON.
        """

        file_path = os.path.join(directory, filename)

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            self.logger.info(f"Arquivo carregado: {file_path}")

            return data

        except Exception as error:
            self.logger.error(f"Erro ao carregar arquivo: {error}")
            return None


    def list_files(self, directory):
        """
        Lista arquivos dentro de um diretório.
        """

        try:
            files = os.listdir(directory)
            return files

        except Exception as error:
            self.logger.error(f"Erro ao listar arquivos: {error}")
            return []


    def delete_file(self, directory, filename):
        """
        Deleta um arquivo.
        """

        file_path = os.path.join(directory, filename)

        try:
            os.remove(file_path)

            self.logger.info(f"Arquivo removido: {file_path}")

        except Exception as error:
            self.logger.error(f"Erro ao remover arquivo: {error}")