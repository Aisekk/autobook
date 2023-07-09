from PySide6.QtCore import QSize, qDebug
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
        self.carDataWidget = self.createCarDataWidget(self)
        self.buttonsWidget = self.createButtons(self)
        vbxMainLayout = QVBoxLayout()
        vbxMainLayout.addWidget(self.carDataWidget, 10)
        vbxMainLayout.addStretch(10)
        vbxMainLayout.addWidget(self.buttonsWidget, 1)
        self.setLayout(vbxMainLayout)

    def createCarDataWidget(self, parent=None):
        carDataWidget = QWidget(parent)
        self.grdLayout = QGridLayout()
        self.rowSpan = 1
        self.colSpan = 1

        row = 0
        self.leBrand = self.addDataElemWidget("Brand*", row)
        row += 1
        self.leModel = self.addDataElemWidget("Model*", row)
        row += 1
        self.leEngineCapacity = self.addDataElemWidget("Engine capacity, l", row)
        row += 1
        self.leManufactureYear = self.addDataElemWidget("Manufacture year", row)
        row += 1
        self.leBodyType = self.addDataElemWidget("Body type", row)
        row += 1
        self.leStateNumber = self.addDataElemWidget("State number", row)
        row += 1
        self.leOwnerDriver = self.addDataElemWidget("Owner/Driver", row)

        carDataWidget.setLayout(self.grdLayout)
        return carDataWidget

    def addDataElemWidget(self, labelName, row):
        col = 0
        self.grdLayout.addWidget(
            QLabel(self.tr(labelName)), row, col, self.rowSpan, self.colSpan
        )
        lineEdit = QLineEdit()
        col += 1
        self.grdLayout.addWidget(lineEdit, row, col, self.rowSpan, self.colSpan)
        return lineEdit

    def createButtons(self, parent=None):
        buttonsWidget = QWidget(parent)
        self.addButton = QPushButton(self.tr("Add"), buttonsWidget)
        self.cancelButton = QPushButton(self.tr("Cancel"), buttonsWidget)
        hbxLayout = QHBoxLayout()
        hbxLayout.addStretch(10)
        hbxLayout.addWidget(self.addButton, 1)
        hbxLayout.addWidget(self.cancelButton, 1)
        buttonsWidget.setLayout(hbxLayout)
        return buttonsWidget