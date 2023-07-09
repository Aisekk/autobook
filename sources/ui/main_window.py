from ast import Add
from client import lib

from PySide6.QtCore import QSize  # , Qt
from PySide6.QtWidgets import QMainWindow, QPushButton, QMessageBox
from PySide6.QtGui import QAction, QIcon
from ui.car_addition_dialog import CarAdditionDialog
from ui.project_settings_dialog import ProjectSettingsDialog
from data_store.autobook_data_store import AutobookDataStore


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        # super().__init__()
        # ui
        self.setWindowTitle(self.tr("Autobook"))
        self.setWindowIcon(QIcon("./sources/icons/cabriolet.png"))
        self.createMenus()
        self.carAdditionDialog = CarAdditionDialog(self)
        self.projectSettingsDialog = ProjectSettingsDialog(self)
        self.connectObjects()
        # self.autobookDataStore = AutobookDataStore()
        # button = QPushButton("From Go: backend.Add(10,99) = %d" % lib.Add(10,99))
        # self.setCentralWidget(button)

    def createMenus(self):
        carMenu = self.menuBar().addMenu(self.tr("Car"))
        self.addCarAction = QAction(self.tr("Add") + "...", self)
        self.editCarAction = QAction(self.tr("Edit"), self)
        self.removeCarAction = QAction(self.tr("Remove"), self)
        carMenu.addAction(self.addCarAction)
        carMenu.addAction(self.editCarAction)
        carMenu.addAction(self.removeCarAction)

        garageMenu = self.menuBar().addMenu(self.tr("Garage"))
        self.openGarageAction = QAction(self.tr("Open"), self)
        garageMenu.addAction(self.openGarageAction)

        settingsMenu = self.menuBar().addMenu(self.tr("Settings"))
        self.projectAction = QAction(self.tr("Project"), self)
        settingsMenu.addAction(self.projectAction)

        infoMenu = self.menuBar().addMenu(self.tr("Info"))
        self.aboutProgramAction = QAction(self.tr("About program"), self)
        infoMenu.addAction(self.aboutProgramAction)

    def connectObjects(self):
        self.addCarAction.triggered.connect(lambda: self.carAdditionDialog.show())
        self.projectAction.triggered.connect(lambda: self.projectSettingsDialog.show())
        self.aboutProgramAction.triggered.connect(
            lambda: QMessageBox.information(
                self,
                self.tr("About program"),
                self.tr("Autobook v0.0.0.0\nCopyright (c) 2023 Aleksandr Chekmarev"),
            )
        )
