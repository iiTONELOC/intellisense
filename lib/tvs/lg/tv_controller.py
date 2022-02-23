from decouple import config
from .controls import *

B_NAME = config('BOTNAME').lower()

commands = {
    "tv power off": lambda query, bot: bot.rooms['Living Room']['LG TV'].remote.turn_off(),
    "tv screen off": lambda query, bot: bot.rooms['Living Room']['LG TV'].remote.screen_off(),
    "tv screen on": lambda query, bot: bot.rooms['Living Room']['LG TV'].remote.screen_on(),
    "tv launch": lambda query, bot: bot.rooms['Living Room']['LG TV'].remote.launch_app(query),
    "tv info": lambda query, bot: bot.rooms['Living Room']['LG TV'].remote.tv.systemControls.info(),
    "tv exit": lambda query, bot: bot.rooms['Living Room']['LG TV'].remote.exit_button(),
}


def living_room_tv_voice_controller(bot, command):
    command = command.split(B_NAME)[1].strip()
    for k, v in commands.items():
        if k in command:
            return v(command, bot)
