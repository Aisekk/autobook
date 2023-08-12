import data_store.structs as s

classifiers = {
    s.Classifier.MainComponentsAndAssemblies: "Main components and assemblies",
    s.Classifier.Mechanisms: "Mechanisms",
    s.Classifier.Materials: "Materials",
    s.Classifier.Filters: "Filters",
    s.Classifier.Liquids: "Liquids",
    s.Classifier.Electrics: "Electrics",
}

groups = {
    s.Groups.EngineAndItsSystems: "EngineAndItsSystems",
    s.Groups.TransmissionSystem: "TransmissionSystem",
    s.Groups.Chassis: "Chassis",
    s.Groups.Body: "Body",
    s.Groups.Steering: "Steering",
    s.Groups.BrakeSystem: "BrakeSystem",
    s.Groups.ElectricalEquipment: "ElectricalEquipment",
    s.Groups.AdditionalEquipment: "AdditionalEquipment",
}

main_components = {
    s.MainComponents.Engine: "Engine",
    s.MainComponents.PowerSystem: "Power system",
    s.MainComponents.CoolingSystem: "Cooling system",
    s.MainComponents.LubricationSystem: "Lubrication system",
    s.MainComponents.ExhaustSystem: "Exhaust system",
    s.MainComponents.Clutch: "Clutch",
    s.MainComponents.Gearbox: "Gearbox",
    s.MainComponents.WheelDrive: "Wheel drive",
    s.MainComponents.FrontSuspension: "Front suspension",
    s.MainComponents.RearSuspension: "Rear suspension",
    s.MainComponents.Wheels: "Wheels",
    s.MainComponents.Tires: "Tires",
    s.MainComponents.ServiceBrakeSystem: "Service brake system",
    s.MainComponents.ParkingBrakeSystem: "Parking brake system",
    s.MainComponents.ElectricitySources: "Electricity sources",
    s.MainComponents.ElectricityConsumers: "Electricity consumers",
}