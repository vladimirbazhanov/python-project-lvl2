import pdb


def format_diff_dict(diff_dict, depth=1):
    diff_string = "{\n"
    for key in sorted(diff_dict.keys()):

        diff_string += format_key(key, diff_dict[key], depth)

    diff_string += "}\n"

    return diff_string

def format_key(key, info_dict, depth):
    prefix = '    ' * depth
    if info_dict['action'] == 'added':
        prefix = prefix[:-2] + '+ '
        return f"{prefix}{key}: {info_dict['value']}\n"
    if info_dict['action'] == 'removed':
        prefix = prefix[:-2] + '- '
        return f"{prefix}{key}: {info_dict['value']}\n"
    if info_dict['action'] == 'unchanged':
        return f"{prefix}{key}: {info_dict['value']}\n"
    if info_dict['action'] == 'changed':
        return f"{prefix[:-2] + '- '}{key}: {info_dict['initial_value']}\n" + f"{prefix[:-2] + '+ '}{key}: {info_dict['final_value']}\n"