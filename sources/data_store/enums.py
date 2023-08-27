import enum
from PySide6.QtCore import Qt


class Classifier(enum.IntEnum):
    MainComponentsAndAssemblies = 0
    Mechanisms = 1
    Materials = 2
    Filters = 3
    Liquids = 4
    Electrics = 5


class ClassifierItemRole(enum.IntEnum):
    ItemType = Qt.ItemDataRole.UserRole
    ItemId = Qt.ItemDataRole.UserRole + 1


class MainComponent(enum.IntEnum):
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


class WidgetIndex(enum.IntEnum):
    Empty = 0
    # Records = 1
    # Parameters = 2
    # NumbersAndCodes = 3
    # Owner = 4
    Engine = 1
    PowerSystem = 6
    CoolingSystem = 7
    LubricationSystem = 8
    ExhaustSystem = 9
    Clutch = 10
    Gearbox = 11
    WheelDrive = 12
    FrontSuspension = 13
    RearSuspension = 14
    Wheels = 15
    Tires = 16
    Body = 17
    Steering = 18
    ServiceBrakeSystem = 19
    ParkingBrakeSystem = 20
    ElectricitySources = 21
    ElectricityConsumers = 22