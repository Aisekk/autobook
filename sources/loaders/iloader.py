from data_store.values import Values
from data_store.params import Params
from PySide6.QtCore import qDebug

class ILoader(object):
    def __init__(self) -> None:
        "ILoader"
        self.params = Params()
        self.__values = Values()
    
    def getParams(self) -> Params:
        "Return car params"
        return self.params

    def getValues(self) -> Values:
        "Return car values"
        return self.__values
    
    def loadValues(self) -> bool:
        "Load car values from data source"
        return False
    
    def loadParams(self) -> bool:
        "Load car parameters from data source" 
        if self.loadEngineParams():
            return True
        return False

    def loadEngineParams(self) -> bool:
        "Load engine parameters"
        return False
