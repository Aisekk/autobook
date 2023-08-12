from PySide6.QtCore import Qt, qDebug
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QGroupBox,
    QPushButton,
    QLineEdit,
    QLabel,
    QComboBox,
    QTreeView,
    QAbstractItemView,
)

import data_store.data_store as storage
import data_store.structs as structs
import models.classifier_model as classifier_model
import items.classifier_item as classifier_item
import data_store.const_info as const_info


class ControlWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.__carDataDisplayWidget = self.__createCarDataDisplayWidget(self)
        self.__buttonsWidget = self.__createButtons(self)
        self.__leSearch = self.__createSearchLineEdit(self)
        self.__cbxClassifier = self.__createClassifierComboBox(self)
        self.__classifierView = self.__createClassifierView(self)
        self.__classifierModel = classifier_model.ClassifierModel(self.__classifierView)

        self.__classifierView.setModel(self.__classifierModel)

        items = storage.AutobookDataStore().getItems(
            structs.Classifier.MainComponentsAndAssemblies,
            self.__classifierModel.invisibleRootItem(),
        )
        self.__classifierModel.addItems(
            self.__classifierModel.invisibleRootItem(), items
        )
        # self.__classifierModel.addItems(items[0], [child])

        vbxMainLayout = QVBoxLayout()
        vbxMainLayout.addWidget(self.__carDataDisplayWidget, 10)
        vbxMainLayout.addWidget(self.__buttonsWidget, 10)
        vbxMainLayout.addWidget(self.__leSearch, 1)
        vbxMainLayout.addWidget(self.__cbxClassifier, 1)
        vbxMainLayout.addWidget(self.__classifierView, 50)
        vbxMainLayout.addStretch(1)
        self.setLayout(vbxMainLayout)

    def __createCarDataDisplayWidget(self, parent=None) -> QGroupBox:
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

    def getCarLabelText(self) -> str:
        # carData = storage.AutobookDataStore().getCarData()
        carData = storage.AutobookDataStore().getDefaultCarData()
        brand = self.__getCarDataTextElem__(carData.brand)
        model = self.__getCarDataTextElem__(carData.model)
        engineCap = self.__getCarDataTextElem__(carData.engineCapacity)
        manufYear = self.__getCarDataTextElem__(carData.manufactureYear)
        gosNum = self.__getCarDataTextElem__(carData.gosNumber)
        bodyType = self.__getCarDataTextElem__(carData.bodyType)
        ownerDriver = self.__getCarDataTextElem__(carData.ownerDriver)
        text = brand + model + engineCap + manufYear + gosNum + bodyType + ownerDriver
        return text

    def __getCarDataTextElem__(self, elem: str) -> str:
        return str("<STRONG><CENTER>" + str(elem) + "</STRONG>")
        # return str("<H4><CENTER><FONT COLOR=GREEN>" + str(elem) + "</H4>")

    def __createButtons(self, parent=None) -> QWidget:
        buttonsWidget = QWidget(parent)
        self.__basicsButton = QPushButton(self.tr("Basics"), buttonsWidget)
        self.__detailsButton = QPushButton(self.tr("Details"), buttonsWidget)
        self.__numbersAndCodesButton = QPushButton(
            self.tr("Numbers and codes"), buttonsWidget
        )
        self.__ownerDriverButton = QPushButton(self.tr("Owner/Driver"), buttonsWidget)

        maxButtonWidth = 150
        self.__basicsButton.setMaximumWidth(maxButtonWidth)
        self.__detailsButton.setMaximumWidth(maxButtonWidth)
        self.__numbersAndCodesButton.setMaximumWidth(maxButtonWidth)
        self.__ownerDriverButton.setMaximumWidth(maxButtonWidth)

        vbxLayout = QVBoxLayout()
        vbxLayout.addWidget(self.__basicsButton, 1)
        vbxLayout.addWidget(self.__detailsButton, 1)
        vbxLayout.addWidget(self.__numbersAndCodesButton, 1)
        vbxLayout.addWidget(self.__ownerDriverButton, 1)
        buttonsWidget.setLayout(vbxLayout)
        return buttonsWidget

    def __createSearchLineEdit(self, parent=None) -> QLineEdit:
        lineEdit = QLineEdit(parent)
        lineEdit.setPlaceholderText(self.tr("Find") + "...")
        return lineEdit

    def __createClassifierComboBox(self, parent=None) -> QComboBox:
        cbxClassifier = QComboBox(parent)
        for index, name in const_info.classifiers.items():
            cbxClassifier.addItem(self.tr(name), index)
        return cbxClassifier

    def __createClassifierView(self, parent=None) -> QTreeView:
        treeView = QTreeView(parent)
        treeView.setHeaderHidden(True)
        treeView.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        treeView.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)
        return treeView