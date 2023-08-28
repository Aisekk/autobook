from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QStackedWidget,
)
from PySide6.QtGui import QAction, QIcon

import ui.control_widget
import ui.car_addition_dialog
import ui.project_settings_dialog
import ui.stack_widgets.engine_widget


class StructUi(object):
    def __init__(self, mainWindow) -> None: 
        self.carAdditionDialog = ui.car_addition_dialog.CarAdditionDialog(mainWindow)
        self.projectSettingsDialog = ui.project_settings_dialog.ProjectSettingsDialog(
            mainWindow
        )
        self.controlWidget = ui.control_widget.ControlWidget(mainWindow)

        self.stackedWidget = QStackedWidget()
        self.emptyWidget = QWidget()
        self.engineWidget = ui.stack_widgets.engine_widget.EngineWidget()

        self.stackedWidget.addWidget(self.emptyWidget)
        self.stackedWidget.addWidget(self.engineWidget)

        self.centralWidget = QWidget(mainWindow)

        self.addCarAction = QAction(mainWindow.tr("Add") + "...", mainWindow)
        self.editCarAction = QAction(mainWindow.tr("Edit"), mainWindow)
        self.removeCarAction = QAction(mainWindow.tr("Remove"), mainWindow)
        
        self.openGarageAction = QAction(mainWindow.tr("Open"), mainWindow)
        self.projectAction = QAction(mainWindow.tr("Project"), mainWindow)
        self.aboutProgramAction = QAction(mainWindow.tr("About program"), mainWindow)

    def createMenus(self, mainWindow) -> None:
        carMenu = mainWindow.menuBar().addMenu(mainWindow.tr("Car"))
        carMenu.addAction(self.addCarAction)
        carMenu.addAction(self.editCarAction)
        carMenu.addAction(self.removeCarAction)

        garageMenu = mainWindow.menuBar().addMenu(mainWindow.tr("Garage"))
        garageMenu.addAction(self.openGarageAction)

        settingsMenu = mainWindow.menuBar().addMenu(mainWindow.tr("Settings"))
        settingsMenu.addAction(self.projectAction)

        infoMenu = mainWindow.menuBar().addMenu(mainWindow.tr("Info"))
        infoMenu.addAction(self.aboutProgramAction)