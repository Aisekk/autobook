import enum
import copy
from PySide6.QtCore import Qt

class ClassifierItemRole(enum.IntEnum):
    ItemType = Qt.ItemDataRole.UserRole
    ItemId = Qt.ItemDataRole.UserRole + 1


class ClassifierItem(object):
    def __init__(self, parent=None, data=list(), name=str()):
        self.id = 0
        self.name = name
        self.isGroup = False
        self.__parent: ClassifierItem = parent
        self.__itemData = data
        self.__children: list[ClassifierItem] = []

    def addChild(self, child) -> None:
        self.__children.append(child)

    def addChildren(self, children) -> None:
        for child in children:
            child.__parentItem = self
            self.__children.append(child)

    def getChildren(self) -> list:
        return self.__children

    def takeChildren(self) -> list:
        children = copy(self.__children)
        self.__children.clear()
        return children

    def child(self, index: int):
        if index < 0 or index >= len(self.__children):
            return None
        return self.__children[index]

    def childIndex(self, item) -> int:
        return self.__children.index(item)

    def childCount(self) -> int:
        return len(self.__children)

    def hasChildren(self) -> bool:
        return len(self.__children) == 0

    def columnCount(self) -> int:
        return len(self.__itemData)

    def row(self) -> int:
        if self.__parent:
            return self.__parent.__childItems.indexOf(ClassifierItem(self))
        return int(0)

    def parent(self):
        return self.__parent

    def data(self, column: int):
        if column < 0 or column >= len(self.__itemData):
            return None
        return self.__itemData.at(column)