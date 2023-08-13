from PySide6.QtWidgets import (
    QWidget,
    QLineEdit,
    QComboBox,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
)
from PySide6.QtGui import QDoubleValidator


class EngineWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.__leCapacity = QLineEdit()
        validator = QDoubleValidator(0.0, 1.0e10, 10, self.__leCapacity)
        self.__leCapacity.setValidator(validator)

        self.__cbxFuelCombustionTypes = self.__createComboBox()
        self.__cbxDesignTypes = self.__createComboBox()
        self.__cbxCylinderArrangement = self.__createComboBox()
        self.__cbxCylindersNumber = self.__createComboBox()
        self.__cbxFuelType = self.__createComboBox()
        self.__cbxTact = self.__createComboBox()
        self.__cbxCombustibleMixtureFormation = self.__createComboBox()
        self.__cbxCoolingSystem = self.__createComboBox()
        self.__cbxGdmDriveDesign = self.__createComboBox()
        self.__cbxLocation = self.__createComboBox()
        self.__cbxAirPressure = self.__createComboBox()

        capacityWidget = self.__createParamWidget(
            self, self.tr("Engine capacity, l"), self.__leCapacity
        )
        fuelCombustionTypesWidget = self.__createParamWidget(
            self, self.tr("Fuel combustion type"), self.__cbxFuelCombustionTypes
        )
        designTypesWidget = self.__createParamWidget(
            self, self.tr("Design type"), self.__cbxDesignTypes
        )
        cylinderArrangementWidget = self.__createParamWidget(
            self, self.tr("Cylinder arrangement"), self.__cbxCylinderArrangement
        )
        cylindersNumberWidget = self.__createParamWidget(
            self, self.tr("Cylinders number"), self.__cbxCylindersNumber
        )
        fuelTypeWidget = self.__createParamWidget(
            self, self.tr("Fuel type"), self.__cbxFuelType
        )
        tactWidget = self.__createParamWidget(self, self.tr("Tact"), self.__cbxTact)
        combustibleMixtureFormationWidget = self.__createParamWidget(
            self,
            self.tr("Combustible mixture formation"),
            self.__cbxCombustibleMixtureFormation,
        )
        coolingSystemWidget = self.__createParamWidget(
            self, self.tr("Cooling system"), self.__cbxCoolingSystem
        )
        gdmDriveDesignWidget = self.__createParamWidget(
            self, self.tr("GDM Drive design"), self.__cbxGdmDriveDesign
        )
        locationWidget = self.__createParamWidget(
            self, self.tr("Location"), self.__cbxLocation
        )
        airPressureWidget = self.__createParamWidget(
            self, self.tr("Air pressure"), self.__cbxAirPressure
        )

        vbxLayout = QVBoxLayout()
        vbxLayout.addWidget(capacityWidget, 1)
        vbxLayout.addWidget(fuelCombustionTypesWidget, 1)
        vbxLayout.addWidget(designTypesWidget, 1)
        vbxLayout.addWidget(cylinderArrangementWidget, 1)
        vbxLayout.addWidget(cylindersNumberWidget, 1)
        vbxLayout.addWidget(fuelTypeWidget, 1)
        vbxLayout.addWidget(tactWidget, 1)
        vbxLayout.addWidget(combustibleMixtureFormationWidget, 1)
        vbxLayout.addWidget(coolingSystemWidget, 1)
        vbxLayout.addWidget(gdmDriveDesignWidget, 1)
        vbxLayout.addWidget(locationWidget, 1)
        vbxLayout.addWidget(airPressureWidget, 1)
        vbxLayout.addStretch(20)

        self.setLayout(vbxLayout)

    def __createComboBox(self, parent=None) -> QComboBox:
        comboBox = QComboBox(parent)
        return comboBox

    def __createParamWidget(self, parent, text: str, dataWidget) -> QWidget:
        widget = QWidget(parent)
        hbxLayout = QHBoxLayout()
        hbxLayout.addWidget(QLabel(text, widget), 15)
        hbxLayout.addWidget(dataWidget, 25)
        hbxLayout.addStretch(30)
        widget.setLayout(hbxLayout)
        return widget