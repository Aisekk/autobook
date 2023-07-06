from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import (
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
    QRadioButton,
    QSizePolicy,
)


class ProjectSettingsDialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setWindowTitle(self.tr("Project settings"))
        self.resize(500, 400)
        self.settingsWidget = self.createSettingsWidget(self)
        self.buttonsWidget = self.createButtons(self)
        vbxMainLayout = QVBoxLayout()
        vbxMainLayout.addWidget(self.settingsWidget, 10)
        vbxMainLayout.addWidget(self.buttonsWidget, 1)
        self.setLayout(vbxMainLayout)
        self.connectObjects()

    def createSettingsWidget(self, parent=None):
        settingsWidget = QWidget(parent)

        self.settingsGroup = QListWidget(settingsWidget)
        self.settingsGroup.setAutoScroll(False)
        self.carItem = QListWidgetItem(self.tr("Car"), self.settingsGroup)
        self.databaseItem = QListWidgetItem(self.tr("Database"), self.settingsGroup)
        self.optionsItem = QListWidgetItem(self.tr("Options"), self.settingsGroup)

        self.settingsGroup.addItem(self.carItem)
        self.settingsGroup.addItem(self.databaseItem)
        self.settingsGroup.addItem(self.optionsItem)

        self.setSizeHintOfItems(QSize(200, 50))

        self.carWidget = self.createCarWidget(settingsWidget)
        self.databaseWidget = self.createDatabaseWidget(settingsWidget)
        self.optionsWidget = self.createOptionsWidget(settingsWidget)
        self.emptyWidget = QWidget(settingsWidget)

        self.stackedWidget = QStackedWidget(self)
        self.stackedWidget.addWidget(self.emptyWidget)
        self.stackedWidget.addWidget(self.carWidget)
        self.stackedWidget.addWidget(self.databaseWidget)
        self.stackedWidget.addWidget(self.optionsWidget)
        self.stackedWidget.setCurrentWidget(self.emptyWidget)

        # sp_retain = self.database_widget.sizePolicy()
        # sp_retain.setRetainSizeWhenHidden(True)
        # self.database_widget.setSizePolicy(sp_retain)

        hbxLayout = QHBoxLayout()
        hbxLayout.addWidget(self.settingsGroup, 1)
        hbxLayout.addWidget(self.stackedWidget, 1)

        settingsWidget.setLayout(hbxLayout)
        return settingsWidget

    def createCarWidget(self, parent=None):
        carWidget = QWidget(parent)
        carGroupBox = QGroupBox(self.tr("Car"), carWidget)
        self.fillCarBox(carGroupBox)
        vbxLayout = QVBoxLayout()
        vbxLayout.addWidget(carGroupBox, 1)
        vbxLayout.addStretch(10)
        carWidget.setLayout(vbxLayout)
        return carWidget

    def createDatabaseWidget(self, parent=None):
        databaseWidget = QWidget(parent)
        dataloadGroupBox = QGroupBox(self.tr("Data load"), databaseWidget)
        threadsGroupBox = QGroupBox(self.tr("Multithreading"), databaseWidget)
        self.fillDataLoadBox(dataloadGroupBox)
        self.fillThreadsBox(threadsGroupBox)
        vbxLayout = QVBoxLayout()
        vbxLayout.addWidget(dataloadGroupBox, 1)
        vbxLayout.addWidget(threadsGroupBox, 1)
        vbxLayout.addStretch(10)
        databaseWidget.setLayout(vbxLayout)
        return databaseWidget

    def createOptionsWidget(self, parent=None):
        optionsWidget = QWidget(parent)
        optionsGroupBox = QGroupBox(self.tr("Options"), optionsWidget)
        vbxLayout = QVBoxLayout()
        vbxLayout.addWidget(optionsGroupBox, 5)
        vbxLayout.addStretch(10)
        optionsWidget.setLayout(vbxLayout)
        return optionsWidget

    def createButtons(self, parent=None):
        buttonsWidget = QWidget(parent)
        self.applyButton = QPushButton(self.tr("Apply"), buttonsWidget)
        self.cancelButton = QPushButton(self.tr("Cancel"), buttonsWidget)
        hbxLayout = QHBoxLayout()
        hbxLayout.addStretch(10)
        hbxLayout.addWidget(self.applyButton, 1)
        hbxLayout.addWidget(self.cancelButton, 1)
        buttonsWidget.setLayout(hbxLayout)
        return buttonsWidget

    def setSizeHintOfItems(self, sizeHint):
        for row in range(self.settingsGroup.count()):
            self.settingsGroup.item(row).setSizeHint(sizeHint)

    def fillCarBox(self, carGroupBox):
        self.carComboBox = QComboBox()
        self.carComboBox.addItems(
            [
                "Hyundai Solaris 1.6 2012",
                "VAZ Lada Vesta 1.5 2020",
                "Haval F7x 1.5 2023",
            ]
        )
        vbox = QVBoxLayout()
        vbox.addWidget(self.carComboBox, 1)
        vbox.addStretch(1)
        carGroupBox.setLayout(vbox)

    def fillDataLoadBox(self, dataloadGroupBox):
        self.radioPython = QRadioButton("Python")
        self.radioGo = QRadioButton("Go")
        self.radioCpp = QRadioButton("C++")
        self.radioJava = QRadioButton("Java")
        vbox = QVBoxLayout()
        vbox.addWidget(self.radioPython, 1)
        vbox.addWidget(self.radioGo, 1)
        vbox.addWidget(self.radioCpp, 1)
        vbox.addWidget(self.radioJava, 1)
        vbox.addStretch(1)
        self.radioPython.setChecked(True)
        dataloadGroupBox.setLayout(vbox)

    def fillThreadsBox(self, threads_group_box):
        self.multithreadingOn = QRadioButton(self.tr("On"))
        self.multithreadingOff = QRadioButton(self.tr("Off"))
        vbox = QVBoxLayout()
        vbox.addWidget(self.multithreadingOn, 1)
        vbox.addWidget(self.multithreadingOff, 1)
        vbox.addStretch(1)
        self.multithreadingOff.setChecked(True)
        threads_group_box.setLayout(vbox)

    def onItemClicked(self, item):
        match item:
            case self.carItem:
                self.stackedWidget.setCurrentWidget(self.carWidget)
            case self.databaseItem:
                self.stackedWidget.setCurrentWidget(self.databaseWidget)
            case self.optionsItem:
                self.stackedWidget.setCurrentWidget(self.optionsWidget)
            case _:
                self.stackedWidget.setCurrentWidget(self.emptyWidget)

    def connectObjects(self):
        self.settingsGroup.itemClicked.connect(self.onItemClicked)