import json
import requests
import secrets
from datetime import datetime, timedelta
from .article import Article

with open("config.json", "r") as f:
    config = json.load(f)

apiKey = config["DEFAULT"]["GUARDIAN_KEY"]
base = "https://content.guardianapis.com/"


def build_base_query(year, month, day):
    return "{}search?from-date={}-{}-{}".format(base, year, month, day)


def get_articles_count(year, month, day):
    url = build_base_query(year, month, day)
    url += "&page-size=1"
    url += "&api-key=" + apiKey

    r = requests.get(url)
    return r.json()["response"]["total"]


def get_articles(year, month, day):
    url = build_base_query(year, month, day)
    url += "&page-size=200"
    url += "&api-key=" + apiKey

    r = requests.get(url)

    articles = []
    for article_json in r.json()["response"]["results"]:
        articles.append(Article(article_json))
    return articles


def get_recent_random_articles(count):
    yesterday = datetime.now() - timedelta(1)
    articles = get_articles(
        yesterday.strftime("%Y"), yesterday.strftime("%m"), yesterday.strftime("%d")
    )
    secure_random = secrets.SystemRandom()
    res = secure_random.sample(articles, count)

    return res
