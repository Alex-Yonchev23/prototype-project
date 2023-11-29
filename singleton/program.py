# Logger.py
class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.logs = []
        return cls._instance

    def log(self, message):
        self.logs.append(message)

# IProgram.py
from Logger import Logger

class IProgram:
    def __init__(self):
        self.logger = Logger()

    def log(self, message):
        self.logger.log(message)

    def run(self):
        pass
