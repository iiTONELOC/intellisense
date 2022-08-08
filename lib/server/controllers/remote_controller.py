from flask import jsonify
from lib.alfred.voice.commands import query_controller


def remote_access_API(req, res, bot):
    query_controller(req.json['command'], bot)
    return res(jsonify({'message': 'REMOTE ACCESS API'}), 200)


def device_status_API(req, res, bot):
    data = bot.rooms.items()
    rooms = {}

    for room, room_devices in data:
        rooms[room] = []

        for device_name, device in room_devices.items():
            status = None
            try:
                status = device.status()
                rooms[room].append({
                    'name': device_name,
                    'status': status
                })
            except Exception as err:
                pass

    return res(jsonify(rooms), 200)
