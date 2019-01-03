from guardian import *
from github import *
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


def format_ph(size):
    res = 'Top products from yesterday<br>'
    products = build_products_from_request(
        get_top_scores(yesterday.strftime("%Y"), yesterday.strftime("%m"), yesterday.strftime("%d")))
    for product in products[:size]:
        res += '<a href="' + product.url + '"> ' + product.name + '</a>: '
        res += product.description
        res += '<br>'
    return res


def format_gh(size):
    res = 'Top repos from yesterday<br>'
    repos = build_repo_from_request(
        get_trending_repo(' ', yesterday.strftime("%Y"), yesterday.strftime("%m"),
                          yesterday.strftime("%d"), today.strftime("%Y"), today.strftime("%m"), today.strftime("%d")))
    for repo in repos[:size]:
        res += '<a href="' + repo.url + '">' + repo.name + '</a>'
        res += ': ' + repo.description
        res += '<br>'
    return res


def format_guardian(size):
    res = 'Recent news<br>'
    articles = get_recent_random_articles(size)
    for article in articles:
        res += '<a href="' + article.url + '">' + article.title + '</a><br>'
    return res