from PySide6.QtCore import Qt, qDebug
from PySide6.QtGui import  QFont
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
    
)


class ControlWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.carDataDisplayWidget = self.createCarDataDisplayWidget(self)
        self.buttonsWidget = self.createButtons(self)
        self.leSearch = self.createSearchLineEdit(self)
        self.cbxClassificator = self.createClassificatorComboBox(self)
        vbxMainLayout = QVBoxLayout()
        vbxMainLayout.addWidget(self.carDataDisplayWidget, 10)
        vbxMainLayout.addWidget(self.buttonsWidget, 10)
        vbxMainLayout.addWidget(self.leSearch, 1)
        vbxMainLayout.addWidget(self.cbxClassificator, 1)
        vbxMainLayout.addStretch(30)
        self.setLayout(vbxMainLayout)

    def createCarDataDisplayWidget(self, parent=None):
        carGroupBox = QGroupBox(self.tr("Car"), parent)
        font = QFont("Arial", 10)
        font.setBold(True)
        carGroupBox.setFont(font)
        carGroupBox.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.brandLabel = QLabel("Hyundai")
        self.modelLabel = QLabel("Solaris")
        self.engineCapLabel = QLabel("1.6")
        self.manufYearLabel = QLabel("2012")
        self.gosNumLabel = QLabel("a555aa152rus")
        self.bodyTypeLabel = QLabel("Sedan")
        self.ownerDriverLabel = QLabel("Matreshkin Filipp")      
        vbxLayout = QVBoxLayout()
        vbxLayout.addWidget(self.brandLabel, 1, Qt.AlignmentFlag.AlignHCenter)
        vbxLayout.addWidget(self.modelLabel, 1, Qt.AlignmentFlag.AlignHCenter)
        vbxLayout.addWidget(self.engineCapLabel, 1, Qt.AlignmentFlag.AlignHCenter)
        vbxLayout.addWidget(self.manufYearLabel, 1, Qt.AlignmentFlag.AlignHCenter)
        vbxLayout.addWidget(self.gosNumLabel, 1, Qt.AlignmentFlag.AlignHCenter)
        vbxLayout.addWidget(self.bodyTypeLabel, 1, Qt.AlignmentFlag.AlignHCenter)
        vbxLayout.addWidget(self.ownerDriverLabel, 1, Qt.AlignmentFlag.AlignHCenter)
        carGroupBox.setLayout(vbxLayout)
        return carGroupBox

    def createButtons(self, parent=None):
        buttonsWidget = QWidget(parent)
        self.basicsButton = QPushButton(self.tr("Basics"), buttonsWidget)
        self.detailsButton = QPushButton(self.tr("Details"), buttonsWidget)
        self.numbersAndCodesButton = QPushButton(
            self.tr("Numbers and codes"), buttonsWidget
        )
        self.ownerDriverButton = QPushButton(self.tr("Owner/Driver"), buttonsWidget)
        vbxLayout = QVBoxLayout()
        vbxLayout.addWidget(self.basicsButton, 1)
        vbxLayout.addWidget(self.detailsButton, 1)
        vbxLayout.addWidget(self.numbersAndCodesButton, 1)
        vbxLayout.addWidget(self.ownerDriverButton, 1)
        buttonsWidget.setLayout(vbxLayout)
        return buttonsWidget

    def createSearchLineEdit(self, parent=None):
        searchLineEdit = QLineEdit(parent)
        searchLineEdit.setPlaceholderText(self.tr("Find") + "...")
        return searchLineEdit

    def createClassificatorComboBox(self, parent=None):
        cbxClassificator = QComboBox(parent)
        cbxClassificator.addItems(["Class 1", "Class 2"])
        return cbxClassificator