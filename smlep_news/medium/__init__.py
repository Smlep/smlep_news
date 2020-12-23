import feedparser
import time

from datetime import datetime
from time import mktime


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
        stories = feedparser.parse("https://medium.com/feed/topic/{}".format(topic))

        if not stories.bozo:
            break
        time.sleep(retry_interval)

    return Feed(topic, stories)
