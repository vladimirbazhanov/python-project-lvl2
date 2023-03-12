def generate_tree(initial_dict,final_dict):
    tree = {}
    tree_keys = list(initial_dict.keys() | final_dict.keys())
    for key in tree_keys:
        tree[key] = generate_node(key, initial_dict, final_dict)

    return tree


def process_value(value):
    if type(value) == bool:
        return str(value).lower()
    return value


def generate_node(key, initial_dict, final_dict):
    initial_value = initial_dict.get(key)
    final_value = final_dict.get(key)

    if initial_value is None:
        node = {
            'action': 'added',
            'value': process_value(final_value)
        }
    elif final_value is None:
        node = {
            'action': 'removed',
            'value': process_value(initial_value)
        }
    elif type(initial_value) == dict and type(final_value) == dict:
        node = {
            'action': 'level',
            'value': generate_tree(initial_value, final_value)
        }
    elif initial_value == final_value:
        node = {
            'action': 'unchanged',
            'value': process_value(initial_value)
        }
    elif initial_value != final_value:
        node = {
            'action': 'changed',
            'initial_value': process_value(initial_value),
            'final_value': process_value(final_value)
        }

    return node
