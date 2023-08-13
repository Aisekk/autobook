from PySide6.QtCore import qDebug
from PySide6.QtCore import QCoreApplication

import data_store.structs as structs
import data_store.const_info as const_info
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

    def getItems(self, classifier, parent: ClassifierItem) -> list[ClassifierItem]:
        items = []
        mc = const_info.main_components
        if classifier == structs.Classifier.MainComponentsAndAssemblies:
            for index, name in mc.items():
                if index < structs.MainComponents.Engine:
                    item = ClassifierItem(parent, index, name)
                    if (
                        index == structs.MainComponents.Body
                        or index == structs.MainComponents.Steering
                    ):
                        item.isGroup = False
                    else:
                        item.isGroup = True
                    items.append(item)
            for item in items:
                children = self.__getMainComponentsItems(item)
                item.addChildren(children)
        return items

    def __getMainComponentsItems(self, parent: ClassifierItem):
        items = []
        ids = []
        
        if parent.id == structs.MainComponents.EngineAndItsSystems:
            ids = [
                structs.MainComponents.Engine,
                structs.MainComponents.PowerSystem,
                structs.MainComponents.CoolingSystem,
                structs.MainComponents.LubricationSystem,
                structs.MainComponents.ExhaustSystem,
            ]
        elif parent.id == structs.MainComponents.TransmissionSystem:
            ids = [
                structs.MainComponents.Clutch,
                structs.MainComponents.Gearbox,
                structs.MainComponents.WheelDrive,
            ]
        elif parent.id == structs.MainComponents.Chassis:
            ids = [
                structs.MainComponents.FrontSuspension,
                structs.MainComponents.RearSuspension,
                structs.MainComponents.Wheels,
                structs.MainComponents.Tires,
            ]
        elif parent.id == structs.MainComponents.Body:
            ids = []
        elif parent.id == structs.MainComponents.Steering:
            ids = []
        elif parent.id == structs.MainComponents.BrakeSystem:
            ids = [
                structs.MainComponents.ServiceBrakeSystem,
                structs.MainComponents.ParkingBrakeSystem,
            ]
        elif parent.id == structs.MainComponents.ElectricalEquipment:
            ids = [
                structs.MainComponents.ElectricitySources,
                structs.MainComponents.ElectricityConsumers,
            ]
        elif parent.id == structs.MainComponents.AdditionalEquipment:
            ids = []

        mc = const_info.main_components
        for id in ids:
            item = ClassifierItem(parent, id, mc.get(id))
            items.append(item)

        return items
