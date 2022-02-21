from sys import stdout
from .wemo import WemoSwitch
from lib.utils.colors import Colors
from lib.utils.load_data import load_data_from_json


def kitchen_data():
    return load_data_from_json('devices', 'kitchen')


def get_devices():
    stdout.write(f"\n  Kitchen... ")
    data = kitchen_data()
    all_devices = {}
    for wemo_device, device in data.items():
        stdout.write(f"\n    Gathering devices... ")
        if wemo_device == 'single_pole_outlets':
            for props in device:
                all_devices["Switch 1"] = WemoSwitch(**dict(props))
    stdout.write(f"[{Colors.green('OK')}]\n")
    return all_devices


class Kitchen:
    def __init__(self, devices=None):
        self.devices = get_devices()


if __name__ == "__main__":
    print('This file is not meant to be run directly!')
