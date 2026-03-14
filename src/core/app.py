import sys

from PySide6.QtWidgets import QApplication

from core.paths import Paths
from core.config import Config
from core.logger import Logger
from core.file_manager import FileManager

from ui.main_window import MainWindow


class Application:

    def __init__(self):

        # Inicialização do núcleo
        self.paths = Paths()

        self.config = Config(self.paths)

        self.logger = Logger(self.paths).get_logger()

        self.file_manager = FileManager(self.paths, self.logger)

        # Inicialização da interface
        self.qt_app = QApplication(sys.argv)

        self.main_window = MainWindow()

        self.logger.info("Aplicação inicializada.")

    def run(self):

        """
        Executa a aplicação.
        """

        self.logger.info("Aplicação iniciada.")

        self.main_window.show()

        exit_code = self.qt_app.exec()

        self.shutdown()

        sys.exit(exit_code)

    def shutdown(self):

        """
        Encerramento seguro da aplicação.
        """

        self.logger.info("Encerrando aplicação.")
