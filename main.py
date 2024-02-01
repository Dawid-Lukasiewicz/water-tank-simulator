import os
from flask import Flask, jsonify, make_response, request
from flasgger import Swagger #swagger
from TankSimClass import PumpType, Tank
import threading
from time import sleep

app = Flask(__name__)
app.config['SWAGGER'] = {'title': 'Tank API', 'uiversion': 3}
swagger = Swagger(app) #swagger

tank = Tank()

@app.route("/")
def get_home():
    """
    file: docs/root.yml
    """
    return tank.__str__()

@app.route("/temp", methods = ['GET'])
def get_tank_temp():
    """
    file: docs/temp.yml
    """
    response = make_response(
                jsonify(
                    { "temp": tank.getTemperature()}
                ),
                200
            )
    return response

@app.route("/waterLevel", methods = ['GET'])
def get_water_level():
    """
    file: docs/???.yml
    """
    response = make_response(
                jsonify(
                    { "waterLevel": tank.getLevel()}
                ),
                200
            )
    return response

@app.route("/status", methods = ['GET'])
def get_tank_state():
    """
    file: docs/status.yml
    """
    response = make_response(
        jsonify(
            {
                "temp": tank.getTemperature(),
                "heater": tank.heaterState,
                "pumpIn": tank.pumpInState,
                "pumpOut": tank.pumpOutState
            }
        ),
        200
    )
    return response

# curl -X POST localhost:5000/heater -H "Content-Type: application/json" -d "{\"state\": true}"
# curl -X POST localhost:5000/heater -H "Content-Type: application/json" -d "{\"state\": false}"
@app.route("/heater", methods = ['POST'])
def set_heater():
    """
    file: docs/heater.yml
    """
    data_json = request.get_json()
    state = data_json["state"]
    print(state)
    tank.setHeater(state)
    return f"Heate State: {state}", 200

# curl -X POST localhost:5000/pump -H "Content-Type: application/json" -d "{\"type\": \"IN_PUMP\",\"state\": true}"
# curl -X POST localhost:5000/pump -H "Content-Type: application/json" -d "{\"type\": \"IN_PUMP\",\"state\": false}"
# curl -X POST localhost:5000/pump -H "Content-Type: application/json" -d "{\"type\": \"OUT_PUMP\",\"state\": true}"
# curl -X POST localhost:5000/pump -H "Content-Type: application/json" -d "{\"type\": \"OUT_PUMP\",\"state\": false}"
@app.route("/pump", methods=['POST'])
def set_pump():
    """
    file: docs/pump.yml
    """
    data_json = request.get_json()
    state = data_json["state"]
    type = data_json["type"]
    if type == "IN_PUMP":
        type = PumpType.IN_PUMP
    else:
        type = PumpType.OUT_PUMP

    tank.setPump(type, state)
    return f"Pump: {type}, State: {state}"

def thread_run():
    while True:
        tank.run()
        sleep(1)

thread = threading.Thread(target=thread_run)
thread.start()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')