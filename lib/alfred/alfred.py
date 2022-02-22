import sys
from decouple import config

from .voice.voice import Voice
from .voice.voice_activation import voice_controller
from .voice.commands import query_controller
from lib.rooms.living_room import LivingRoom
from lib.rooms.kitchen import Kitchen
from lib.utils.colors import Colors


USERNAME = config('USER')
BOTNAME = config('BOTNAME')


def get_devices():
    k = Kitchen().devices
    lr = LivingRoom().devices
    if k or lr is not None:
        sys.stdout.write(f"\nDevices Found!")
    return {**k, **lr}


class Alfred(Voice):
    def __init__(self):
        sys.stdout.write("\nInitializing Please Wait...")
        super().__init__()
        self.devices = get_devices()
        self.input_mode = 'voice'
        sys.stdout.write(f"\n{BOTNAME} Status [{Colors.green('Online')}]\n\n")

    def take_user_input(self):
        return voice_controller(self)

    def run(self):
        self.greet_user()
        while self.input_mode == 'voice':
            try:
                query = self.take_user_input()
                query_controller(query, self)
            except KeyboardInterrupt:
                sys.exit(1)

        # FIXME: ADD TEXT MENU MODE
        # provide a traditional menu for times when listening to music or needing to use the microphone
        while self.input_mode == 'menu':
            pass
