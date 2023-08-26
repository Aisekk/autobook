
class Values(object):
    def __init__(
        self,
        brand=str(),
        model=str(),
        engineCap=str(),
        manufYear=str(),
        gosNum=str(),
        bodyType=str(),
        ownerDriver=str(),
    ):
        self.brand = brand
        self.model = model
        self.engineCapacity = engineCap
        self.manufactureYear = manufYear
        self.gosNumber = gosNum
        self.bodyType = bodyType
        self.ownerDriver = ownerDriver


class Engine(object):
    def __init__(self, capacity=str(), manufCountry = str()):
        self.capacity = capacity
        self.manufCountry = manufCountry
        self.fuelCombustionTypeId = int(-1)
        self.designTypeId = int(-1)
        self.cylinderArrangementId = int(-1)
        self.cylindersNumberId = int(-1)
        self.fuelTypeId = int(-1)
        self.tactId = int(-1)
        self.combustibleMixtureFormationId = int(-1)
        self.coolingSystemId = int(-1)
        self.gdmDriveDesignId = int(-1)
        self.locationId = int(-1)
        self.airPressureId = int(-1)
