import pywemo


class Wemo:
    def __init__(self):
        self.wemo = lambda x: pywemo.discover_devices(x)


class WemoSwitch(Wemo):
    def __init__(
        self,
        name,
        type,
        mac,
        serial_number,
        firmware=None,
        location=None,
        description=None,
        default_schedule=None,
    ):
        super().__init__()
        self.mac = mac
        self.type = type
        self.name = name
        self.firmware = firmware
        self.location = location
        self.API = self.wemo(self.mac)
        self.description = description
        self.serial_number = serial_number
        self.default_schedule = default_schedule

    def _api(self):
        devices = self.API
        print('DEVICES:', devices)
        for device in self.API:
            if self.name == device.name:
                return device

    def on(self):
        self._api().on()

    def off(self):
        self._api().off()

    def toggle(self):
        self._api().toggle()

    def __str__(self):
        return f"{self.name} ({self.location}) ({self.description})"

    def status(self):
        return self._api().get_state()


def create_wemo_outlet_ensure_connection(data):
    # ENSURES THE CONNECTION TO THE DEVICE IS ESTABLISHED
    print("\n    Creating Wemo Switch")
    new_outlet = WemoSwitch(**dict(data))
    res = None

    def retry():
        print('      ERROR: Could not connect to device')
        print('      retrying...')
        create_wemo_outlet_ensure_connection(data)
    try:
        print("    Switch Created! Verifying Connection...")
        res = new_outlet.API[0].get_state()
    except Exception:
        retry()
    finally:
        if res == None:
            retry()
    return new_outlet
