from sys import stdout
from lib.tvs.lg.tv import LGTV
from lib.utils.load_data import load_data_from_json
from lib.utils.colors import Colors


# FIXME- CURRENTLY NOT WORKING BC THIS TV IS ON A DIFFERENT NETWORK


def get_devices():
    stdout.write(f"  Loading Living Room... ")
    devices = load_data_from_json('devices', 'living_room')
    all_devices = {}
    for device, props in devices.items():
        if device == 'tv':
            my_tv = LGTV(props['name'])
            all_devices['Living Room Tv'] = my_tv
    stdout.write(f"[{Colors.green('OK')}]\n")
    return all_devices


class LivingRoom:
    def __init__(self):
        self.devices = get_devices()
