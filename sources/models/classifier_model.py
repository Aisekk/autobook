from typing_extensions import override
from PySide6.QtCore import QAbstractItemModel, QModelIndex, Qt, qDebug
from items.classifier_item import ClassifierItem
from data_store.enums import ClassifierItemRole

class ClassifierModel(QAbstractItemModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__root = ClassifierItem()
        self.__root.name = "root"
        self.__root.id = -1

    def invisibleRootItem(self) -> ClassifierItem:
        return self.__root

    def addItems(self, parent: ClassifierItem, children: list[ClassifierItem]) -> None:
        parentIndex = QModelIndex()
        if parent != self.__root:
            parentOfParent = parent.parent()
            if parentOfParent == None:
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

    @override
    def data(self, index: QModelIndex, role: int = Qt.ItemDataRole.DisplayRole):
        result = None
        if not index.isValid():
            return result
        item = index.internalPointer()
        if not item:
            return result
        if role == Qt.ItemDataRole.DisplayRole or role == Qt.ItemDataRole.ToolTipRole:
            if index.column() == 0:
                return self.tr(item.name)
        elif role == ClassifierItemRole.ItemId:
            if index.column() == 0:
                result = item.id
        return result

    @override
    def flags(self, index: QModelIndex) -> Qt.ItemFlag:
        return Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled

    @override
    def index(self, row: int, column: int, parent=QModelIndex()) -> QModelIndex:
        if not self.hasIndex(row, column, parent):
            return QModelIndex()
        if not parent.isValid():
            parentItem = self.__root
        else:
            parentItem = parent.internalPointer()
        childItem = parentItem.child(row)
        if childItem:
            return self.createIndex(row, column, childItem)
        return QModelIndex()

    @override
    def parent(self, index: QModelIndex) -> QModelIndex:
        if not index.isValid():
            return QModelIndex()
        childItem = index.internalPointer()
        parentItem = childItem.parent()
        if parentItem == self.__root or parentItem == None:
            return QModelIndex()
        parentOfParent = parentItem.parent()
        if parentOfParent == None:
            return QModelIndex()
        return self.createIndex(parentOfParent.childIndex(parentItem), 0, parentItem)

    @override
    def rowCount(self, parent=QModelIndex()) -> int:
        parentItem = ClassifierItem()
        if parent.column() > 0:
            return 0
        if not parent.isValid():
            parentItem = self.__root
        else:
            parentItem = parent.internalPointer()
        return parentItem.childCount()

    @override
    def columnCount(self, parent=QModelIndex()) -> int:
        return 1
