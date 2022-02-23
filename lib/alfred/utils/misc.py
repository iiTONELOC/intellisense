import wikipedia
import webbrowser as web
import requests
from lib.alfred.utils.weather.open_weather import Weather


def tell_joke(bot):
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/",
                       headers=headers).json()
    bot.speak(res["joke"])


def give_advice(bot):
    res = requests.get("https://api.adviceslip.com/advice").json()
    bot.read(['Here is your pro tip',  res['slip']['advice']])


def info_lookup(bot, command):
    query = command.split('tell me about')[1]
    res = wikipedia.summary(query, sentences=3)
    bot.read([f'Results for{query}', res])


def give_current_weather(bot):
    bot.read(Weather().current_weather())


def search(bot, command):
    query = command.split('search')[1]
    link = f"https://www.duckduckgo.com/?q={query}"
    bot.read([f'Here is what I found for {query}',
              'Opening results in a new tab, Sir...'])
    web.open(link)


def play_on_youtube(bot, video):
    bot.speak('Opening video in a new tab, Sir...')
    kit.playonyt(video)
