import requests
from .repository import Repository

base = 'https://api.github.com/'


def two_digits(n):
    return format(int(n), '02d')


def get_trending_repo(key, year_from, month_from, day_from, year_to, month_to, day_to):
    url = base + 'search/repositories?q=' + key
    url += '+created:' + two_digits(year_from) + '-' + two_digits(month_from) + '-' + two_digits(day_from)
    url += '..' + two_digits(year_to) + '-' + two_digits(month_to) + '-' + two_digits(day_to)
    url += '&sort=stars'
    url += '&order=desc'
    r = requests.get(url)
    return r


def build_repo_from_request(request):
    json_repos = request.json()['items']
    repos = []
    for json_repo in json_repos:
        repos.append(Repository(json_repo))
    return repos
