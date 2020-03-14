import requests
from .repository import Repository

base = "https://api.github.com/"


def two_digits(n):
    return format(int(n), "02d")


def get_trending_repo(key, from_date, to_date):
    url = base + "search/repositories?q=" + key
    url += "+created:{}-{}-{}..{}-{}-{}".format(
        two_digits(from_date[0]),
        two_digits(from_date[1]),
        two_digits(from_date[2]),
        two_digits(to_date[0]),
        two_digits(to_date[1]),
        two_digits(to_date[2]),
    )

    url += "&sort=stars"
    url += "&order=desc"
    r = requests.get(url)
    return r
