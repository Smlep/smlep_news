class Product:
    def __init__(self, post):
        self.name = post["name"]
        self.description = post["tagline"]
        self.votes = post["votes_count"]
        self.url = post["discussion_url"]

    def __str__(self):
        return self.name

    def short_string(self):
        res = ""
        res += self.name
        res += " ("
        res += str(self.votes)
        res += "): "
        res += self.description
        res += " url: "
        res += self.url
        return res
