import pdb

from gendiff.loader import load_file
from gendiff.parser import generate_tree


def generate_diff(file_path1, file_path2):
    file1_content = load_file(file_path1)
    file2_content = load_file(file_path2)

    diff_dict = generate_tree(file1_content, file2_content)

    diff_string = "{\n"

    for key, info_dict in sorted(diff_dict.items()):
        if info_dict['action'] == 'added':
            diff_string += f"  + {key}: {info_dict['value']}\n"
        if info_dict['action'] == 'removed':
            diff_string += f"  - {key}: {info_dict['value']}\n"
        if info_dict['action'] == 'changed':
            diff_string += f"  - {key}: {info_dict['initial_value']}\n"
            diff_string += f"  + {key}: {info_dict['final_value']}\n"
        if info_dict['action'] == 'unchanged':
            diff_string += f"    {key}: {info_dict['value']}\n"
    diff_string += "}\n"

    return diff_string
