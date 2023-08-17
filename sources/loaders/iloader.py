import data_store.values as vals
import data_store.params as params

class ILoader(object):
    def __init__(self) -> None:
        "ILoader"
        #self.engineParams: params.EngineParams()
    
    def getParams():
        "Return car values"

    def getValues():
        "Return car values"
    
    def loadValues(self) -> bool:
        "Load car values from data source"
        return False
    
    def loadParams(self) -> bool:
        "Load car parameters from data source"
        #self.engineParams = 
        self.loadEngineParams()
        return False

    def loadEngineParams(self) -> bool:
        "Load engine parameters"
        return False
