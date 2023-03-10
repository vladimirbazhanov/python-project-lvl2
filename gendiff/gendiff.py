from gendiff.loader import load_file
from gendiff.parser import parse


def generate_diff(file_path1, file_path2):
    file1_content = load_file(file_path1)
    file2_content = load_file(file_path2)

    diff_dict = parse(file1_content, file2_content)

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
