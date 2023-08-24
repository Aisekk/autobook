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
            self.__readParams(
                jsonEngineObject,
                "FuelCombustionType",
                self.__engineParams.fuelCombustionTypes,
            )
            self.__readParams(
                jsonEngineObject, "DesignType", self.__engineParams.designTypes
            )
            self.__readParams(
                jsonEngineObject,
                "CylinderArrangement",
                self.__engineParams.cylinderArrangements,
            )
            self.__readParams(
                jsonEngineObject,
                "CylindersNumber",
                self.__engineParams.cylindersNumbers,
            )
            self.__readParams(
                jsonEngineObject, "FuelType", self.__engineParams.fuelTypes
            )
            self.__readParams(jsonEngineObject, "Tact", self.__engineParams.tactValues)
            self.__readParams(
                jsonEngineObject,
                "CombustibleMixtureFormation",
                self.__engineParams.combustibleMixtureFormations,
            )
            self.__readParams(
                jsonEngineObject, "CoolingSystem", self.__engineParams.coolingSystems
            )
            self.__readParams(
                jsonEngineObject, "GdmDriveDesign", self.__engineParams.gdmDriveDesigns
            )
            self.__readParams(
                jsonEngineObject, "Location", self.__engineParams.locations
            )
            self.__readParams(
                jsonEngineObject, "AirPressure", self.__engineParams.airPressureValues
            )
        self.params.engineParams = self.__engineParams
        file.close()

    def __readParams(self, jsonEngineObject, key, params):
        if jsonEngineObject.__contains__(key):
            source: list = jsonEngineObject.get(key)
            # print(source)
            params = self.__fillParams(source)
            print(params)

    def __fillParams(self, source: list) -> dict:
        params = {}
        for item in source:
            params[item.get("id")] = item.get("name")
        return params

    def __output(self, params):
        for key, val in params.items():
            qDebug(str(key) + ": " + val)