import json
import requests
from .product import Product

with open("config.json", "r") as f:
    config = json.load(f)

base = "https://api.producthunt.com/v1/"
developer_token = config["DEFAULT"]["PH_KEY"]


def get_top_scores(year, month=0, day=0, count=50):
    url = (
        base
        + "posts/all?sort_by=votes_count&order=desc&search[featured_year]="
        + str(year)
    )
    if month != 0:
        url += "&search[featured_month]=" + str(month)
    if day != 0:
        url += "&search[featured_day]=" + str(day)
    if count != 50:
        url += "&per_page=" + str(count)
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + developer_token,
        "Host": "api.producthunt.com",
    }
    r = requests.get(url, headers=headers)
    return r
