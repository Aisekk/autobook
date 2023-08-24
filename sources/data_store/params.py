
class EngineParams(object):
    def __init__(self) -> None:
        self.fuelCombustionTypes: dict(int, str) = {}
        self.designTypes: dict(int, str) = {}
        self.cylinderArrangements: dict(int, str) = {}
        self.cylindersNumbers: dict(int, str) = {}
        self.fuelTypes: dict(int, str) = {}
        self.tactValues: dict(int, str) = {}
        self.combustibleMixtureFormations: dict(int, str) = {}
        self.coolingSystems: dict(int, str) = {}
        self.gdmDriveDesigns: dict(int, str) = {}
        self.locations: dict(int, str) = {}
        self.airPressureValues: dict(int, str) = {}

class Params(object):
    def __init__(self) -> None:
        self.engineParams = EngineParams()