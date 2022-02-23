from .room import Room
from lib.tvs.vizio.tv import VizioTV


def get_devices(self):
    self.stdout(f"  Loading Office... ")
    devices = self.loader('devices', 'office')
    all_devices = {}
    for device, props in devices.items():
        if device == 'tv':
            my_tv = VizioTV(props['name'])
            all_devices[props['name']] = my_tv
    self.stdout(f"[{self.Colors.green('OK')}]\n")
    return all_devices


class Office(Room):
    def __init__(self) -> None:
        super().__init__('Office')
        self.devices = get_devices(self)
