from PySide6.QtCore import Qt, qDebug
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QGridLayout,
    QGroupBox,
    QPushButton,
    QLineEdit,
    QLabel,
    QComboBox,
    QTreeView,
)

import data_store.autobook_data_store as storage
import data_store.structs


class ControlWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.__carDataDisplayWidget = self.__createCarDataDisplayWidget(self)
        self.__buttonsWidget = self.__createButtons(self)
        self.__leSearch = self.__createSearchLineEdit(self)
        self.__cbxClassifier = self.__createClassifierComboBox(self)
        self.__classifierView = self.__createClassifierView(self)
        vbxMainLayout = QVBoxLayout()
        vbxMainLayout.addWidget(self.__carDataDisplayWidget, 10)
        vbxMainLayout.addWidget(self.__buttonsWidget, 10)
        vbxMainLayout.addWidget(self.__leSearch, 1)
        vbxMainLayout.addWidget(self.__cbxClassifier, 1)
        vbxMainLayout.addWidget(self.__classifierView, 30)
        vbxMainLayout.addStretch(1)
        self.setLayout(vbxMainLayout)

    def __createCarDataDisplayWidget(self, parent=None):
        carGroupBox = QGroupBox(parent)
        # font = QFont("Arial", 10)
        # font.setBold(True)
        # carGroupBox.setFont(font)
        # carGroupBox.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.__carLabel = QLabel(self.getCarLabelText())
        vbxLayout = QVBoxLayout()
        vbxLayout.addWidget(self.__carLabel)
        carGroupBox.setLayout(vbxLayout)
        return carGroupBox

    def getCarLabelText(self):
        # carData = storage.AutobookDataStore().getCarData()
        carData = storage.AutobookDataStore().getDefaultCarData()
        brand = self.__getCarDataTextElem(carData.brand)
        model = self.__getCarDataTextElem(carData.model)
        engineCap = self.__getCarDataTextElem(carData.engineCapacity)
        manufYear = self.__getCarDataTextElem(carData.manufactureYear)
        gosNum = self.__getCarDataTextElem(carData.gosNumber)
        bodyType = self.__getCarDataTextElem(carData.bodyType)
        ownerDriver = self.__getCarDataTextElem(carData.ownerDriver)
        text = brand + model + engineCap + manufYear + gosNum + bodyType + ownerDriver
        return text

    def __getCarDataTextElem(self, elem):
        return str("<STRONG><CENTER>" + str(elem) + "</STRONG>")
        # return str("<H4><CENTER><FONT COLOR=GREEN>" + str(elem) + "</H4>")

    def __createButtons(self, parent=None):
        buttonsWidget = QWidget(parent)
        self.__basicsButton = QPushButton(self.tr("Basics"), buttonsWidget)
        self.__detailsButton = QPushButton(self.tr("Details"), buttonsWidget)
        self.__numbersAndCodesButton = QPushButton(
            self.tr("Numbers and codes"), buttonsWidget
        )
        self.__ownerDriverButton = QPushButton(self.tr("Owner/Driver"), buttonsWidget)
        vbxLayout = QVBoxLayout()
        vbxLayout.addWidget(self.__basicsButton, 1)
        vbxLayout.addWidget(self.__detailsButton, 1)
        vbxLayout.addWidget(self.__numbersAndCodesButton, 1)
        vbxLayout.addWidget(self.__ownerDriverButton, 1)
        buttonsWidget.setLayout(vbxLayout)
        return buttonsWidget

    def __createSearchLineEdit(self, parent=None):
        searchLineEdit = QLineEdit(parent)
        searchLineEdit.setPlaceholderText(self.tr("Find") + "...")
        return searchLineEdit

    def __createClassifierComboBox(self, parent=None):
        cbxClassifier = QComboBox(parent)
        cbxClassifier.addItems(["Classifier 1", "Classifier 2"])
        return cbxClassifier

    def __createClassifierView(self, parent=None):
        classifierView = QTreeView(parent)
        return classifierView