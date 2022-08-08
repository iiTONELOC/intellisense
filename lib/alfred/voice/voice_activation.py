import sys
from random import choice
import speech_recognition as sr

from lib.utils.colors import Colors


def voice_controller(self):
    r = sr.Recognizer()
    m = sr.Microphone()
    with m as source:
        r.adjust_for_ambient_noise(source)
        r.energy_threshold = r.energy_threshold * 1.12
        # stdout.write(f"[{Colors.green(r.energy_threshold)}]\n")
        r.pause_threshold = 2

        try:
            sys.stdout.write(
                f"{Colors.cyan('% ')}listening...\n")
            audio = r.listen(source)
            sys.stdout.write(
                f"{Colors.cyan('% ')}recognizing...\n")
            query = str(r.recognize_google(audio, language='en-us')).lower()

            self.speak(choice([
                "Cool, I'm on it sir.\n",
                "Okay sir, I'm working on it.\n",
                "Just a second sir.\n",
            ]))
        except Exception:
            query = 'None'
        return query
