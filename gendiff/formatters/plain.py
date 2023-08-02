import itertools


def format(tree, depth=0):
    def iter_(node, path=''):
        kind = node['kind']
        value = node.get('value', None)
        key = node['key']

        current_path = f"{path}{key}"

        if kind == 'removed':
            return f"Property '{current_path}' was removed"

        elif kind == 'added':
            return f"Property '{current_path}' was added" \
                   f" with value: {to_string(value)}"

        elif kind == 'nested':
            node_children = sorted(
                node['children'], key=lambda item: item['key'])
            nested_lines = map(
                lambda child: iter_(
                    child, f"{current_path}."), node_children)
            result = itertools.chain(nested_lines)
            return '\n'.join(filter(lambda item: item, result))

        elif kind == 'changed':
            return f"Property '{current_path}' was updated." \
                   f" From {to_string(value[0])}" \
                   f" to {to_string(value[1])}"

    children = children = sorted(
        tree.get('children'), key=lambda node: node['key'])
    lines = map(lambda child: iter_(child), children)
    result = itertools.chain(lines)
    return '\n'.join(filter(lambda item: item, result))


def to_string(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, int):
        return value
    elif value is None:
        return 'null'
    else:
        return f"'{value}'"
