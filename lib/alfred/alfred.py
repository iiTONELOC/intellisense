import os
import sys
from decouple import config

from lib.databases import DB

from .voice.voice import Voice
from .voice.voice_activation import voice_controller
from .voice.commands import query_controller
from lib.rooms.office import Office
from lib.utils.colors import Colors


USERNAME = config('USER')
BOTNAME = config('BOTNAME')


def get_devices():
    # Room to expand here, for now just Office
    rooms = [Office()]
    room_data = {}
    for room in rooms:
        room_data[room.name] = room.devices
    if len(rooms) > 1:
        sys.stdout.write(f"\nDevices Found!")
    return room_data


def handle_voice_mode(self):
    query = self.take_user_input()

    if f'{BOTNAME.lower()} exit' in query:
        sys.exit(1)
    elif f'{BOTNAME.lower()} stop listening' in query:
        self.speak("Entering text only mode!\n")
        self.input_mode = 'menu'
    else:
        query_controller(query, self)


def handle_text_mode(self):
    user_input = input(f"{Colors.magenta('$ ')}").strip().lower()
    if user_input == 'exit':
        sys.exit(1)
    elif user_input == 'activate voice mode':
        sys.stdout.write(
            f"\n{Colors.cyan(BOTNAME)}: Entering Voice Mode...\n")
        self.input_mode = 'voice'
        self.speak(f'Thanks for the nap, {USERNAME}!')
        self.run()
    elif user_input == 'clear' or user_input == 'cls':
        os.system('cls')
    else:
        query_controller(BOTNAME.lower() + " " + user_input, self)


class Alfred(Voice):
    def __init__(self):
        sys.stdout.write("\nInitializing Please Wait...")
        super().__init__()
        self.rooms = get_devices()
        self.database = DB()
        self.input_mode = 'menu'

        self.database.init()
        sys.stdout.write(f"\n{BOTNAME} Status [{Colors.green('Online')}]\n\n")

    def take_user_input(self):
        return voice_controller(self)

    def run(self):
        while self.input_mode == 'voice':
            try:
                handle_voice_mode(self)

            except KeyboardInterrupt:
                sys.exit(1)

        while self.input_mode == 'menu':
            try:
                handle_text_mode(self)
            except KeyboardInterrupt:
                sys.exit(1)
