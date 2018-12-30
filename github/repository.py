class Repository:
    def __init__(self, repo_json):
        self.name = repo_json['name']
        self.author = repo_json['owner']['login']
        self.description = repo_json['description']
        self.stars = repo_json['stargazers_count']

    def __str__(self):
        return self.name

    def short_string(self):
        res = ''
        res += self.name
        res += ' ('
        res += str(self.stars)
        res += '): '
        res += self.description
        res += ' author: '
        res += self.author
        return res
