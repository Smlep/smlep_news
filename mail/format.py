from datetime import datetime, timedelta
from product_hunt import *
from weather import *

today = datetime.now()
yesterday = today - timedelta(1)

city_name = 'Paris'
city_id = '6455259'


def format_weather():
    res = 'Weather in ' + city_name + '<br>'
    weathers = gather_weathers(city_id)
    for weather in weathers:
        res += weather.time[10:-3].replace(':', 'h') + ': '
        res += str(weather.temperature) + '°C / '
        res += weather.conditions[0].description.title() + ' / '
        res += str(weather.humidity) + '% humidity'
        res += '<br>'
    return res


def format_ph():
    products = build_products_from_request(
        get_top_scores(yesterday.strftime("%Y"), yesterday.strftime("%m"), yesterday.strftime("%d")))

    res = 'Top products from yesterday<br>'
    for product in products:
        res += '<a href="' + product.url + '"> ' + product.name + '</a>: '
        res += product.description
        res += '<br>'

    return res
