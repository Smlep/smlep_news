def build_list_from_request(request, field, object_type):
    json_repos = request.json()[field]
    repos = []
    for json_repo in json_repos:
        repos.append(object_type(json_repo))
    return repos
