from PySide6.QtWidgets import QMainWindow
from ui.dashboard import Dashboard


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("HordaRPG")

        self.dashboard = Dashboard()

        self.setCentralWidget(self.dashboard)