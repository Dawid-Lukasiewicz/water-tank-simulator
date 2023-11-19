from TankSimClass import Tank
from TankSimClass import PumpType

def test4_heater():
    tank = Tank(capacity=10, flowRate=1.0, heaterPower=1000, ambientTemp=20)
    tank.setPump(PumpType.IN_PUMP, True)
    tank.run(5)
    tank.setPump(PumpType.IN_PUMP, False)

    assert tank.getLevel() == 5
    assert tank.getTemperature() == 20

    tank.setHeater(True)
    tank.run(60)
    temp = tank.getTemperature()
    print(temp)
    assert temp > 22
    assert temp < 23

    tank.run(150)
    temp = tank.getTemperature()
    print(temp)
    assert temp == 30

def test5_heater():
    tank = Tank(capacity=10, flowRate=1.0, heaterPower=1000, ambientTemp=20)
    assert tank.getLevel() == 0
    assert tank.getTemperature() == 20
    tank.setHeater(True)
    tank.run(10)
    assert tank.getTemperature() == 20

test4_heater()
test5_heater()