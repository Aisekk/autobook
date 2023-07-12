from PySide6.QtCore import qDebug
from PySide6.QtCore import QCoreApplication

import data_store.structs


class AutobookDataStore(object):
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(AutobookDataStore, cls).__new__(cls)
            cls.__initialize(cls)
        return cls.instance

    def __initialize(cls):
        cls.__carData = data_store.structs.CarData("Huyndai", "Solaris")
        cls.__context = "AutobookDataStore"
        qDebug("singleton")

    def getCarData(self) -> data_store.structs.CarData:
        return self.__carData

    def getDefaultCarData(self) -> data_store.structs.CarData:
        # return data_store.structs.CarData(
        #    "Huyndai", "Solaris", "1.6L", "2012", "A123BC 152 RUS", "Sedan", "Ivanov A.S."
        # )
        return data_store.structs.CarData(
            str(QCoreApplication.translate(self.__context, "Brand")),
            str(QCoreApplication.translate(self.__context, "Model")),
            str(QCoreApplication.translate(self.__context, "Engine capacity, L")),
            str(QCoreApplication.translate(self.__context, "Manufacture year")),
            str(QCoreApplication.translate(self.__context, "State number")),
            str(QCoreApplication.translate(self.__context, "Body type")),
            str(QCoreApplication.translate(self.__context, "Owner/Driver")),
        )
