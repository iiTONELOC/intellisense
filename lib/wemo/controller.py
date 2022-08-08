import re


def _get_device_name(query, delimiter):
    return query.split(delimiter, 1)[1].strip()


def _dict_wemo_switches(bot):
    devices = {}
    for room_devices in bot.rooms.values():
        for device in room_devices:
            if 'switch' in device:
                devices[device] = room_devices[device]
    return devices


def _parse_query(query):
    query += ' '  # Add a space for easier parsing
    # The regex to search for the word 'to'
    regex_two = re.compile(r'(\sto\s)')
    # The regex to search for the word 'for'
    regex_four = re.compile(r'(\sfor\s)')
    match = regex_two.search(query)  # Holds the match object if found
    match_four = regex_four.search(query)  # Holds the match object if found

    if match is not None:
        query = query.replace(match.group(0), ' two').strip()
    elif match_four is not None:
        query.replace(match_four.group(0), ' four').strip()
    else:
        return query.strip()


def _handle_all(query, devices):
    for device in devices.keys():
        if 'all monitors' in query and 'monitor' in device or 'all switches'\
            in query and 'switch' in device or 'all lights' in query\
                and 'monitor' not in device:

            device = devices[device]

            if 'off' in query:
                device.off()
            elif 'on' in query:
                device.on()
            else:
                device.toggle()


def wemo_switch_controller(query, bot):
    query = _parse_query(query)  # handles oddities from voice recognition

    # Dictionary of all wemo devices in the bot
    devices = _dict_wemo_switches(bot)

    if 'turn' in query or 'toggle' in query:  # checked before here, being safe
        try:
            if 'all' in query:
                _handle_all(query, devices)
            elif 'turn on' in query:
                devices[_get_device_name(query, 'on')].on()
            elif 'turn off' in query:
                devices[_get_device_name(query, 'off')].off()
            elif 'toggle' in query:
                devices[_get_device_name(query, 'toggle')].toggle()
            else:
                return
        except Exception:
            print(f"Device not found!")
