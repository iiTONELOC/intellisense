from .room import Room
from lib.wemo import WemoSwitch
from lib.tvs.vizio.tv import VizioTV


def get_devices(self):
    self.stdout(f"  Loading Office... ")
    # Use our loader helper to load the room data from our JSON file
    # self.loader is inherited from the Room class
    devices = self.loader('devices', 'office')

    room_devices = {}

    for device, props in devices.items():
        if device == 'tv':
            my_tv = VizioTV(props['name'])
            room_devices[props['name']] = my_tv

        if device == 'outlets':
            for _props in props:
                room_devices[_props['name']] = WemoSwitch(**dict(_props))

    self.stdout(f"[{self.colors.green('OK')}]\n")

    print("OFFICE DEVICES:\n")
    print(room_devices)
    return room_devices


class Office(Room):
    def __init__(self) -> None:
        super().__init__('Office')
        self.devices = get_devices(self)
