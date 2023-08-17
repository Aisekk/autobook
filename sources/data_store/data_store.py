from PySide6.QtCore import qDebug
from PySide6.QtCore import QCoreApplication, QDir

import data_store.values as vals
import data_store.enums as enums
import data_store.const_info as const_info
from items.classifier_item import ClassifierItem
import loaders.json_loader


class AutobookDataStore(object):
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(AutobookDataStore, cls).__new__(cls)
            cls.__initialize(cls)
        return cls.instance

    def __initialize(cls):
        cls.__values = vals.Values("Huyndai", "Solaris")
        cls.__context = "AutobookDataStore"

        cls.__mainPath = QDir.currentPath()
        cls.__loader = loaders.json_loader.JsonLoader(cls.__mainPath)
        cls.__loader.loadParams()

    def getValues(self) -> vals.Values:
        return self.__values

    def getDefaultValues(self) -> vals.Values:
        # return structs.Values(
        #   "Huyndai", "Solaris", "1.6L", "2012", "A123BC 152 RUS", "Sedan", "Ivanov A.S."
        # )
        return vals.Values(
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
        if classifier == enums.Classifier.MainComponentsAndAssemblies:
            for index, name in mc.items():
                if index < enums.MainComponent.Engine:
                    item = ClassifierItem(parent, index, name)
                    if (
                        index == enums.MainComponent.Body
                        or index == enums.MainComponent.Steering
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

        if parent.id == enums.MainComponent.EngineAndItsSystems:
            ids = [
                enums.MainComponent.Engine,
                enums.MainComponent.PowerSystem,
                enums.MainComponent.CoolingSystem,
                enums.MainComponent.LubricationSystem,
                enums.MainComponent.ExhaustSystem,
            ]
        elif parent.id == enums.MainComponent.TransmissionSystem:
            ids = [
                enums.MainComponent.Clutch,
                enums.MainComponent.Gearbox,
                enums.MainComponent.WheelDrive,
            ]
        elif parent.id == enums.MainComponent.Chassis:
            ids = [
                enums.MainComponent.FrontSuspension,
                enums.MainComponent.RearSuspension,
                enums.MainComponent.Wheels,
                enums.MainComponent.Tires,
            ]
        elif parent.id == enums.MainComponent.Body:
            ids = []
        elif parent.id == enums.MainComponent.Steering:
            ids = []
        elif parent.id == enums.MainComponent.BrakeSystem:
            ids = [
                enums.MainComponent.ServiceBrakeSystem,
                enums.MainComponent.ParkingBrakeSystem,
            ]
        elif parent.id == enums.MainComponent.ElectricalEquipment:
            ids = [
                enums.MainComponent.ElectricitySources,
                enums.MainComponent.ElectricityConsumers,
            ]
        elif parent.id == enums.MainComponent.AdditionalEquipment:
            ids = []

        mc = const_info.main_components
        for id in ids:
            item = ClassifierItem(parent, id, mc.get(id))
            items.append(item)

        return items
