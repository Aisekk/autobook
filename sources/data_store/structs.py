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


class MainComponents(enum.IntEnum):
    EngineAndItsSystems = 0
    TransmissionSystem = 1
    Chassis = 2
    Body = 3
    Steering = 4
    BrakeSystem = 5
    ElectricalEquipment = 6
    AdditionalEquipment = 7
    Engine = 8
    PowerSystem = 9
    CoolingSystem = 10
    LubricationSystem = 11
    ExhaustSystem = 12
    Clutch = 13
    Gearbox = 14
    WheelDrive = 15
    FrontSuspension = 16
    RearSuspension = 17
    Wheels = 18
    Tires = 19
    ServiceBrakeSystem = 20
    ParkingBrakeSystem = 21
    ElectricitySources = 22
    ElectricityConsumers = 23
