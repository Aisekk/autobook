from PySide6.QtCore import QAbstractItemModel, QModelIndex
from data_store.structs import ClassifierItem


class ClassifierModel(QAbstractItemModel):
    def __init__(self, parent=None):
        QAbstractItemModel().__init__(parent)
        self.__root = ClassifierItem()

    def invisibleRootItem(self) -> ClassifierItem:
        return self.__root

    def addItems(self, parent: ClassifierItem, children: list[ClassifierItem]) -> None:
        parentIndex = QModelIndex()

        if parent != self.__root:
            parentOfParent = parent.parentItem()
            if parentOfParent == None:
                return
            parentIndex = self.createIndex(parentOfParent.childIndex(parent), 0, parent)

        self.beginInsertRows(
            parentIndex, parent.childCount(), parent.childCount() + children.size()
        )
        parent.addChildren(children)
        self.endInsertRows()