import json


def format(tree):
    return json.dumps({'diff': tree['children']}, sort_keys=True)
