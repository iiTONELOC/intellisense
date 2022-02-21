from sys import stdout
from decouple import config
import speech_recognition as sr
from random import choice
from datetime import datetime
from lib.utils.colors import Colors


def voice_controller(self):
    B_NAME = config('BOTNAME')
    r = sr.Recognizer()
    m = sr.Microphone()
    with m as source:
        r.adjust_for_ambient_noise(source)
        r.energy_threshold = r.energy_threshold * 1.12
        stdout.write(f"[{Colors.green(r.energy_threshold)}]\n")
        r.pause_threshold = 2
        stdout.write(
            f"{Colors.cyan('% ')}listening...\n")
        audio = r.listen(source)
        try:
            stdout.write(
                f"{Colors.cyan('% ')}recognizing...\n")
            query = str(r.recognize_google(audio, language='en-us')).lower()
            if query == f'{B_NAME} exit' or query == f'{B_NAME} stop listening':
                hour = datetime.now().hour
                if hour >= 21 and hour < 6:
                    self.speak("Good night sir, take care!\n")
                else:
                    self.speak('Have a good day sir!\n')
                exit()
            elif B_NAME in query:
                self.speak(choice([
                    "Cool, I'm on it sir.\n",
                    "Okay sir, I'm working on it.\n",
                    "Just a second sir.\n",
                ]))
        except Exception:
            query = 'None'
        return query
