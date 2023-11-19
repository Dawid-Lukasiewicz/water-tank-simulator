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
    assert temp > 22
    assert temp < 23

    tank.run(150)
    temp = tank.getTemperature()
    assert temp == 30

def test5_heater():
    tank = Tank(capacity=10, flowRate=1.0, heaterPower=1000, ambientTemp=20)
    assert tank.getLevel() == 0
    assert tank.getTemperature() == 20
    tank.setHeater(True)
    tank.run(10)
    assert tank.getTemperature() == 20

def test6_termomix():
    tank = Tank(capacity=10, flowRate=1.0, heaterPower=1000, ambientTemp=20)
    tank.setPump(PumpType.IN_PUMP, True)
    tank.run(5)
    tank.setPump(PumpType.IN_PUMP, False)
    # warunki początkowe: % 5 litrów wody o temperaturze 20 stopni
    assert tank.getLevel() == 5
    assert tank.getTemperature() == 20

    # grzejemy wodę
    tank.setHeater(True)
    tank.run(210)
    tank.setHeater(False)
    # temperatura wody powinna być w okolicach 30 stopni
    assert tank.getTemperature() == 30

    # pompujemy zimną wodę
    tank.setPump(PumpType.IN_PUMP, True)
    tank.run(5)
    # na początku mieliśmy 5 litów wody o temperaturze 30 stopni
    # dopompowaliśmy 5 litrów wody o temperaturze 20 stopni
    # powinnismy miec 10 litórw o temperaturze 25 stopni
    assert tank.getTemperature() == 25

test4_heater()
test5_heater()
test6_termomix()