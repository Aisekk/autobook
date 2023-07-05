from ast import Add
from client import lib

from PyQt6.QtCore import QSize  # , Qt
from PyQt6.QtWidgets import QMainWindow, QPushButton, QWidget
from PyQt6.QtGui import QAction, QIcon
from ui.settings_dialog import SettingsDialog


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        # super().__init__()
        self.setWindowTitle(self.tr("Autobook"))
        self.setWindowIcon(QIcon("./sources/icons/cabriolet.png"))
        self.createMenus()
        self.settingsDialog = SettingsDialog(self)
        self.connectObjects()
        # button = QPushButton("From Go: backend.Add(10,99) = %d" % lib.Add(10,99))
        # self.setCentralWidget(button)

    def createMenus(self):
        carMenu = self.menuBar().addMenu(self.tr("Car"))
        self.createCarAction = QAction(self.tr("Create"), self)
        self.editCarAction = QAction(self.tr("Edit"), self)
        self.removeCarAction = QAction(self.tr("Remove"), self)
        carMenu.addAction(self.createCarAction)
        carMenu.addAction(self.editCarAction)
        carMenu.addAction(self.removeCarAction)

        projectMenu = self.menuBar().addMenu(self.tr("Project"))
        self.settingsAction = QAction(self.tr("Settings"), self)
        projectMenu.addAction(self.settingsAction)

    def connectObjects(self):
        self.settingsAction.triggered.connect(lambda: self.settingsDialog.show())
