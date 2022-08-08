from sys import stdout
from lib.utils.load_data import load_data_from_json
from lib.utils.colors import Colors


class Room:
    def __init__(self, name):
        self.name = name
        self.devices = {}
        self.loader = load_data_from_json
        self.colors = Colors
        self.stdout = stdout.write
