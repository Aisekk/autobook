import data_store.values as vals
import data_store.params as params

class ILoader(object):
    def __init__(self) -> None:
        super.__init__()
        self.engineParams: params.EngineParams()

    def loadValues(self):
        "Load values: car data"
    
    def loadParams(self):
        "Load car parameters"
        self.engineParams = self.loadEngineParams()

    #def loadComponentParams(self, component: structs.MainComponents):
    #    "Load component parameters"
    #    if component == structs.MainComponents.Engine:
    #        self.loadEngineParams()

    def loadEngineParams(self):
        "Load engine parameters"
