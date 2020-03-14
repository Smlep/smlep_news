from datetime import datetime, timedelta

from figaro import get_figaro_articles
from github import get_trending_repo, Repository
from guardian import get_recent_random_articles
from product_hunt import get_top_scores, Product
from tools import build_list_from_request
from weather import gather_weathers

today = datetime.now()
yesterday = today - timedelta(1)

city_name = "Paris"
city_id = "6455259"


def link(name, target):
    return '<a href="' + target + '"> ' + name + "</a>"


def format_weather(lg="en"):
    res = "{} {}<br>".format("Météo à" if lg == "fr" else "Weather in", city_name)
    suffix = "d'humidité<br>" if lg == "fr" else "humidity<br>"
    weathers = gather_weathers(city_id)
    for weather in weathers:
        res += "{}: {}°C / {} / {}% {}".format(
            weather.time[10:-3].replace(":", "h"),
            weather.temperature,
            weather.conditions[0].description.title(),
            weather.humidity,
            suffix,
        )
    return res


def format_ph(size, lg="en"):
    res = ""
    if lg == "en":
        res += "Top products from yesterday<br>"
    if lg == "fr":
        res += "Meilleurs produits d'hier<br>"
    products = build_list_from_request(
        get_top_scores(
            yesterday.strftime("%Y"), yesterday.strftime("%m"), yesterday.strftime("%d")
        ),
        "posts",
        Product,
    )
    for product in products[:size]:
        res += link(product.name, product.url) + ": "
        res += product.description
        res += "<br>"
    return res


def format_gh(size, lg="en"):
    res = ""
    if lg == "en":
        res += "Top repos from yesterday<br>"
    if lg == "fr":
        res += "Meilleurs dépôts GitHub d'hier<br>"
    repos = build_list_from_request(
        get_trending_repo(
            " ",
            [
                yesterday.strftime("%Y"),
                yesterday.strftime("%m"),
                yesterday.strftime("%d"),
            ],
            [today.strftime("%Y"), today.strftime("%m"), today.strftime("%d")],
        ),
        "items",
        Repository,
    )
    for repo in repos[:size]:
        res += link(repo.name, repo.url)
        if repo.description is not None:
            res += ": " + repo.description
        res += "<br>"
    return res


def format_guardian(size):
    res = "Recent news<br>"
    articles = get_recent_random_articles(size)
    for article in articles:
        res += link(article.title, article.url) + "<br>"
    return res


def format_figaro(size, long=False):
    res = "Articles récents<br>"
    articles = get_figaro_articles()
    for article in articles[:size]:
        res += link(article.title, article.url)
        if long:
            res += ": " + article.summary
        res += "<br>"
    return res
