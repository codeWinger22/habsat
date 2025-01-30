
   



# from flask import Flask, request, jsonify,render_template
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)  # Allow cross-origin requests

# sensor_data_list = []  # Store received sensor data


# @app.route('/')
# def index():
#     return render_template("index.html")


# @app.route('/data', methods=['POST'])
# def receive_data():
#     try:
#         data = request.json  # Get JSON data from ESP32
        
#         if not data or "data" not in data:
#             return jsonify({"error": "Invalid JSON format"}), 400
        
#         sensor_data = data["data"]  # Fix JSON key to match ESP32
        
#         sensor_data_list.append(sensor_data)  # Store data
#         print("Received Data:", sensor_data)
        
#         return jsonify({"message": "Data received successfully!", "data": sensor_data}), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')  # Run on all available network interfaces




# from flask import Flask, request, jsonify, render_template
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)  # Allow cross-origin requests

# sensor_data_list = []  # Store received sensor data

# @app.route('/')
# def index():
#     # Pass sensor data to HTML template
#     return render_template("data.html", sensor_data_list=sensor_data_list)

# @app.route('/data', methods=['POST'])
# def receive_data():
#     try:
#         data = request.json  # Get JSON data from ESP32
        
#         if not data or "data" not in data:
#             return jsonify({"error": "Invalid JSON format"}), 400
        
#         sensor_data = data["data"]  # Fix JSON key to match ESP32
        
#         sensor_data_list.append(sensor_data)  # Store data
#         print("Received Data:", sensor_data)
        
#         return jsonify({"message": "Data received successfully!", "data": sensor_data}), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')  # Run on all available network interfaces




from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

sensor_data_list = []  # Store received sensor data

@app.route('/')
def index():
    # Pass sensor data to HTML template
    return render_template("data.html", sensor_data_list=sensor_data_list)

@app.route('/data', methods=['POST'])
def receive_data():
    try:
        data = request.json  # Get JSON data from ESP32
        
        if not data or "data" not in data:
            return jsonify({"error": "Invalid JSON format"}), 400
        
        sensor_data = data["data"]  # Fix JSON key to match ESP32
        
        sensor_data_list.append(sensor_data)  # Store data
        print("Received Data:", sensor_data)
        
        return jsonify({"message": "Data received successfully!", "data": sensor_data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/data', methods=['GET'])
def get_data():
    try:
        if sensor_data_list:
            # Return the most recent sensor data in JSON format
            return jsonify({"data": sensor_data_list[-1]}), 200
        else:
            return jsonify({"error": "No data available"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # Run on all available network interfaces
