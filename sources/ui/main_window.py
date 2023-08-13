from ast import Add
from client import lib

# from PySide6.QtCore import Qt, QCoreApplication
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QPushButton,
    QMessageBox,
    QStackedWidget,
)
from PySide6.QtGui import QAction, QIcon

import ui.control_widget
import ui.car_addition_dialog
import ui.project_settings_dialog
import data_store.data_store as storage


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        # super().__init__()
        self.setWindowTitle(self.tr("Autobook"))
        self.setWindowIcon(QIcon("./sources/icons/cabriolet.png"))
        self.__createMenus()
        self.__carAdditionDialog = ui.car_addition_dialog.CarAdditionDialog(self)
        self.__projectSettingsDialog = ui.project_settings_dialog.ProjectSettingsDialog(
            self
        )
        self.__controlWidget = ui.control_widget.ControlWidget()
        self.__stackedWidget = QStackedWidget()
        self.__emptyWidget = QWidget()
        self.__stackedWidget.addWidget(self.__emptyWidget)

        centralWidget = QWidget(self)
        hbxMainLayout = QHBoxLayout()
        hbxMainLayout.addWidget(self.__controlWidget, 10)
        hbxMainLayout.addWidget(self.__stackedWidget, 40)
        centralWidget.setLayout(hbxMainLayout)
        self.setCentralWidget(centralWidget)

        self.__stackedWidget.setCurrentWidget(self.__emptyWidget)

        self.__connectObjects()
        # button = QPushButton("From Go: backend.Add(10,99) = %d" % lib.Add(10,99))
        # self.setCentralWidget(button)

    def __createMenus(self) -> None:
        carMenu = self.menuBar().addMenu(self.tr("Car"))
        self.__addCarAction = QAction(self.tr("Add") + "...", self)
        self.__editCarAction = QAction(self.tr("Edit"), self)
        self.__removeCarAction = QAction(self.tr("Remove"), self)
        carMenu.addAction(self.__addCarAction)
        carMenu.addAction(self.__editCarAction)
        carMenu.addAction(self.__removeCarAction)

        garageMenu = self.menuBar().addMenu(self.tr("Garage"))
        self.__openGarageAction = QAction(self.tr("Open"), self)
        garageMenu.addAction(self.__openGarageAction)

        settingsMenu = self.menuBar().addMenu(self.tr("Settings"))
        self.__projectAction = QAction(self.tr("Project"), self)
        settingsMenu.addAction(self.__projectAction)

        infoMenu = self.menuBar().addMenu(self.tr("Info"))
        self.__aboutProgramAction = QAction(self.tr("About program"), self)
        infoMenu.addAction(self.__aboutProgramAction)

    def __connectObjects(self) -> None:
        self.__addCarAction.triggered.connect(lambda: self.__carAdditionDialog.show())
        self.__projectAction.triggered.connect(
            lambda: self.__projectSettingsDialog.show()
        )
        self.__aboutProgramAction.triggered.connect(
            lambda: QMessageBox.information(
                self,
                self.tr("About program"),
                self.tr("Autobook v0.0.0.0\nCopyright (c) 2023 Aleksandr Chekmarev"),
                # QCoreApplication.translate("MainWindow", "Autobook v0.0.0.0\nCopyright (c) 2023 Aleksandr Chekmarev")
            )
        )
