from datetime import datetime

class TemperatureDataManager:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(TemperatureDataManager, cls).__new__(cls)
            cls._instance.initialize_data()
        return cls._instance

    def initialize_data(self):
        self.data = [
            {"timestamp": "2024-03-01 12:00:00", "temp": 20},
            {"timestamp": "2024-03-02 12:00:00", "temp": 22},
            {"timestamp": "2024-03-03 12:00:00", "temp": 18},
            {"timestamp": "2024-03-04 12:00:00", "temp": 21},
            {"timestamp": "2024-03-05 12:00:00", "temp": 19},
        ]

    def add_record(self, temp):
        now = datetime.now()
        formatted_timestamp = now.strftime('%Y-%m-%d %H:%M:%S')
        new_record = {"timestamp": formatted_timestamp, "temp": temp}
        self.data.append(new_record)
        return new_record

    def get_last_record(self):
        if self.data:
            return self.data[-1]
        return None

    def get_last_records(self, count):
        if count > 0 and count <= len(self.data):
            return self.data[-count:]
        return []

    def delete_records(self, count):
        if count > 0 and count <= len(self.data):
            del self.data[:count]
            return count
        return 0

    def get_data(self):
        return self.data