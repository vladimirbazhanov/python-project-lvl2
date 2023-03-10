import argparse
from gendiff.gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')

    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('--format', required=False, metavar='FORMAT', default='plain', help='set format of output')

    args = parser.parse_args()

    diff_dict = generate_diff(args.first_file, args.second_file)

    diff_string = print_diff_dict(diff_dict)

    print(diff_string)

def print_diff_dict(diff_dict):
    result_string = "{\n"

    for key, info_dict in sorted(diff_dict.items()):
        if info_dict['action'] == 'added':
            result_string += f"  + {key}: {info_dict['file2_value']}\n"
        if info_dict['action'] == 'removed':
            result_string += f"  - {key}: {info_dict['file1_value']}\n"
        if info_dict['action'] == 'changed':
            result_string += f"  - {key}: {info_dict['file1_value']}\n"
            result_string += f"  + {key}: {info_dict['file2_value']}\n"
        if info_dict['action'] == 'unchanged':
            result_string += f"    {key}: {info_dict['file1_value']}\n"
    result_string += "}\n"

    return result_string

