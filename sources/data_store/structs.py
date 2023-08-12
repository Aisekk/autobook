import enum


class CarData(object):
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


class Classifier(enum.IntEnum):
    MainComponentsAndAssemblies = 0
    Mechanisms = 1
    Materials = 2
    Filters = 3
    Liquids = 4
    Electrics = 5

class Groups(enum.IntEnum):
    EngineAndItsSystems = 0
    TransmissionSystem = 1
    Chassis = 2
    Body = 3
    Steering = 4
    BrakeSystem = 5
    ElectricalEquipment = 6
    AdditionalEquipment = 7

class MainComponents(enum.IntEnum):
    Engine = 0    
    PowerSystem = 1
    CoolingSystem = 2
    LubricationSystem = 3
    ExhaustSystem = 4    
    Clutch = 5
    Gearbox = 6
    WheelDrive = 7
    FrontSuspension = 8
    RearSuspension = 9
    Wheels = 10
    Tires = 11
    ServiceBrakeSystem = 12
    ParkingBrakeSystem = 13
    ElectricitySources = 14
    ElectricityConsumers = 15
