import itertools


INDENT = '  '
DEEP_INDENT = '    '
ADDED = '+'
REMOVED = '-'


def format(tree, depth=0):

    def iter_(node, path=''):
        current_path = f"{path}{node['key']}"

        if node['kind'] == 'removed':
            return f"Property '{current_path}' was removed"

        elif node['kind'] == 'added':
            return f"Property '{current_path}' was added" \
                   f" with value: {to_s(node['value'])}"

        elif node['kind'] == 'nested':
            node_children = sorted(
                node['children'], key=lambda item: item['key'])
            nested_lines = map(
                lambda child: iter_(
                    child, f"{current_path}."), node_children)
            result = itertools.chain(nested_lines)
            return '\n'.join(filter(lambda item: item, result))

        elif node['kind'] == 'changed':
            return f"Property '{current_path}' was updated." \
                   f" From {to_s(node['value'][0])}" \
                   f" to {to_s(node['value'][1])}"

    children = children = sorted(
        tree.get('children'), key=lambda node: node['key'])
    lines = map(lambda child: iter_(child), children)
    result = itertools.chain(lines)
    return '\n'.join(filter(lambda item: item, result))


def get_indent(depth):
    if depth == 1:
        return INDENT
    else:
        return INDENT + (DEEP_INDENT * (depth - 1))


def to_s(value):
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
