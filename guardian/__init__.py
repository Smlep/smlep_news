import json
import requests

with open('config.json', 'r') as f:
    config = json.load(f)

apiKey = config['DEFAULT']['GUARDIAN_KEY']
base = 'https://content.guardianapis.com/'


def get_articles():
    url = base + 'search'
    url += '?api-key=' + apiKey


    r = requests.get(url)
    return r
