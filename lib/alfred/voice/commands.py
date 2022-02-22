from lib.alfred.utils.entertainment.netflix import netflix
from lib.alfred.utils.misc import tell_joke, give_advice, info_lookup, search
from lib.alfred.utils.misc import give_current_weather, play_on_youtube
from lib.tvs.lg.tv_controller import living_room_tv_voice_controller
from lib.alfred.utils.os_controller.controller import os_query_handler
from decouple import config

B_NAME = config('BOTNAME').lower()

voice_commands = {
    # OS RELATED COMMANDS
    "launch": lambda query, bot: os_query_handler(query, bot),
    "open": lambda query, bot: os_query_handler(query, bot),
    # home automation/devices
    # kitchen
    "toggle kitchen light": lambda query, bot: bot.devices['Switch 1'].toggle(),
    # living room
    f"{B_NAME} living room living room tv": lambda query, bot: living_room_tv_voice_controller(bot, query),
    #  BOT COMPUTER COMMANDS
    f"{B_NAME} netflix": lambda query, bot: netflix(bot, query),
    f"{B_NAME} current weather": lambda query, bot: give_current_weather(bot),
    # WIKIPEDIA SEARCH SUMMARY
    f"{B_NAME} what is": lambda query, bot: info_lookup(bot, query),
    f"{B_NAME} tell me about": lambda query, bot: info_lookup(bot, query),
    # _
    f"{B_NAME} tell me a joke": lambda query, bot: tell_joke(bot),
    f"{B_NAME} can i have a tip": lambda query, bot: give_advice(bot),
    # DUCKDUCKGO SEARCH
    f"{B_NAME} search for": lambda query, bot: search(bot, query),
    # YOUTUBE SEARCH
    f"{B_NAME} search youtube for": lambda query, bot: play_on_youtube(bot, query),
}


def query_controller(command, bot):
    if command.startswith(B_NAME):
        for key, value in voice_commands.items():
            if command.startswith(key):
                return value(command, bot)
