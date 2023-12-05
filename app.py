from flask import Flask, request, jsonify
from flask_cors import CORS
from RPICommunication.ArduinoCOM.COMListener import listener, listener2
from RPICommunication.RPIGPIO.PWMLED import gpioLED

app = Flask(__name__)
CORS(app, origins="*") #DEV ONLY!
listener()

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
        gpioLED(content['value'])
        return jsonify({"status": "success", "message": "Pump1 control successful!"})
    elif content['ID'] == 2:
        return jsonify({"status": "success", "message": "Pump2 control successful!"})
    else:
        return jsonify({"status": "failure", "message": "Device of this ID doesn't exist!"})


@app.route('/lighting', methods=['POST'])
def lighting():
    print("Function Lighting triggered!")
    content = request.json
    print(content['ID'])
    print(content['value'])
    if content['ID'] == 1:
        return jsonify({"status": "success", "message": "Light1 control successful!"})
    elif content['ID'] == 2:
        return jsonify({"status": "success", "message": "Light2 control successful!"})
    elif content['ID'] == 3:
        return jsonify({"status": "success", "message": "Light3 control successful!"})
    elif content['ID'] == 4:
        return jsonify({"status": "success", "message": "Light4 control successful!"})
    else:
        return jsonify({"status": "failure", "message": "Device of this ID doesn't exist!"})


@app.route('/datasets', methods=['POST'])
def datasets():
    print("Function Datasets triggered!")
    content = request.json
    print(content['ID'])
    print(content['value'])
    if content['ID'] == 1:
        return jsonify({"status": "success", "message": "Dataset1 control successful!"})
    elif content['ID'] == 2:
        return jsonify({"status": "success", "message": "Dataset2 control successful!"})
    elif content['ID'] == 3:
        return jsonify({"status": "success", "message": "Dataset3 control successful!"})
    elif content['ID'] == 4:
        return jsonify({"status": "success", "message": "Dataset4 control successful!"})
    else:
        return jsonify({"status": "failure", "message": "Device of this ID doesn't exist!"})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)


#. .venv/bin/activate
#flask run --host=0.0.0.0 --port=5000
