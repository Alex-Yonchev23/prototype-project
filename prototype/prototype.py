# DB.py
import copy

class DB:
    def clone(self, shallow=True):
        if shallow:
            return copy.copy(self)
        else:
            return copy.deepcopy(self)

    def connect(self):
        print("Connecting to the database...")

    def query(self, query):
        print(f"Executing query: {query}")
