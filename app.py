from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="*") #DEV ONLY!


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
    print("Function triggered!")
    content = request.json
    print(content['ID'])
    print(content['value'])
    if content['ID'] == '1':
        return jsonify({"status": "success", "message": "Pump1 control successful!"})
    elif content['ID'] == '2':
        return jsonify({"status": "success", "message": "Pump2 control successful!"})
    else:
        return jsonify({"status": "failure", "message": "Device of this ID doesn't exist!"})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)


#flask run --host=0.0.0.0 --port=5000
