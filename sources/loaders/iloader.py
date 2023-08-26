from data_store.values import Values
from data_store.params import Params
from PySide6.QtCore import qDebug

class ILoader(object):
    def __init__(self) -> None:
        "ILoader"
        self._params = Params()
        self._values = Values()
    
    def getParams(self) -> Params:
        "Return car params"
        return self._params

    def getValues(self) -> Values:
        "Return car values"
        return self._values
    
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
