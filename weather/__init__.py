import json
import requests
from .weather import Weather

with open('config.json', 'r') as f:
    config = json.load(f)

apiKey = config['DEFAULT']['WEATHER_KEY']
base = 'http://api.openweathermap.org/data/2.5/'


def gather_weathers(city):
    current = get_weather(city)
    nexts = get_forecast(city)
    #nexts.pop(0)
    weathers = [current]
    weathers.extend(nexts)
    return weathers


def get_weather(city):
    url = base + 'weather?id=' + city
    url += '&units=metric'
    url += '&appId=' + apiKey

    r = requests.get(url)

    return Weather(r.json())


def get_forecast(city):
    url = base + 'forecast?id=' + city
    url += '&units=metric'
    url += '&appId=' + apiKey

    r = requests.get(url)

    forecasts = []
    for forecast in r.json()['list']:
        forecasts.append(Weather(forecast))

    forecasts = forecasts[:5]
    return forecasts
