from TankSimClass import Tank
from TankSimClass import PumpType

def test1_pump():
    # test działania pompowania
    tank = Tank(flowRate=1)
    tank.run(1)
    # samo run nie zmienia poziomu wody jeżeli pompy są wyłączone
    assert tank.getLevel() == 0
    tank.setPump(PumpType.IN_PUMP, True)
    # pompa uruchomiona
    tank.run(1)
    assert tank.getLevel() == 1
    # test mniejszego kwantu czasu
    tank.run(0.5)
    assert tank.getLevel() == 1.5
    # zmiana kierunku pompowania
    tank.setPump(PumpType.IN_PUMP, False)
    tank.setPump(PumpType.OUT_PUMP, True)
    tank.run(2)
    assert tank.getLevel() == 0
    # wypompowanie poniżej zera powinno być niemożliwe
    tank.run(1)
    assert tank.getLevel() == 0

def test2_pump():
    # test pompowania do maksymalnego poziomu wody
    tank = Tank(flowRate=2.5, capacity=10)
    tank.run(10)
    assert tank.getLevel() == 0
    tank.setPump(PumpType.IN_PUMP, True)
    tank.run(10)
    #zbiornik powinien osiągnąć maksymalny poziom
    assert tank.getLevel() == 10

def test3_pump():
    # dwie pompy naraz
    tank = Tank()
    # działa tylko pompa IN
    tank.setPump(PumpType.IN_PUMP, True)
    tank.run(1)
    assert tank.getLevel() == 1
    # teraz obie pompy działaja naraz
    tank.setPump(PumpType.OUT_PUMP, True)
    tank.run(1)
    assert tank.getLevel() == 1
    # działa tylko pompa OUT
    tank.setPump(PumpType.IN_PUMP, False)
    tank.run(1)
    assert tank.getLevel() == 0

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

test1_pump()
test2_pump()
test3_pump()
test4_heater()
test5_heater()
test6_termomix()
