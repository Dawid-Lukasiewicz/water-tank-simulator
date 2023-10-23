from enum import Enum

class PumpType(Enum):
    IN_PUMP = 0
    OUT_PUMP = 1

class Tank:
    # capacity = 0
    # waterLevel = 0
    # waterTemp = 0
    # heaterState = False
    # pumpOutState = False
    # pumpInState = False

    def __init__(self
                 ,capacity = 20.0
                 ,waterLevel = 0.0
                 ,ambientTemp = 20.0
                 ,waterTemp = 20.0
                 ,heaterState = False
                 ,pumpInState = False
                 ,pumpOutState = False):
        self.capacity       = capacity
        self.waterLevel     = waterLevel
        self.ambientTemp    = ambientTemp
        self.waterTemp      = waterTemp
        self.heaterState    = heaterState
        self.pumpInState    = pumpInState
        self.pumpOutState   = pumpOutState

    def setHeater(self, state: bool) -> None:
        self.heaterState = state
    def setPump(self, pump: PumpType, pumpState: bool) -> None:
        if pump == PumpType.IN_PUMP:
            self.pumpInState = pumpState
        else:
            self.pumpOutState = pumpState

    def getTemperature(self) -> float:
        return self.waterTemp
    
    def getLevel(self) -> float:
        return self.waterLevel
    
    def run(self) -> None:
        self.waterLevel += 1

    def __str__(self) -> str:
        return f"Tank capacity: {self.capacity}\nTank level: {self.waterLevel}\nTank temp: {self.waterTemp}\n"
    