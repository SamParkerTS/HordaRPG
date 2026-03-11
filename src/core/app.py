import sys
from core.logger import Logger
from core.config import Config

from PySide6.QtWidgets import QApplication

from core.paths import Paths
from ui.main_window import MainWindow


class Application:
    def __init__(self):
        """
        Núcleo da aplicação.
        Responsável por inicializar sistemas essenciais.
        """

    def __init__(self):

        self.paths = Paths()

        self.config = Config(self.paths)

        self.logger = Logger(self.paths).get_logger()

        self.qt_app = QApplication(sys.argv)

        self.main_window = MainWindow()

        self.logger.info("Aplicação inicializada.")

    def run(self):
        """
        Inicia a interface e o loop da aplicação.
        """

        self.main_window.show()

        return self.qt_app.exec()