import requests
# import json
from decouple import config


def get_cords():
    api_key = config('OPEN_WEATHER_API_KEY')
    loc = config("WEATHER_LOC")
    url = f"http://api.openweathermap.org/geo/1.0/zip?zip={loc},US&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return {"lat": data['lat'], "lon": data['lon']}


class Weather:
    def __init__(self) -> None:
        self.key = config('OPEN_WEATHER_API_KEY')
        self.location = get_cords()
        self.current_url = f"https://api.openweathermap.org/data/2.5/onecall?lat={self.location['lat']}&lon={self.location['lon']}&units=imperial&exclude=hourly,daily&appid={self.key}"

    def current_weather(self):
        res = requests.get(self.current_url).json()
        data = res['current']
        summary_data = [
            f"The current weather is {data['weather'][0]['description']}.",
            f"The temperature is {data['temp']} degrees.",
            f"The visibility is {int(data['visibility'])*0.000621371} Miles.\n"
        ]
        return summary_data
