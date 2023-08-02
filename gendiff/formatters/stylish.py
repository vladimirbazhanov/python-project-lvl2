import itertools


def format(tree, depth=0):
    def iter_(node, depth):
        kind = node['kind']
        value = node.get('value', None)
        key = node['key']

        if kind == 'added' or kind == 'removed' or kind == 'unchanged':
            return f"{get_indent(depth, kind)}{key}: {to_string(value, depth)}"

        elif kind == 'nested':
            node_children = sorted(
                node['children'], key=lambda item: item['key'])
            nested_lines = map(
                lambda child: iter_(child, depth + 1), node_children)
            result = '\n'.join(nested_lines)
            return f"{get_indent(depth, kind)}{key}:" \
                   f" {{\n{result}\n{get_indent(depth, kind)}}}"

        elif node['kind'] == 'changed':
            line_1 = f"{get_indent(depth, 'removed')}{key}:" \
                     f" {to_string(node['value'][0], depth)}\n"
            line_2 = f"{get_indent(depth, 'added')}{key}:" \
                     f" {to_string(node['value'][1], depth)}"
            return line_1 + line_2

    children = sorted(tree.get('children'), key=lambda node: node['key'])
    lines = map(lambda child: iter_(child, depth + 1), children)
    result = itertools.chain("{", lines, "}")
    return '\n'.join(result)


def get_indent(depth, sign_type=None):
    indent_line = (' ' * 4 * depth)[:-2]
    sign = get_sign(sign_type)

    if sign:
        indent_line = indent_line + f"{sign} "
    return indent_line


def get_sign(sign_type=None):
    signs = {
        'added': '+',
        'removed': '-',
        'unchanged': ' ',
        'nested': ' ',
        'key': ' '
    }
    return signs.get(sign_type, None)


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
