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
        vbx_main_layout = QVBoxLayout()
        vbx_main_layout.addWidget(self.settings_widget, 10)
        vbx_main_layout.addWidget(self.buttons_widget, 1)
        self.setLayout(vbx_main_layout)
        self.connectObjects()

    def createSettingsWidget(self):
        self.settings_widget = QWidget(self)

        self.settings_group = QListWidget(self.settings_widget)
        self.settings_group.setAutoScroll(False)
        self.database_item = QListWidgetItem("Database", self.settings_group)
        self.options_item = QListWidgetItem("Options", self.settings_group)
        size_hint = QSize(200,50);
        self.database_item.setSizeHint(size_hint)
        self.options_item.setSizeHint(size_hint)
        self.settings_group.addItem(self.database_item)
        self.settings_group.addItem(self.options_item)

        self.createDatabaseWidget()
        self.createOptionsWidget()     
        self.empty_widget = QWidget(self)
        
        self.stacked_widget = QStackedWidget(self)
        self.stacked_widget.addWidget(self.empty_widget)
        self.stacked_widget.addWidget(self.database_widget)
        self.stacked_widget.addWidget(self.options_widget)
        self.stacked_widget.setCurrentWidget(self.empty_widget)

        #sp_retain = self.database_widget.sizePolicy()
        #sp_retain.setRetainSizeWhenHidden(True)
        #self.database_widget.setSizePolicy(sp_retain)

        hbx_layout = QHBoxLayout()
        hbx_layout.addWidget(self.settings_group, 1)
        hbx_layout.addWidget(self.stacked_widget, 1)

        self.settings_widget.setLayout(hbx_layout)

    def createDatabaseWidget(self):
        self.database_widget = QWidget(self.settings_widget)
        dataload_group_box = QGroupBox("Data load", self.database_widget)
        threads_group_box = QGroupBox("Multithreading", self.database_widget)
        self.fillDataLoadBox(dataload_group_box)
        self.fillThreadsBox(threads_group_box)
        vbx_layout = QVBoxLayout()
        vbx_layout.addWidget(dataload_group_box, 1)
        vbx_layout.addWidget(threads_group_box, 1)
        vbx_layout.addStretch(10)
        self.database_widget.setLayout(vbx_layout)

    def createOptionsWidget(self):
        self.options_widget = QWidget(self.settings_widget)
        options_group_box = QGroupBox("Options", self.options_widget)
        vbx_layout = QVBoxLayout()
        vbx_layout.addWidget(options_group_box, 5)
        vbx_layout.addStretch(10)
        self.options_widget.setLayout(vbx_layout)

    def createButtons(self):
        self.buttons_widget = QWidget(self)
        self.apply_button = QPushButton("Apply", self)
        self.cancel_button = QPushButton("Cancel", self)
        hbx_layout = QHBoxLayout()
        hbx_layout.addStretch(10);
        hbx_layout.addWidget(self.apply_button, 1)
        hbx_layout.addWidget(self.cancel_button, 1)
        self.buttons_widget.setLayout(hbx_layout)

    def fillDataLoadBox(self, dataload_group_box):
        self.radio_python = QRadioButton("Python")
        self.radio_go = QRadioButton("Go")
        self.radio_cpp = QRadioButton("C++")
        self.radio_java = QRadioButton("Java")
        vbox = QVBoxLayout()
        vbox.addWidget(self.radio_python, 1)
        vbox.addWidget(self.radio_go, 1)
        vbox.addWidget(self.radio_cpp, 1)
        vbox.addWidget(self.radio_java, 1)
        vbox.addStretch(1)
        self.radio_python.setChecked(True)
        dataload_group_box.setLayout(vbox)

    def fillThreadsBox(self, threads_group_box):
        self.multithreading_on = QRadioButton("On")
        self.multithreading_off = QRadioButton("Off")
        vbox = QVBoxLayout()
        vbox.addWidget(self.multithreading_on, 1)
        vbox.addWidget(self.multithreading_off, 1)
        vbox.addStretch(1)
        self.multithreading_off.setChecked(True)
        threads_group_box.setLayout(vbox)

    def onItemClicked(self, item):
        if item == self.database_item:
            self.stacked_widget.setCurrentWidget(self.database_widget)
        elif item == self.options_item:
            self.stacked_widget.setCurrentWidget(self.options_widget)
        else:
            self.stacked_widget.setCurrentWidget(self.empty_widget)

    def connectObjects(self):
        self.settings_group.itemClicked.connect(self.onItemClicked)