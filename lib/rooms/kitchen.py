from .wemo import WemoSwitch
from.room import Room


def get_devices(self):
    self.stdout(f"  Loading Kitchen... ")
    data = self.loader('devices', 'kitchen')
    all_devices = {}
    for wemo_device, device in data.items():
        if wemo_device == 'outlets':
            for props in device:
                all_devices[props['name']] = WemoSwitch(**dict(props))
    self.stdout(f"[{self.Colors.green('OK')}]\n")
    return all_devices


class Kitchen(Room):
    def __init__(self, devices=None):
        super().__init__('Kitchen')
        self.devices = get_devices(self)


if __name__ == "__main__":
    print('This file is not meant to be run directly!')
