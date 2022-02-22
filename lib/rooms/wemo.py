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

    def on(self):
        self.API[0].on()

    def off(self):
        self.API[0].off()

    def toggle(self):
        self.API[0].toggle()

    def __str__(self):
        return f"{self.name} ({self.location}) ({self.description})"

    def status(self):
        return self.API.get_state()
