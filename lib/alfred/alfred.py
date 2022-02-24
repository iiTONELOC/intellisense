import os
import sys
from decouple import config

from lib.databases.movies.db import Movie_DB

from .voice.voice import Voice
from .voice.voice_activation import voice_controller
from .voice.commands import query_controller
from lib.rooms.living_room import LivingRoom
from lib.rooms.kitchen import Kitchen
from lib.rooms.office import Office
from lib.utils.colors import Colors


USERNAME = config('USER')
BOTNAME = config('BOTNAME')


def get_devices():
    rooms = [LivingRoom(), Kitchen(), Office()]
    room_data = {}
    for room in rooms:
        room_data[room.name] = room.devices
    if len(rooms) > 1:
        sys.stdout.write(f"\nDevices Found!")
    return room_data


class Alfred(Voice):
    def __init__(self):
        sys.stdout.write("\nInitializing Please Wait...")
        super().__init__()
        self.rooms = get_devices()
        self.databases = {
            'movies': Movie_DB()
        }
        self.input_mode = 'voice'
        sys.stdout.write(f"\n{BOTNAME} Status [{Colors.green('Online')}]\n\n")
        # initialize the databases
        for db_name, db in self.databases.items():
            db.init()

    def take_user_input(self):
        return voice_controller(self)

    def run(self):

        while self.input_mode == 'voice':
            try:
                query = self.take_user_input()
                if f'{BOTNAME.lower()} exit' in query:
                    sys.exit(1)
                elif f'{BOTNAME.lower()} stop listening' in query:
                    self.speak("Entering text only mode sir!\n")
                    self.input_mode = 'menu'
                else:
                    query_controller(query, self)

            except KeyboardInterrupt:
                sys.exit(1)

        # FIXME: ADD TEXT MENU MODE
        # provide a traditional menu for times when listening to music or needing to use the microphone
        while self.input_mode == 'menu':
            user_input = input(f"{Colors.magenta('$ ')}").strip().lower()
            if user_input == 'exit':
                sys.exit(1)
            elif user_input == 'activate voice mode':
                sys.stdout.write(
                    f"\n{Colors.cyan(BOTNAME)}: Entering Voice Mode...\n")
                self.input_mode = 'voice'
                self.speak('Thanks for the nap sir!')
                self.run()
            elif user_input == 'clear' or user_input == 'cls':
                os.system('cls')
            else:
                query_controller(BOTNAME.lower() + " " + user_input, self)
            pass
