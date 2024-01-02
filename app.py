from flask import Flask, request, jsonify
from flask_cors import CORS
import threading
from RPICommunication.ArduinoCOM.COMListener import listener, listener2
from RPICommunication.ArduinoCOM.JSONIFYtemp import get_temp
from RPICommunication.RPIGPIO.PWMLED import gpioLED, initGpio

#from RPICommunication.RPIGPIO.PWMLED import gpioLED

app = Flask(__name__)
CORS(app, origins="*") #DEV ONLY!
#listener()

royal_blue_Top_Left = pin07 = initGpio(7)
deep_red_Top_Left = pin11 = initGpio(11)
IR_Top_Left = pin12 = initGpio(12)

royal_blue_Top_Right = pin13 = initGpio(13)
deep_red_Top_Right = pin15 = initGpio(15)
IR_Top_Right = pin16 = initGpio(16)

royal_blue_Bottom_Left = pin18 = initGpio(18)
deep_red_Bottom_Left = pin29 = initGpio(29)
IR_Bottom_Left = in31 = initGpio(31)

royal_blue_Bottom_Right = pin32 = initGpio(32)
deep_red_Bottom_Right = pin33 = initGpio(33)
IR_Bottom_Right = pin35 = initGpio(35)

peristaltic_PH_Positive = pin36 = initGpio(36)
peristaltic_PH_Negative = pin37 = initGpio(37)
peristaltic_Nutrients = pin38 = initGpio(38)
water_pump = pin40 = initGpio(40)

def runApp():
    app.run(host="0.0.0.0", port=5000, debug=True)

#def random_dataset():
#    dataset = {
#        "dataset": [
#            {
#                data = [
#                    Math.random() * 10,
#                    Math.random() * 10,
#                    Math.random() * 10,
#                    Math.random() * 10,
#                    Math.random() * 10,
#                    Math.random() * 10
#                ]
#            }
#        ]
#    }


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/login', methods=['POST'])
def login():
    print("Function triggered!")
    content = request.json
    print(content['ID'])
    if content['ID'] == '1234':
        return jsonify({"status": "success", "message": "Login successful!"})
    return jsonify({"status": "failure", "message": "Device of this ID doesn't exist!"})


@app.route('/pumps', methods=['POST'])
def pumps():
    print("Function Pumps triggered!")
    content = request.json
    print(content['ID'])
    print(content['value'])
    if content['ID'] == 1:
        gpioLED(water_pump, content['value'])
        return jsonify({"status": "success", "message": "Pump1 control successful!"})
    elif content['ID'] == 2:
        gpioLED(peristaltic_Nutrients, content['value'])
        return jsonify({"status": "success", "message": "Pump2 control successful!"})
    else:
        return jsonify({"status": "failure", "message": "Device of this ID doesn't exist!"})


@app.route('/lighting', methods=['POST'])
def lighting():
    print("Function Lighting triggered!")
    content = request.json
    print("ID:", content['ID'])
    print("Value:", content['value'])
    if content['ID'] == 'Blue_T_L':
        gpioLED(royal_blue_Top_Left, content['value'])
        return jsonify({"status": "success", "message": "Blue_Top_Left control successful!"})
    elif content['ID'] == 'Red_T_L':
        gpioLED(deep_red_Top_Left, content['value'])
        return jsonify({"status": "success", "message": "Red_Top_Left control successful!"})
    elif content['ID'] == 'IR_T_L':
        gpioLED(IR_Top_Left, content['value'])
        return jsonify({"status": "success", "message": "IR_Top_Left control successful!"})
    elif content['ID'] == 'Blue_T_R':
        gpioLED(royal_blue_Top_Right, content['value'])
        return jsonify({"status": "success", "message": "Blue_Top_Right control successful!"})
    elif content['ID'] == 'Red_T_R':
        gpioLED(deep_red_Top_Right, content['value'])
        return jsonify({"status": "success", "message": "Red_Top_Right control successful!"})
    elif content['ID'] == 'IR_T_R':
        gpioLED(IR_Top_Right, content['value'])
        return jsonify({"status": "success", "message": "IR_Top_Right control successful!"})
    elif content['ID'] == 'Blue_B_L':
        gpioLED(royal_blue_Bottom_Left, content['value'])
        return jsonify({"status": "success", "message": "Blue_Bottom_Left control successful!"})
    elif content['ID'] == 'Red_B_L':
        gpioLED(deep_red_Bottom_Left, content['value'])
        return jsonify({"status": "success", "message": "Red_Bottom_Left control successful!"})
    elif content['ID'] == 'IR_B_L':
        gpioLED(IR_Bottom_Left, content['value'])
        return jsonify({"status": "success", "message": "IR_Bottom_Left control successful!"})
    elif content['ID'] == 'Blue_B_R':
        gpioLED(royal_blue_Bottom_Right, content['value'])
        return jsonify({"status": "success", "message": "Blue_Bottom_Right control successful!"})
    elif content['ID'] == 'Red_B_R':
        gpioLED(deep_red_Bottom_Right, content['value'])
        return jsonify({"status": "success", "message": "Red_Bottom_Right control successful!"})
    elif content['ID'] == 'IR_B_R':
        gpioLED(IR_Bottom_Right, content['value'])
        return jsonify({"status": "success", "message": "IR_Bottom_Right control successful!"})
    else:
        return jsonify({"status": "failure", "message": "Device of this ID doesn't exist!"})


@app.route('/datasets', methods=['POST'])
def datasets():
    print("Function Datasets triggered!")
    content = request.json
    #print(content['ID'])
    print(content['message'])
    if content['ID'] == 1:
        return get_temp()
        #return jsonify({"status": "success", "message": "Dataset1 control successful!"})
    elif content['ID'] == 2:
        return jsonify({"status": "success", "message": "Dataset2 control successful!"})
    elif content['ID'] == 3:
        return jsonify({"status": "success", "message": "Dataset3 control successful!"})
    elif content['ID'] == 4:
        return jsonify({"status": "success", "message": "Dataset4 control successful!"})
    else:
        return jsonify({"status": "failure", "message": "Device of this ID doesn't exist!"})


if __name__ == '__main__':
    runApp()
    #print("Main function triggered!")
    #t1 = threading.Thread(target=listener)
    #2 = threading.Thread(target=runApp)
    #app.run(host="0.0.0.0", port=5000, debug=True)

    #t1.start()
    #print("Thread 1 started!")
    #t2.start()
    #print("Thread 2 started!")

    #t1.join()
    #t2.join()


#. .venv/bin/activate
#flask run --host=0.0.0.0 --port=5000
#flask --app app --debug run
#python app.py
