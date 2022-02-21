import sys
from decouple import config

from .voice.voice import Voice
from .voice.voice_activation import voice_controller
from .voice.commands import query_controller
from lib.home_devices.living_room import LivingRoom
from lib.home_devices.kitchen import Kitchen
from lib.utils.colors import Colors


USERNAME = config('USER')
BOTNAME = config('BOTNAME')


def get_devices():
    k = Kitchen().devices
    lr = LivingRoom().devices
    return {**k, **lr}


class Alfred(Voice):
    def __init__(self):
        sys.stdout.write("\nInitializing Please Wait... \n")
        super().__init__()
        self.devices = get_devices()
        self.input_mode = 'voice'
        sys.stdout.write(f"{BOTNAME} Status [{Colors.green('Online')}]\n")

    def take_user_input(self):
        return voice_controller(self)

    def run(self):
        self.greet_user()
        while self.input_mode == 'voice':
            query = self.take_user_input()
            query_controller(query, self)
        # provide a traditional menu for times when listening to music or needing to use the microphone
        while self.input_mode == 'menu':
            pass
