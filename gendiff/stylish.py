import pdb
from pprint import pprint


def format_diff_dict(diff_dict, depth=1):
    prefix = '    '
    result = ''
    for key in sorted(diff_dict.keys()):

        if type(diff_dict[key]) == dict:
            result += f'{prefix * depth}{key}:\n' + format_diff_dict(diff_dict[key], depth + 1)
        else:
            result += f'{prefix * depth}{key}: {diff_dict[key]}\n'
    result += '\n'

    return result
