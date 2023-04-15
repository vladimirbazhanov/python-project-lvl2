import itertools


INDENT = '  '
DEEP_INDENT = '    '
ADDED = '+'
REMOVED = '-'


def format(tree, depth=0):

    def iter_(node, depth):
        indent = get_indent(depth)

        if node['kind'] == 'removed':
            return f"{indent}{REMOVED} {node['key']}:" \
                   f" {to_s(node['value'], depth)}"

        elif node['kind'] == 'added':
            return f"{indent}{ADDED} {node['key']}:" \
                   f" {to_s(node['value'], depth)}"

        elif node['kind'] == 'nested':
            node_children = sorted(
                node['children'], key=lambda item: item['key'])
            nested_lines = map(
                lambda child: iter_(child, depth + 1), node_children)
            result = '\n'.join(nested_lines)
            return f"{indent}  {node['key']}: {{\n{result}\n  {indent}}}"

        elif node['kind'] == 'unchanged':
            return f"{indent}  {node['key']}:" \
                   f" {to_s(node['value'], depth)}"

        elif node['kind'] == 'changed':
            line_1 = f"{indent}{REMOVED} {node['key']}:" \
                     f" {to_s(node['value'][0], depth)}\n"
            line_2 = f"{indent}{ADDED} {node['key']}:" \
                     f" {to_s(node['value'][1], depth)}"
            return line_1 + line_2

    children = sorted(tree.get('children'), key=lambda node: node['key'])
    lines = map(lambda child: iter_(child, depth + 1), children)
    result = itertools.chain("{", lines, "}")
    return '\n'.join(result)


def get_indent(depth):
    if depth == 1:
        return INDENT
    else:
        return INDENT + (DEEP_INDENT * (depth - 1))


def to_s(value, depth):
    current_indent = get_indent(depth)

    if isinstance(value, dict):
        lines = []
        for key, val in value.items():
            lines.append(
                f"{INDENT + current_indent + DEEP_INDENT}{key}:"
                f" {to_s(val, depth + 1)}")
        result = '\n'.join(lines)
        return f'{{\n{result}\n  {current_indent}}}'
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return value
