import enum


class CarData(object):
    def __init__(
        self,
        brand=str(),
        model=str(),
        engineCap=str(),
        manufYear=str(),
        gosNum=str(),
        bodyType=str(),
        ownerDriver=str(),
    ):
        self.brand = brand
        self.model = model
        self.engineCapacity = engineCap
        self.manufactureYear = manufYear
        self.gosNumber = gosNum
        self.bodyType = bodyType
        self.ownerDriver = ownerDriver


class Classifier(enum.Enum):
    main_components_and_assemblies = 0
    materials = 1
    filters = 2
    liquids = 3
    electrics = 4


class ClassifierItem(object):
    def __init__(self, data=None, parentItem=None):
        self.__itemData = data
        self.__parentItem = parentItem
        self.__childItems = []

    def appendChild(self, child) -> None:
        self.__childItems.append(child)

    def child(self, row):
        if row < 0 or row >= self.__childItems.size():
            return None
        return self.__childItems.at(row)

    def childCount(self) -> int:
        return self.__childItems.count()

    def columnCount(self) -> int:
        return self.__itemData.count()

    def row(self) -> int:
        if self.__parentItem:
            return self.__parentItem.__childItems.indexOf(ClassifierItem(self))
        return int(0)

    def parentItem(self):
        return self.__parentItem

    def data(self, column):
        if column < 0 or column >= self.__itemData.size():
            return None
        return self.__itemData.at(column)
