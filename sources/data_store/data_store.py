from PySide6.QtCore import qDebug
from PySide6.QtCore import QCoreApplication

import data_store.structs as structs
from items.classifier_item import ClassifierItem, ClassifierItemRole


class AutobookDataStore(object):
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(AutobookDataStore, cls).__new__(cls)
            cls.__initialize(cls)
        return cls.instance

    def __initialize(cls):
        cls.__carData = structs.CarData("Huyndai", "Solaris")
        cls.__context = "AutobookDataStore"
        qDebug("singleton")

    def getCarData(self) -> structs.CarData:
        return self.__carData

    def getDefaultCarData(self) -> structs.CarData:
        # return data_store.structs.CarData(
        #    "Huyndai", "Solaris", "1.6L", "2012", "A123BC 152 RUS", "Sedan", "Ivanov A.S."
        # )
        return structs.CarData(
            str(QCoreApplication.translate(self.__context, "Brand")),
            str(QCoreApplication.translate(self.__context, "Model")),
            str(QCoreApplication.translate(self.__context, "Engine capacity, L")),
            str(QCoreApplication.translate(self.__context, "Manufacture year")),
            str(QCoreApplication.translate(self.__context, "State number")),
            str(QCoreApplication.translate(self.__context, "Body type")),
            str(QCoreApplication.translate(self.__context, "Owner/Driver")),
        )

    def getItems(classifier, parent) -> list[ClassifierItem]:
        items = []
        if classifier == structs.Classifier.MainComponentsAndAssemblies:
            for i in range(3):
                item = ClassifierItem(parent)
                item.name = "item " + str(i)
                items.append(item)
            child = ClassifierItem(items[0], [], "child 0")
            child1 = ClassifierItem(items[0], [], "child 1")
            items[0].addChild(child1)
            qDebug("child name: " + items[0].child(0).name)
        return items