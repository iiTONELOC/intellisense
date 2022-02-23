from subprocess import Popen
from decouple import config

IP = config('VIZIO_IP')
AUTH = config('VIZIO_AUTH')
LOG = config('VIZIO_OUT')
DEVICE_TYPE = 'tv'


def _py_vizio(command):
    """controller function for pyvizio"""
    command_string = f"pyvizio --ip={IP} --device_type=tv --auth={AUTH} {command}"
    Popen(command_string,  # dont want to clutter my output
          stdout=open(LOG + '\\user_log.txt', 'w'),
          stderr=open(LOG + '\\error_log.txt', 'w'),
          shell=True
          )


class VizioRemote:
    def __init__(self):
        self.turn_on = lambda: _py_vizio('power on')
        self.turn_off = lambda: _py_vizio('power off')
        self.toggle_power = lambda: _py_vizio('power toggle')
        self.volume_up = lambda: _py_vizio('volume up 2')
        self.volume_down = lambda: _py_vizio('volume down 2')
        self.mute = lambda: _py_vizio('mute toggle')
        self.change_input = lambda: _py_vizio('next-input')
        self.xbox = lambda: _py_vizio('input HDMI-2')
        self.launch_netflix = lambda: _py_vizio("launch-app Netflix")


class VizioTV(VizioRemote):
    def __init__(self, name):
        self.name = name
        self.remote = VizioRemote()
