import importlib


ALLOWED_FORMATS = ['stylish']


def format_diff(diff_tree, format):
    if not format in ALLOWED_FORMATS:
        raise Exception('Format not supported: ' + format)

    formatter = importlib.import_module('gendiff.formatters.' + format)

    return formatter.format(diff_tree)
