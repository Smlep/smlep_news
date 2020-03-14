class Product:
    def __init__(self, post):
        self.name = post["name"]
        self.description = post["tagline"]
        self.votes = post["votes_count"]
        self.url = post["discussion_url"]

    def __str__(self):
        return self.name

    def short_string(self):
        return "{} ({}): {} url: {}".format(
            self.name, self.votes, self.description, self.url
        )
