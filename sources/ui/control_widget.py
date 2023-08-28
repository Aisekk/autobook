import signal
#from PySide6.QtGui import QString
from PySide6.QtCore import Signal, QModelIndex, Qt, qDebug
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
import data_store.enums as enums
import models.classifier_model as classifier_model
import items.classifier_item as classifier_item
import data_store.const_info as const_info
from sources.data_store.values import BasicValues


class ControlWidget(QWidget):
    treeItemClicked = Signal(enums.MainComponent)

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
            enums.Classifier.MainComponentsAndAssemblies,
            self.__classifierModel.invisibleRootItem(),
        )
        self.__classifierModel.addItems(
            self.__classifierModel.invisibleRootItem(), items
        )

        vbxMainLayout = QVBoxLayout()
        vbxMainLayout.addWidget(self.__carDataDisplayWidget, 10)
        vbxMainLayout.addWidget(self.__buttonsWidget, 10)
        vbxMainLayout.addWidget(self.__leSearch, 1)
        vbxMainLayout.addWidget(self.__cbxClassifier, 1)
        vbxMainLayout.addWidget(self.__classifierView, 50)
        vbxMainLayout.addStretch(1)
        self.setLayout(vbxMainLayout)

        self.__connectObjects()

    def loadData(self):
        basicValues = storage.AutobookDataStore().getValues().basicValues
        text = self.getCarLabelText(basicValues)
        self.__carLabel.setText(text)

    def __connectObjects(self) -> None:
        self.__classifierView.clicked.connect(
            lambda modelIndex: self.treeItemClicked.emit(
                modelIndex.data(enums.ClassifierItemRole.ItemId)
            )
        )

    def __createCarDataDisplayWidget(self, parent=None) -> QGroupBox:
        carGroupBox = QGroupBox(parent)
        basicValues = storage.AutobookDataStore().getDefaultValues()
        self.__carLabel = QLabel(self.getCarLabelText(basicValues))
        vbxLayout = QVBoxLayout()
        vbxLayout.addWidget(self.__carLabel)
        carGroupBox.setLayout(vbxLayout)
        return carGroupBox

    def getCarLabelText(self, basicValues: BasicValues) -> str:
        brand = self.__getCarDataTextElem(basicValues.brand)
        model = self.__getCarDataTextElem(basicValues.model)
        engineCap = self.__getCarDataTextElem(basicValues.engineCapacity)
        manufYear = self.__getCarDataTextElem(basicValues.manufactureYear)
        gosNum = self.__getCarDataTextElem(basicValues.gosNumber)
        bodyType = self.__getCarDataTextElem(basicValues.bodyType)
        ownerDriver = self.__getCarDataTextElem(basicValues.ownerDriver)
        manufWarranty = self.__getCarDataTextElem(self.tr("Warranty") + " " + basicValues.manufWarranty)
        text = (
            brand
            + model
            + engineCap
            + manufYear
            + gosNum
            + bodyType
            + ownerDriver
            + manufWarranty
        )
        return text

    def __getCarDataTextElem(self, elem: str) -> str:
        return str("<STRONG><CENTER>" + str(elem) + "</STRONG>")

    def __createButtons(self, parent=None) -> QWidget:
        buttonsWidget = QWidget(parent)
        self.__basicsButton = QPushButton(self.tr("Records"), buttonsWidget)
        self.__detailsButton = QPushButton(self.tr("Parameters"), buttonsWidget)
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
