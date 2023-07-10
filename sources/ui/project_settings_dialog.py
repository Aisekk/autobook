import sys
from PySide6.QtCore import QSize, qDebug
from PySide6.QtWidgets import (
    QDialog,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QGroupBox,
    QListWidget,
    QListWidgetItem,
    QStackedWidget,
    QPushButton,
    QComboBox,
    QSpinBox,
    QRadioButton,
    QLabel,
    QSizePolicy,
)


class ProjectSettingsDialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setWindowTitle(self.tr("Project settings"))
        self.resize(550, 400)
        self.__settingsWidget = self.__createSettingsWidget(self)
        self.__buttonsWidget = self.__createButtons(self)
        vbxMainLayout = QVBoxLayout()
        vbxMainLayout.addWidget(self.__settingsWidget, 10)
        vbxMainLayout.addWidget(self.__buttonsWidget, 1)
        self.setLayout(vbxMainLayout)
        self.__connectObjects()

    def __createSettingsWidget(self, parent=None):
        settingsWidget = QWidget(parent)

        self.__settingsGroup = QListWidget(settingsWidget)
        self.__settingsGroup.setAutoScroll(False)
        self.__carItem = QListWidgetItem(self.tr("Car"), self.__settingsGroup)
        self.__garageItem = QListWidgetItem(self.tr("Garage"), self.__settingsGroup)
        self.__databaseItem = QListWidgetItem(self.tr("Database"), self.__settingsGroup)

        self.__settingsGroup.addItem(self.__carItem)
        self.__settingsGroup.addItem(self.__garageItem)
        self.__settingsGroup.addItem(self.__databaseItem)

        self.setSizeHintOfItems(QSize(200, 50))

        self.__carWidget = self.__createCarWidget(settingsWidget)
        self.__garageWidget = self.__createGarageWidget(settingsWidget)
        self.__databaseWidget = self.__createDatabaseWidget(settingsWidget)
        self.__emptyWidget = QWidget(settingsWidget)

        self.__stackedWidget = QStackedWidget(self)
        self.__stackedWidget.addWidget(self.__emptyWidget)
        self.__stackedWidget.addWidget(self.__carWidget)
        self.__stackedWidget.addWidget(self.__garageWidget)
        self.__stackedWidget.addWidget(self.__databaseWidget)
        self.__stackedWidget.setCurrentWidget(self.__emptyWidget)

        # sp_retain = self.database_widget.sizePolicy()
        # sp_retain.setRetainSizeWhenHidden(True)
        # self.database_widget.setSizePolicy(sp_retain)

        hbxLayout = QHBoxLayout()
        hbxLayout.addWidget(self.__settingsGroup, 1)
        hbxLayout.addWidget(self.__stackedWidget, 1)

        settingsWidget.setLayout(hbxLayout)
        return settingsWidget

    def __createCarWidget(self, parent=None):
        carWidget = QWidget(parent)
        carGroupBox = QGroupBox(self.tr("Car"), carWidget)
        self.__fillCarBox(carGroupBox)
        vbxLayout = QVBoxLayout()
        vbxLayout.addWidget(carGroupBox, 1)
        vbxLayout.addStretch(10)
        carWidget.setLayout(vbxLayout)
        return carWidget

    def __createDatabaseWidget(self, parent=None):
        databaseWidget = QWidget(parent)
        dataloadGroupBox = QGroupBox(self.tr("Data load"), databaseWidget)
        threadsGroupBox = QGroupBox(self.tr("Multithreading"), databaseWidget)
        self.__fillDataLoadBox(dataloadGroupBox)
        self.__fillThreadsBox(threadsGroupBox)
        vbxLayout = QVBoxLayout()
        vbxLayout.addWidget(dataloadGroupBox, 1)
        vbxLayout.addWidget(threadsGroupBox, 1)
        vbxLayout.addStretch(10)
        databaseWidget.setLayout(vbxLayout)
        return databaseWidget

    def __createGarageWidget(self, parent=None):
        garageWidget = QWidget(parent)
        garageLimitsGroupBox = QGroupBox(self.tr("Limits"), garageWidget)
        self.__fillGarageLimitsBox(garageLimitsGroupBox)
        vbxLayout = QVBoxLayout()
        vbxLayout.addWidget(garageLimitsGroupBox, 10)
        vbxLayout.addStretch(10)
        garageWidget.setLayout(vbxLayout)
        return garageWidget

    def __createButtons(self, parent=None):
        buttonsWidget = QWidget(parent)
        self.__applyButton = QPushButton(self.tr("Apply"), buttonsWidget)
        self.__cancelButton = QPushButton(self.tr("Cancel"), buttonsWidget)
        hbxLayout = QHBoxLayout()
        hbxLayout.addStretch(10)
        hbxLayout.addWidget(self.__applyButton, 1)
        hbxLayout.addWidget(self.__cancelButton, 1)
        buttonsWidget.setLayout(hbxLayout)
        return buttonsWidget

    def setSizeHintOfItems(self, sizeHint):
        for row in range(self.__settingsGroup.count()):
            self.__settingsGroup.item(row).setSizeHint(sizeHint)

    def __fillCarBox(self, carGroupBox):
        self.__carComboBox = QComboBox()
        self.__carComboBox.addItems(
            [
                "Hyundai Solaris 1.6 2012",
                "VAZ Lada Vesta 1.5 2020",
                "Haval F7x 1.5 2023",
            ]
        )
        vbox = QVBoxLayout()
        vbox.addWidget(self.__carComboBox, 1)
        vbox.addStretch(1)
        carGroupBox.setLayout(vbox)

    def __fillGarageLimitsBox(self, garageLimitsGroupBox):
        maxCarCountLabel = QLabel(self.tr("Maximum car count") + ":")
        self.__maxCarCountSpinBox = QSpinBox()
        self.__maxCarCountSpinBox.setRange(1, int(10e8))
        self.__maxCarCountSpinBox.setValue(5)
        vbox = QVBoxLayout()
        vbox.addWidget(maxCarCountLabel, 1)
        vbox.addWidget(self.__maxCarCountSpinBox, 1)
        vbox.addStretch(10)
        garageLimitsGroupBox.setLayout(vbox)

    def __fillDataLoadBox(self, dataloadGroupBox):
        self.__radioPython = QRadioButton("Python")
        self.__radioGo = QRadioButton("Go")
        self.__radioCpp = QRadioButton("C++")
        self.__radioJava = QRadioButton("Java")
        vbox = QVBoxLayout()
        vbox.addWidget(self.__radioPython, 1)
        vbox.addWidget(self.__radioGo, 1)
        vbox.addWidget(self.__radioCpp, 1)
        vbox.addWidget(self.__radioJava, 1)
        vbox.addStretch(1)
        self.__radioPython.setChecked(True)
        dataloadGroupBox.setLayout(vbox)

    def __fillThreadsBox(self, threads_group_box):
        self.__multithreadingOn = QRadioButton(self.tr("On"))
        self.__multithreadingOff = QRadioButton(self.tr("Off"))
        vbox = QVBoxLayout()
        vbox.addWidget(self.__multithreadingOn, 1)
        vbox.addWidget(self.__multithreadingOff, 1)
        vbox.addStretch(1)
        self.__multithreadingOff.setChecked(True)
        threads_group_box.setLayout(vbox)

    def __onItemClicked(self, item):
        match item:
            case self.__carItem:
                self.__stackedWidget.setCurrentWidget(self.__carWidget)
            case self.__garageItem:
                self.__stackedWidget.setCurrentWidget(self.__garageWidget)
            case self.__databaseItem:
                self.__stackedWidget.setCurrentWidget(self.__databaseWidget)
            case _:
                self.__stackedWidget.setCurrentWidget(self.__emptyWidget)

    def __connectObjects(self):
        self.__settingsGroup.itemClicked.connect(self.__onItemClicked)