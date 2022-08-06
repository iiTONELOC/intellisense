def _get_device_name(query, delimiter):
    return query.split(delimiter, 1)[1].strip()


def _build_device_dict(bot):
    devices = {}
    for room, room_devices in bot.rooms.items():
        for device in room_devices:
            if 'switch' in device:
                devices[device] = room_devices[device]
    return devices


def wemo_switch_controller(query, bot):

    devices = _build_device_dict(bot)
    device = None

    if 'turn' in query or 'toggle' in query:
        try:
            if 'turn on' in query:
                device = devices[_get_device_name(query, 'on')]
                device.on()

            if 'turn off' in query:
                device = devices[_get_device_name(query, 'off')]
                device.off()

            if 'toggle' in query:
                device = devices[_get_device_name(query, 'toggle')]
                device.toggle()

        except KeyError:
            print(f"Device not found!")
