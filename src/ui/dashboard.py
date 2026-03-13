from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Qt


class Dashboard(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("HordaRPG")

        layout = QVBoxLayout()

        title = QLabel("HordaRPG")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold;")

        layout.addWidget(title)

        self.grid_button = QPushButton("Grid")
        self.book_button = QPushButton("Livro")
        self.sheet_button = QPushButton("Ficha")
        self.settings_button = QPushButton("Configurações")

        layout.addWidget(self.grid_button)
        layout.addWidget(self.book_button)
        layout.addWidget(self.sheet_button)
        layout.addWidget(self.settings_button)

        layout.addStretch()

        self.setLayout(layout)