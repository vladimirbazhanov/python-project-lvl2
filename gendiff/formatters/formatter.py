import importlib


ALLOWED_FORMATS = ['plain', 'stylish']


def format_diff(diff_tree, format):
    if format not in ALLOWED_FORMATS:
        raise Exception('Format not supported: ' + format)

    formatter = importlib.import_module('gendiff.formatters.' + format)

    return formatter.format(diff_tree)
