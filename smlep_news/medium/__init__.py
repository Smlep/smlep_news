import feedparser
import requests
import time

from bs4 import BeautifulSoup
from datetime import datetime
from time import mktime

topic_feed_url = "https://medium.com/feed/topic/{}"
topics_page_url = "https://medium.com/topics"


class Story:
    def __init__(self, d: feedparser.util.FeedParserDict):
        self.title = d.title
        self.html_summary = d.summary
        self.author = d.author
        self.link = d.link
        self.id_link = d.id

    def __repr__(self):
        return "{} from {}".format(self.title, self.author)


class Feed:
    def __init__(self, topic: str, d: feedparser.util.FeedParserDict):
        self.topic = topic
        self.updated = datetime.fromtimestamp(mktime(d.feed["updated_parsed"]))
        self.stories = [Story(e) for e in d.entries]

    def __repr__(self):
        return "{} feed on {}".format(self.topic, self.updated)


def get_top_topic_stories(topic: str, retry_count=1, retry_interval=0):
    """
    When querying to many topics one after the other, the requests might start failing.
    To fix this, increase the retry_count and retry_interval.
    """
    for i in range(retry_count):
        stories = feedparser.parse(topic_feed_url.format(topic))

        if not stories.bozo:
            break
        time.sleep(retry_interval)

    return Feed(topic, stories)


def build_topics_list():
    """
    Builds topics list.
    This function relies on scrapping the topics page, meaning it is not robust
    and might stop working.

    To avoid calling it every time, a list of topics is stores in medium/topics.json
    """
    response = requests.get(topics_page_url)
    soup = BeautifulSoup(response.content, "html.parser")
    topics_links = soup.select("a[href*=\/topic\/]")
    return {
        t.text: {"link": t.get("href"), "short_name": t.get("href").split("/")[-1]}
        for t in topics_links
        if t.text
    }
