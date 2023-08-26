from typing_extensions import override
from loaders.iloader import ILoader
from data_store.params import EngineParams

from PySide6.QtCore import (
    QCoreApplication,
    QIODevice,
    QFile,
    QJsonDocument,
    qDebug,
)


class JsonLoader(ILoader):
    def __init__(self, path: str) -> None:
        super().__init__()
        self.__mainPath = path
        self.__engineParams = EngineParams()

    @override
    def loadEngineParams(self) -> bool:
        filePath = self.__mainPath + "/resources/configs/engine.json"
        qDebug(filePath)
        if not QFile.exists(filePath):
            return False
        file = QFile(filePath)
        if not file.open(QIODevice.ReadOnly):
            return False
        data = file.readAll()
        if data.isEmpty():
            return False
        doc = QJsonDocument.fromJson(data)
        if doc.isEmpty():
            return False
        if doc.isObject():
            jsonEngineObject = doc.object()
            self.__engineParams.fuelCombustionTypes = self.__readParams(
                jsonEngineObject, "FuelCombustionType"
            )
            self.__engineParams.designTypes = self.__readParams(
                jsonEngineObject, "DesignType"
            )
            self.__engineParams.cylinderArrangements = self.__readParams(
                jsonEngineObject, "CylinderArrangement"
            )
            self.__engineParams.cylindersNumbers = self.__readParams(
                jsonEngineObject, "CylindersNumber"
            )
            self.__engineParams.fuelTypes = self.__readParams(
                jsonEngineObject, "FuelType"
            )
            self.__engineParams.tactValues = self.__readParams(jsonEngineObject, "Tact")
            self.__engineParams.combustibleMixtureFormations = self.__readParams(
                jsonEngineObject, "CombustibleMixtureFormation"
            )
            self.__engineParams.coolingSystems = self.__readParams(
                jsonEngineObject, "CoolingSystem"
            )
            self.__engineParams.gdmDriveDesigns = self.__readParams(
                jsonEngineObject, "GdmDriveDesign"
            )
            self.__engineParams.locations = self.__readParams(
                jsonEngineObject, "Location"
            )
            self.__engineParams.airPressureValues = self.__readParams(
                jsonEngineObject, "AirPressure"
            )
        self._params.engineParams = self.__engineParams
        # qDebug("len fct = " + str(len(self.params.engineParams.fuelCombustionTypes)))
        file.close()
        return True

    def __readParams(self, jsonEngineObject, key):
        if jsonEngineObject.__contains__(key):
            source: list = jsonEngineObject.get(key)
            return self.__fillParams(source)

    def __fillParams(self, source: list) -> dict:
        params = {}
        for item in source:
            params[item.get("id")] = item.get("name")
        return params

    def __output(self, params):
        for key, val in params.items():
            qDebug(str(key) + ": " + val)