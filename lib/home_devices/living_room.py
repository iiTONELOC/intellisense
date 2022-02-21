from lib.utils.load_data import load_data_from_json
from lib.lg.tv import LGTV

# FIXME- CURRENTLY NOT WORKING BC THIS TV IS ON A DIFFERENT NETWORK


def get_devices():
    devices = load_data_from_json('devices', 'living_room')
    all_devices = {}
    for device, props in devices.items():
        if device == 'tv':
            my_tv = LGTV(props['name'])
            all_devices['Living Room Tv'] = my_tv
    return all_devices


class LivingRoom:
    def __init__(self):
        self.devices = get_devices()
