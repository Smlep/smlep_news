from github import *
from guardian import *
from product_hunt import *
from weather import *
from datetime import datetime, timedelta

yesterday = datetime.now() - timedelta(1)


def gather_ph():
    products = build_products_from_request(
        get_top_scores(yesterday.strftime("%Y")))

    for product in products:
        print(product.short_string())


def gather_gh():
    repos = build_repo_from_request(
        get_trending_repo(' ', 2018, 1, 1, yesterday.strftime("%Y"), yesterday.strftime("%m"),
                          yesterday.strftime("%d")))

    for repo in repos:
        print(repo.short_string())


def gather_weather():
    weathers = gather_weathers('6455259')

    for weather in weathers:
        print(weather)


def gather_guardian():
    articles = get_articles()

    print(articles.json())


gather_guardian()
