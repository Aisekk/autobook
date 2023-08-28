#from __future__ import annotations
from data_store.values import Values
from data_store.params import Params
from PySide6.QtCore import qDebug

class ILoader:
    def __init__(self) -> None:
        "ILoader"
        self._params = Params()
        self._values = Values()
    
    #@const_method
    def getParams(self) -> Params:
        "Return car params"
        return self._params

    def getValues(self) -> Values:
        "Return car values"
        return self._values
    
    def loadValues(self) -> bool:
        "Load car values from data source"
        if self.loadEngineValues():
            return True
        return False
    
    def loadParams(self) -> bool:
        "Load car parameters from data source" 
        if self.loadEngineParams():
            return True
        return False

    def loadEngineParams(self) -> bool:
        "Load engine parameters"
        return False

    def loadEngineValues(self) -> bool:
        "Load engine values"
        return False