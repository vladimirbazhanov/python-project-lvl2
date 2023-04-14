import pdb


def generate_tree(initial_dict, final_dict):
    return {'children': generate_nodes(initial_dict, final_dict)}


def generate_nodes(initial_dict, final_dict):
    nodes = []
    tree_keys = list(initial_dict.keys() | final_dict.keys())

    for key in tree_keys:
        initial_value = initial_dict.get(key)
        final_value = final_dict.get(key)
        node = {'key': key}

        if key not in initial_dict:
            node['kind'] = 'added'
            node['value'] = final_value
        elif key not in final_dict:
            node['kind'] = 'removed'
            node['value'] = initial_value
        elif type(initial_value) == dict and type(final_value) == dict:
            node['kind'] = 'nested'
            node['children'] = generate_nodes(initial_value, final_value)
        elif initial_value == final_value:
            node['kind'] = 'unchanged'
            node['value'] = initial_value
        elif initial_value != final_value:
            node['kind'] = 'changed'
            node['value'] = [initial_value, final_value]

        nodes.append(node)
    return nodes
