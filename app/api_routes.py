from flask import Blueprint, request, jsonify
from datetime import datetime

api = Blueprint('api', __name__)

temperature_data = [
    {"timestamp": "2024-03-01 12:00:00", "temp": 20},
    {"timestamp": "2024-03-02 12:00:00", "temp": 22},
    {"timestamp": "2024-03-03 12:00:00", "temp": 18},
    {"timestamp": "2024-03-04 12:00:00", "temp": 21},
    {"timestamp": "2024-03-05 12:00:00", "temp": 19},
]

@api.route('/api/temperature', methods=['POST'])
def insert_temperature():
    data = request.get_json()
    if not data or 'temp' not in data:
        return jsonify({"error": "Missing 'temp' value"}), 400
    timestamp = datetime.now().isoformat()
    temperature_data.append({"timestamp": timestamp, "temp": data['temp']})
    return jsonify({"timestamp": timestamp, "temp": data['temp']}), 201

@api.route('/api/temperature/last', methods=['GET'])
def get_last_temperature():
    if temperature_data:
        return jsonify(temperature_data[-1])
    else:
        return jsonify({"error": "No data available"}), 404

@api.route('/api/temperature/last/<int:count>', methods=['GET'])
def get_last_temperatures(count):
    if count <= 0:
        return jsonify({"error": "Parameter count must be a positive integer"}), 400
    return jsonify(temperature_data[-count:])

@api.route('/api/temperature/delete/<int:count>', methods=['DELETE'])
def delete_temperatures(count):
    if count <= 0 or count > len(temperature_data):
        return jsonify({"error": "Invalid count value"}), 400
    del temperature_data[:count]
    return jsonify({"status": "Deleted", "count": count}), 200
