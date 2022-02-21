import sys
import pyttsx3

from decouple import config
from datetime import datetime
from lib.utils.colors import Colors

BOTNAME = config('BOTNAME')


class Voice:
    def __init__(self):
        self.engine = pyttsx3.init('sapi5')
        self.engine.setProperty('rate', 190)
        self.engine.setProperty('volume', 1.0)
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)

    def speak(self, text):
        sys.stdout.write(
            f"{Colors.green(BOTNAME)}: {text} \n")
        self.engine.say(text)
        self.engine.runAndWait()

    def read(self, list_of_text):
        for text in list_of_text:
            self.speak(text)

    def greet_user(self, username=None):
        # FIXME add username
        hour = datetime.now().hour
        if (hour >= 6) and (hour < 12):
            self.speak(text=f"Good Morning sir\n")
        elif (hour >= 12) and (hour < 16):
            self.speak(text=f"Good afternoon sir\n")
        elif (hour >= 16) and (hour < 19):
            self.speak(text=f"Good Evening sir\n")
        self.speak(text=f"I am {BOTNAME}. How may I assist you?\n")
