import argparse
from gendiff.gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')

    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('--format', required=False, metavar='FORMAT', default='plain', help='set format of output')

    args = parser.parse_args()

    diff_dict = generate_diff(args.first_file, args.second_file)

    print_diff_dict(diff_dict)


def print_diff_dict(diff_dict):
    print('{\n')
    for key, value in sorted(diff_dict.items()):
        print(f' {key}: {value}')
    print('}')
