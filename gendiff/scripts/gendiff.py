import argparse
from gendiff.gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )

    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '--format',
        required=False,
        metavar='FORMAT',
        default='stylish',
        help='set format of output'
    )

    args = parser.parse_args()

    diff_string = generate_diff(args.first_file, args.second_file)

    print(diff_string)
