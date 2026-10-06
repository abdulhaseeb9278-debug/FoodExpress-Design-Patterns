from datetime import datetime


class Logger:
    _instance = None

    def __init__(self):
        if Logger._instance is not None:
            raise Exception("Logger object already exists")

        self._logs = []

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = Logger()

        return cls._instance

    def log(self, message: str):
        timestamp = datetime.now()
        self._logs.append(f"{timestamp} - {message}")

    def get_logs(self):
        return self._logs
