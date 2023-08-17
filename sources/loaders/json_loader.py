from typing_extensions import override
from loaders.iloader import ILoader

from PySide6.QtCore import (
    QCoreApplication,
    QIODevice,
    QFile,
    QJsonDocument,
    QJsonArray,
    QJsonValue,
    qDebug,
)


class JsonLoader(ILoader):
    def __init__(self, path: str) -> None:
        super().__init__()
        self.__mainPath = path

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
            if jsonEngineObject.__contains__("FuelCombustionTypes"):
                jsonEngineValue = jsonEngineObject.get("FuelCombustionTypes")
                print(jsonEngineValue)
                qDebug("read")
                #for val in jsonEngineValue:
                 #   qDebug(val.get("id"))
                #if jsonEngineValue.isArray():
                 #   qDebug("read")

        file.close()
        return True