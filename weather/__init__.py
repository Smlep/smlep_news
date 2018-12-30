import json
import requests
from .weather import Weather

with open('config.json', 'r') as f:
    config = json.load(f)

apiKey = config['DEFAULT']['WEATHER_KEY']


def get_weather(city):
    url = 'http://api.openweathermap.org/data/2.5/weather?id=' + city
    url += '&units=metric'
    url += '&appid=' + apiKey

    r = requests.get(url)

    return Weather(r)
