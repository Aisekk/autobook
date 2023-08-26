from ast import Add
from client import lib

from PySide6.QtCore import qDebug
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QPushButton,
    QMessageBox,
    QStackedWidget,
)
from PySide6.QtGui import QAction, QIcon
import ui.struct_ui
import data_store.data_store as storage


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.__ui = ui.struct_ui.StructUi(self)
        self.setWindowTitle(self.tr("Autobook"))
        self.setWindowIcon(QIcon("./sources/icons/cabriolet.png"))
        self.__ui.createMenus(self)       

        hbxMainLayout = QHBoxLayout()
        hbxMainLayout.addWidget(self.__ui.controlWidget, 10)
        hbxMainLayout.addWidget(self.__ui.stackedWidget, 40)
        self.__ui.centralWidget.setLayout(hbxMainLayout)
        self.setCentralWidget(self.__ui.centralWidget)

        #self.__stackedWidget.setCurrentWidget(self.__ui.emptyWidget)
        self.__ui.stackedWidget.setCurrentWidget(self.__ui.engineWidget)

        self.__connectObjects()
        # button = QPushButton("From Go: backend.Add(10,99) = %d" % lib.Add(10,99))
        # self.setCentralWidget(button)

        self.__loadData()

    def __connectObjects(self) -> None:
        self.__ui.addCarAction.triggered.connect(lambda: self.__ui.carAdditionDialog.show())
        self.__ui.projectAction.triggered.connect(
            lambda: self.__ui.projectSettingsDialog.show()
        )
        self.__ui.aboutProgramAction.triggered.connect(
            lambda: QMessageBox.information(
                self,
                self.tr("About program"),
                self.tr("Autobook v0.0.0.0\nCopyright (c) 2023 Aleksandr Chekmarev"),
                # QCoreApplication.translate("MainWindow", "Autobook v0.0.0.0\nCopyright (c) 2023 Aleksandr Chekmarev")
            )
        )

    def __loadData(self):
        if storage.AutobookDataStore().loadData():
            self.__ui.engineWidget.loadData()
