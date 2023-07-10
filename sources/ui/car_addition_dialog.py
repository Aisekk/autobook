from PySide6.QtCore import qDebug
from PySide6.QtWidgets import (
    QDialog,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QGridLayout,
    QPushButton,
    QLineEdit,
    QLabel,
)


class CarAdditionDialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setWindowTitle(self.tr("Add new car"))
        self.setMaximumSize(800, 250)
        self.resize(400, 250)
        self.__carDataWidget = self.__createCarDataWidget(self)
        self.__buttonsWidget = self.__createButtons(self)
        vbxMainLayout = QVBoxLayout()
        vbxMainLayout.addWidget(self.__carDataWidget, 10)
        vbxMainLayout.addStretch(10)
        vbxMainLayout.addWidget(self.__buttonsWidget, 1)
        self.setLayout(vbxMainLayout)

    def __createCarDataWidget(self, parent=None):
        carDataWidget = QWidget(parent)
        self.__grdLayout = QGridLayout()
        self.__rowSpan = 1
        self.__colSpan = 1

        row = 0
        self.__leBrand = self.__addDataElemWidget("Brand*", row)
        row += 1
        self.__leModel = self.__addDataElemWidget("Model*", row)
        row += 1
        self.__leEngineCapacity = self.__addDataElemWidget("Engine capacity, l", row)
        row += 1
        self.__leManufactureYear = self.__addDataElemWidget("Manufacture year", row)
        row += 1
        self.__leBodyType = self.__addDataElemWidget("Body type", row)
        row += 1
        self.__leStateNumber = self.__addDataElemWidget("State number", row)
        row += 1
        self.__leOwnerDriver = self.__addDataElemWidget("Owner/Driver", row)

        carDataWidget.setLayout(self.__grdLayout)
        return carDataWidget

    def __addDataElemWidget(self, labelName, row):
        col = 0
        self.__grdLayout.addWidget(
            QLabel(self.tr(labelName)), row, col, self.__rowSpan, self.__colSpan
        )
        lineEdit = QLineEdit()
        col += 1
        self.__grdLayout.addWidget(lineEdit, row, col, self.__rowSpan, self.__colSpan)
        return lineEdit

    def __createButtons(self, parent=None):
        buttonsWidget = QWidget(parent)
        self.__addButton = QPushButton(self.tr("Add"), buttonsWidget)
        self.__cancelButton = QPushButton(self.tr("Cancel"), buttonsWidget)
        hbxLayout = QHBoxLayout()
        hbxLayout.addStretch(10)
        hbxLayout.addWidget(self.__addButton, 1)
        hbxLayout.addWidget(self.__cancelButton, 1)
        buttonsWidget.setLayout(hbxLayout)
        return buttonsWidget