import copy
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
    def __init__(self, data: list = None, parentItem=None):
        self.id = 0
        self.__itemData = data
        self.__parentItem = parentItem
        self.__children: list[ClassifierItem] = []

    def addChild(self, child) -> None:
        self.__children.append(child)

    def addChildren(self, children: list) -> None:
        for child in children:
            child.__parentItem = self
            self.__children.append(child)

    def getChildren(self) -> list:
        return self.__children

    def takeChildren(self) -> list:
        children = copy(self.__children)
        self.__children.clear()
        return children

    def child(self, index: int):  # -> ClassifierItem:
        if index < 0 or index >= self.__children.size():
            return None
        return self.__children.at(index)

    def childIndex(self, item) -> int:
        return self.__children.index(item)

    def childCount(self) -> int:
        return self.__children.count()

    def hasChildren(self) -> bool:
        return self.__children.count() == 0

    def columnCount(self) -> int:
        return self.__itemData.count()

    def row(self) -> int:
        if self.__parentItem:
            return self.__parentItem.__childItems.indexOf(ClassifierItem(self))
        return int(0)

    def parentItem(self):
        return self.__parentItem

    def data(self, column: int):
        if column < 0 or column >= self.__itemData.size():
            return None
        return self.__itemData.at(column)
