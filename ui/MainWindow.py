from ast import Add
from PyQt6.QtCore import QSize #, Qt
from PyQt6.QtWidgets import QMainWindow, QPushButton
from client import lib

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Autobook")

        button = QPushButton("From Go: backend.Add(10,99) = %d" % lib.Add(10,99))

        self.setFixedSize(QSize(400, 300))

        self.setCentralWidget(button)