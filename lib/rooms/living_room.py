from .room import Room
from lib.tvs.lg.tv import LGTV


# FIXME- CURRENTLY NOT WORKING BC THIS TV IS ON A DIFFERENT NETWORK


def get_devices(self):
    self.stdout(f"\n  Loading Living Room... ")
    devices = self.loader('devices', 'living_room')
    all_devices = {}
    for device, props in devices.items():
        if device == 'tv':
            my_tv = LGTV(props['name'])
            all_devices[props['name']] = my_tv
            self.stdout(f"[{self.Colors.green('OK')}]\n")
            return all_devices


class LivingRoom(Room):
    def __init__(self):
        super().__init__('Living Room')
        self.devices = get_devices(self)
