import pywhatkit as kit
import webbrowser as web
import requests
from lib.alfred.utils.weather.open_weather import Weather


def tell_joke(jarvis):
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/",
                       headers=headers).json()
    jarvis.speak(res["joke"])


def give_advice(jarvis):
    res = requests.get("https://api.adviceslip.com/advice").json()
    jarvis.read(['Here is your pro tip',  res['slip']['advice']])


def info_lookup(jarvis, command):
    query = command.split('tell me about')[1]
    res = kit.info(query, return_value=True)
    jarvis.read([f'Results for{query}', res])


def give_current_weather(jarvis):
    jarvis.read(Weather().current_weather())


def search(jarvis, command):
    query = command.split('search')[1]
    link = f"https://www.duckduckgo.com/?q={query}"
    jarvis.read([f'Here is what I found for {query}',
                'Opening results in a new tab, Sir...'])
    web.open(link)


def play_on_youtube(jarvis, video):
    jarvis.speak('Opening video in a new tab, Sir...')
    kit.playonyt(video)
