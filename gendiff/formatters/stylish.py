import itertools


INDENT = '  '
DEEP_INDENT = '  '
ADDED = '+'
REMOVED = '-'


def format(tree, depth=0):

    def iter_(node, depth):
        if node['kind'] == 'removed':
            return f"{get_indent(depth, node['kind'])}{node['key']}:" \
                   f" {to_string(node['value'], depth)}"

        elif node['kind'] == 'added':
            return f"{get_indent(depth, node['kind'])}{node['key']}:" \
                   f" {to_string(node['value'], depth)}"

        elif node['kind'] == 'nested':
            node_children = sorted(
                node['children'], key=lambda item: item['key'])
            nested_lines = map(
                lambda child: iter_(child, depth + 1), node_children)
            result = '\n'.join(nested_lines)
            return f"{get_indent(depth, node['kind'])}{node['key']}: {{\n{result}\n{get_indent(depth, node['kind'])}}}"

        elif node['kind'] == 'unchanged':
            return f"{get_indent(depth, node['kind'])}{node['key']}:" \
                   f" {to_string(node['value'], depth)}"

        elif node['kind'] == 'changed':
            line_1 = f"{get_indent(depth, 'removed')}{node['key']}:" \
                     f" {to_string(node['value'][0], depth)}\n"
            line_2 = f"{get_indent(depth, 'added')}{node['key']}:" \
                     f" {to_string(node['value'][1], depth)}"
            return line_1 + line_2

    children = sorted(tree.get('children'), key=lambda node: node['key'])
    lines = map(lambda child: iter_(child, depth + 1), children)
    result = itertools.chain("{", lines, "}")
    return '\n'.join(result)


def get_indent(depth, sign=None):
    signs = {
        'added': '+',
        'removed': '-',
        'unchanged': ' ',
        'nested': ' ',
        'key': ' '
    }
    sign = signs.get(sign, None)
    indent_line = (' ' * 4 * depth)[:-2]
    if sign:
        indent_line = indent_line + f"{sign} "
    return indent_line


def to_string(value, depth):
    if isinstance(value, dict):
        lines = []
        for key, val in value.items():
            lines.append(
                f"{get_indent(depth + 1, 'key')}{key}:"
                f" {to_string(val, depth + 1)}")
        result = '\n'.join(lines)
        return f'{{\n{result}\n  {get_indent(depth)}}}'
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return value
