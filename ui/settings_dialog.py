from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import (QDialog, QWidget, QHBoxLayout, QVBoxLayout, 
                             QGroupBox, QListWidget, QListWidgetItem, 
                             QStackedWidget, QPushButton, QRadioButton, 
                             QSizePolicy)

class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setWindowTitle("Settings")
        self.resize(500, 400);
        self.createSettingsWidget()
        self.createButtons()
        vbxMainLayout = QVBoxLayout()
        vbxMainLayout.addWidget(self.settingsWidget, 10)
        vbxMainLayout.addWidget(self.buttonsWidget, 1)
        self.setLayout(vbxMainLayout)
        self.connectObjects()

    def createSettingsWidget(self):
        self.settingsWidget = QWidget(self)

        self.settingsGroup = QListWidget(self.settingsWidget)
        self.settingsGroup.setAutoScroll(False)
        self.databaseItem = QListWidgetItem("Database", self.settingsGroup)
        self.optionsItem = QListWidgetItem("Options", self.settingsGroup)
        sizeHint = QSize(200,50);
        self.databaseItem.setSizeHint(sizeHint)
        self.optionsItem.setSizeHint(sizeHint)
        self.settingsGroup.addItem(self.databaseItem)
        self.settingsGroup.addItem(self.optionsItem)

        self.createDatabaseWidget()
        self.createOptionsWidget()     
        self.emptyWidget = QWidget(self)
        
        self.stackedWidget = QStackedWidget(self)
        self.stackedWidget.addWidget(self.emptyWidget)
        self.stackedWidget.addWidget(self.databaseWidget)
        self.stackedWidget.addWidget(self.optionsWidget)
        self.stackedWidget.setCurrentWidget(self.emptyWidget)

        #sp_retain = self.database_widget.sizePolicy()
        #sp_retain.setRetainSizeWhenHidden(True)
        #self.database_widget.setSizePolicy(sp_retain)

        hbxLayout = QHBoxLayout()
        hbxLayout.addWidget(self.settingsGroup, 1)
        hbxLayout.addWidget(self.stackedWidget, 1)

        self.settingsWidget.setLayout(hbxLayout)

    def createDatabaseWidget(self):
        self.databaseWidget = QWidget(self.settingsWidget)
        dataloadGroupBox = QGroupBox("Data load", self.databaseWidget)
        threadsGroupBox = QGroupBox("Multithreading", self.databaseWidget)
        self.fillDataLoadBox(dataloadGroupBox)
        self.fillThreadsBox(threadsGroupBox)
        vbxLayout = QVBoxLayout()
        vbxLayout.addWidget(dataloadGroupBox, 1)
        vbxLayout.addWidget(threadsGroupBox, 1)
        vbxLayout.addStretch(10)
        self.databaseWidget.setLayout(vbxLayout)

    def createOptionsWidget(self):
        self.optionsWidget = QWidget(self.settingsWidget)
        optionsGroupBox = QGroupBox("Options", self.optionsWidget)
        vbxLayout = QVBoxLayout()
        vbxLayout.addWidget(optionsGroupBox, 5)
        vbxLayout.addStretch(10)
        self.optionsWidget.setLayout(vbxLayout)

    def createButtons(self):
        self.buttonsWidget = QWidget(self)
        self.applyButton = QPushButton("Apply", self)
        self.cancelButton = QPushButton("Cancel", self)
        hbxLayout = QHBoxLayout()
        hbxLayout.addStretch(10);
        hbxLayout.addWidget(self.applyButton, 1)
        hbxLayout.addWidget(self.cancelButton, 1)
        self.buttonsWidget.setLayout(hbxLayout)

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
        self.multithreadingOn = QRadioButton("On")
        self.multithreadingOff = QRadioButton("Off")
        vbox = QVBoxLayout()
        vbox.addWidget(self.multithreadingOn, 1)
        vbox.addWidget(self.multithreadingOff, 1)
        vbox.addStretch(1)
        self.multithreadingOff.setChecked(True)
        threads_group_box.setLayout(vbox)

    def onItemClicked(self, item):
        if item == self.databaseItem:
            self.stackedWidget.setCurrentWidget(self.databaseWidget)
        elif item == self.optionsItem:
            self.stackedWidget.setCurrentWidget(self.optionsWidget)
        else:
            self.stackedWidget.setCurrentWidget(self.emptyWidget)

    def connectObjects(self):
        self.settingsGroup.itemClicked.connect(self.onItemClicked)