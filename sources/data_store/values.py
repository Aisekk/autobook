
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
    def __init__(self, capacity=str()):
        self.capacity = capacity
