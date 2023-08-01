import gendiff.formatters.json as json
import gendiff.formatters.plain as plain
import gendiff.formatters.stylish as stylish


def format_diff(diff_tree, format):
    formatters = {
        'json': json,
        'plain': plain,
        'stylish': stylish
    }

    if format not in formatters.keys():
        raise Exception('Format not supported: ' + format)

    formatter = formatters[format]

    return formatter.format(diff_tree)
