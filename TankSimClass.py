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
                 ,flowRate = 1.0
                 ,heaterPower = 20.0
                 ,heaterState = False
                 ,pumpInState = False
                 ,pumpOutState = False
                 ):
        self.capacity       = capacity
        self.waterLevel     = waterLevel
        self.ambientTemp    = ambientTemp
        self.waterTemp      = waterTemp
        self.heaterState    = heaterState
        self.pumpInState    = pumpInState
        self.pumpOutState   = pumpOutState
        self.flowRate       = flowRate
        self.heaterPower    = heaterPower

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

    def pump_handler(self, time):
        if self.pumpInState and not self.pumpOutState:
            self.waterLevel += time * self.flowRate
            delta = self.flowRate*time
        elif self.pumpOutState and not self.pumpInState:
            self.waterLevel -= time * self.flowRate
            delta = -self.flowRate*time
        else:
            delta = 0
        # Check if water level is exceeded
        if self.waterLevel < 0:
            self.waterLevel = 0
            delta = 0
        elif self.waterLevel > self.capacity:
            self.waterLevel = self.capacity
            delta = 0

        return delta

    def termomix_handler(self, deltaLiters):
        waterLevelBefore = self.waterLevel - deltaLiters
        # We mix the temperature of water only if it was pumped in
        if deltaLiters > 0:
            self.waterTemp = (waterLevelBefore * self.waterTemp + deltaLiters * self.ambientTemp)/(self.waterLevel)

    def heater_handler(self, time):
        c = 4200
        if self.waterLevel <= 0:
            self.waterTemp = self.ambientTemp
            return
        if self.heaterState:
            self.waterTemp = self.heaterPower*time/(c*self.waterLevel) + self.waterTemp

    def run(self, time: float = 1) -> None:
        delta = self.pump_handler(time)
        self.termomix_handler(delta)
        self.heater_handler(time)

    def __str__(self) -> str:
        return f"Tank capacity: {self.capacity}\nTank level: {self.waterLevel}\nTank temp: {self.waterTemp}\n"
