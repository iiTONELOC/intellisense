from decouple import config
from lib.wemo.controller import wemo_switch_controller
from lib.tvs.vizio.tv_controller import office_tv_voice_controller
from lib.alfred.utils.os_controller.controller import os_query_handler

from lib.alfred.utils.entertainment.netflix import netflix
from lib.alfred.utils.misc import tell_joke, give_advice, info_lookup, search,\
    give_current_weather, play_on_youtube


B_NAME = config('BOTNAME').lower()

voice_commands = {
    # OS RELATED COMMANDS
    f"{B_NAME} launch": lambda query, bot: os_query_handler(query),
    f"{B_NAME} open": lambda query, bot: os_query_handler(query),
    # home automation/devices
    # WeMo Devices
    f"{B_NAME} turn": lambda query, bot: wemo_switch_controller(query, bot),
    f"{B_NAME} toggle": lambda query, bot: wemo_switch_controller(query, bot),
    # office:
    f"{B_NAME} office tv": lambda query, bot: office_tv_voice_controller(bot, query),
    #  BOT COMPUTER COMMANDS
    f"{B_NAME} netflix": lambda query, bot: netflix(bot, query),
    f"{B_NAME} current weather": lambda query, bot: give_current_weather(bot),
    # WIKIPEDIA SEARCH SUMMARY
    f"{B_NAME} what is": lambda query, bot: info_lookup(bot, query),
    f"{B_NAME} tell me about": lambda query, bot: info_lookup(bot, query),
    # GOOFY
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
