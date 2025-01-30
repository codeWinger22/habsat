from flask import Flask, render_template, request, redirect, url_for, jsonify, make_response,session
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

sensor_data_list = []  # Store received sensor data

@app.route('/')
def index():
    return render_template("index.html")
   


@app.route('/data', methods=['POST'])
def receive_data():
    try:
        data = request.json  # Get JSON data from ESP32
        sensor_data = data.get("sensor_data", "")
        
        if sensor_data:
            sensor_data_list.append(sensor_data)  # Store data
            print("Received Data:", sensor_data)
            return jsonify({"message": "Data received successfully!", "data": sensor_data}), 200
        else:
            return jsonify({"error": "No data received"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug = True)