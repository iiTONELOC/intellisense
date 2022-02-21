import json
from decouple import config


def switch(action):
    if action == 'devices':
        return '\\devices.json'
    else:
        return '\\devices.json'


def load_data_from_json(data_type, property_name):
    data_file = config('DATA_FOLDER') + str(switch(data_type))
    data = None
    with open(data_file, 'r') as f:
        data = json.load(f)
    return data[property_name]
