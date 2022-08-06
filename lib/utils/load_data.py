import json
from decouple import config

# THESE ARE THE SAME FOR NOW BC WE ARE ONLY LOADING ONE TYPE OF DATA
# BUT HAVE ANTICIPATED THAT WE WILL LOAD MORE TYPES OF DATA


def switch(action):  # NOSONAR
    if action == 'devices':  # NOSONAR
        return '\\devices.json'
    else:
        return '\\devices.json'


def load_data_from_json(data_type, property_name):
    data_file = config('DATA_FOLDER') + str(switch(data_type))
    data = None
    with open(data_file, 'r') as f:
        data = json.load(f)
    return data[property_name]
