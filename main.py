from flask import Flask
from TankSimClass import Tank
import testClass as tC
import threading
from time import sleep

app = Flask(__name__)
tank1 = Tank()

def thread_run():
    while True:
        tank1.run()
        sleep(1)

thread = threading.Thread(target=thread_run)
thread.start()

@app.route("/")
def hello_world():
    return tank1.__str__()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")