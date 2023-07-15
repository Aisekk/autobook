#from typing_extensions import override
from PySide6.QtCore import QAbstractItemModel, QModelIndex, Qt
from data_store.structs import ClassifierItem, ClassifierItemRole


class ClassifierModel(QAbstractItemModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        #QAbstractItemModel().__init__(parent)
        self.__root = ClassifierItem([])

    def invisibleRootItem(self) -> ClassifierItem:
        return self.__root

    def addItems(self, parent: ClassifierItem, children: list[ClassifierItem]) -> None:
        parentIndex = QModelIndex()
        if parent != self.__root:
            parentOfParent = parent.parent()
            if not parentOfParent:
                return
            parentIndex = self.createIndex(parentOfParent.childIndex(parent), 0, parent)

        self.beginInsertRows(
            parentIndex, parent.childCount(), parent.childCount() + len(children)
        )
        parent.addChildren(children)
        self.endInsertRows()

    def takeItemChildren(self, item: ClassifierItem) -> list[ClassifierItem]:
        itemIndex = QModelIndex()
        if item != self.__root:
            parent: ClassifierItem = item.parent()
            if parent == None:
                return []
            itemIndex = self.createIndex(parent.childIndex(item), 0, item)

        self.beginRemoveRows(itemIndex, 0, item.childCount() - 1)
        result = item.takeChildren()
        self.endRemoveRows()
        return result

    #@override
    def data(self, index: QModelIndex, role: int) -> object: 
        result = None
        if not index.isValid():
            return result
        item = ClassifierItem(index.internalPointer())
        if not item:
            return result
        if role == Qt.ItemDataRole.DisplayRole or role == Qt.ItemDataRole.ToolTipRole:
            if index.column() == 0:
                result = item.name
        elif role == ClassifierItemRole.ItemId:
            if index.column() == 0:
                result = item.id
        return result

    #@override
    def flags(index: QModelIndex) -> Qt.ItemFlag:
        return Qt.ItemFlag.ItemIsSelectable # or Qt.ItemFlag.ItemIsEnabled

    #@override
    def index(self, row: int, column: int, parent = QModelIndex()) -> QModelIndex:
        if not self.hasIndex(row, column, parent):
            return QModelIndex()
        parentItem = ClassifierItem()
        if not parent.isValid():
            parentItem = self.__root
        else:
            parentItem = ClassifierItem(parent.internalPointer())
        childItem = parentItem.child(row)
        if childItem:
            return self.createIndex(row, column, childItem)
        return QModelIndex()

    #@override
    def parent(self, index: QModelIndex) -> QModelIndex:
        if not index.isValid():
            return QModelIndex()
        childItem = ClassifierItem(index.internalPointer())
        parentItem = childItem.parent()
        if parentItem == self.__root:
            return QModelIndex()
        parentOfParent = parentItem.parent()
        if not parentOfParent:
            return QModelIndex()
        return self.createIndex(parentOfParent.childIndex(parentItem), 0, parentItem)

    #@override
    def rowCount(self, parent = QModelIndex()) -> int:
        parentItem = ClassifierItem()
        if parent.column() > 0:
            return 0
        if not parent.isValid():
            parentItem = self.__root
        else:
            parentItem = ClassifierItem(parent.internalPointer())
        return parentItem.childCount()

    #@override
    def columnCount(self, parent = QModelIndex()) -> int:
        return 1

