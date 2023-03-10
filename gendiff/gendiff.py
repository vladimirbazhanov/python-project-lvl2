import json


def generate_diff(file_path1, file_path2):
    file1_json_content = json.load(open(file_path1))
    file2_json_content = json.load(open(file_path2))

    diff_dict = {}

    for key in file1_json_content.keys() | file2_json_content.keys():
        diff_dict[key] = {}
        diff_dict[key]['file1_value'] = file1_json_content.get(key)
        diff_dict[key]['file2_value'] = file2_json_content.get(key)
        if not diff_dict[key]['file1_value']:
            diff_dict[key]['action'] = 'added'
        if not diff_dict[key]['file2_value']:
            diff_dict[key]['action'] = 'removed'
        if diff_dict[key]['file1_value'] == diff_dict[key]['file2_value']:
            diff_dict[key]['action'] = 'unchanged'
        if diff_dict[key]['file1_value'] and diff_dict[key]['file2_value']:
            if diff_dict[key]['file1_value'] != diff_dict[key]['file2_value']:
                diff_dict[key]['action'] = 'changed'

    diff_string = "{\n"

    for key, info_dict in diff_dict.items():
        if type(info_dict['file1_value']) == bool:
            info_dict['file1_value'] = str(info_dict['file1_value']).lower()
        if type(info_dict['file2_value']) == bool:
            info_dict['file2_value'] = str(info_dict['file2_value']).lower()

    for key, info_dict in sorted(diff_dict.items()):
        if info_dict['action'] == 'added':
            diff_string += f"  + {key}: {info_dict['file2_value']}\n"
        if info_dict['action'] == 'removed':
            diff_string += f"  - {key}: {info_dict['file1_value']}\n"
        if info_dict['action'] == 'changed':
            diff_string += f"  - {key}: {info_dict['file1_value']}\n"
            diff_string += f"  + {key}: {info_dict['file2_value']}\n"
        if info_dict['action'] == 'unchanged':
            diff_string += f"    {key}: {info_dict['file1_value']}\n"
    diff_string += "}\n"

    return diff_string
