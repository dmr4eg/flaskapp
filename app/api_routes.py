from flask import Blueprint, request, jsonify
from datetime import datetime
from .data_manager import TemperatureDataManager

api = Blueprint('api', __name__)
data_manager = TemperatureDataManager()

@api.route('/api/temperature', methods=['POST'])
def insert_temperature():
    data = request.get_json()
    if not data or 'temp' not in data:
        return jsonify({"error": "Missing 'temp' value"}), 400
    new_record = data_manager.add_record(data['temp'])
    return jsonify(new_record), 201

@api.route('/api/temperature/last', methods=['GET'])
def get_last_temperature():
    last_record = data_manager.get_last_record()
    if last_record:
        return jsonify(last_record)
    else:
        return jsonify({"error": "No data available"}), 404

@api.route('/api/temperature/last/<int:count>', methods=['GET'])
def get_last_temperatures(count):
    records = data_manager.get_last_records(count)
    if records:
        return jsonify(records)
    return jsonify({"error": "Invalid count value or no data"}), 400

@api.route('/api/temperature/delete/<int:count>', methods=['DELETE'])
def delete_temperatures(count):
    deleted_count = data_manager.delete_records(count)
    if deleted_count:
        return jsonify({"status": "Deleted", "count": deleted_count}), 200
    return jsonify({"error": "Invalid count value"}), 400
