from decouple import config


B_NAME = config('BOTNAME').lower()

commands = {
    "power off": lambda query, bot: bot.rooms['Office']['Vizio Tv'].remote.turn_off(),
    "power on": lambda query, bot: bot.rooms['Office']['Vizio Tv'].remote.turn_on(),
    "volume up": lambda query, bot: bot.rooms['Office']['Vizio Tv'].remote.volume_up(),
    "volume down": lambda query, bot: bot.rooms['Office']['Vizio Tv'].remote.volume_down(),
    "mute": lambda query, bot: bot.rooms['Office']['Vizio Tv'].remote.mute(),
    "change input": lambda query, bot: bot.rooms['Office']['Vizio Tv'].remote.change_input(),
    "netflix": lambda query, bot: bot.rooms['Office']['Vizio Tv'].remote.launch_netflix(),
    "xbox": lambda query, bot: bot.rooms['Office']['Vizio Tv'].remote.xbox(),
}


def office_tv_voice_controller(bot, command):
    print('OFFICE TV CONTROLLER', command)
    command = command.split(B_NAME)[1].strip()
    for k, v in commands.items():
        if k in command:
            return v(command, bot)
