import argparse
from gendiff.loader import load_file
from gendiff.gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )

    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-f',
        '--format',
        required=False,
        metavar='FORMAT',
        default='stylish',
        help='set format of output'
    )

    args = parser.parse_args()
    
    file1_content = load_file(args.first_file)
    file2_content = load_file(args.second_file)

    diff_string = generate_diff(file1_content, file2_content, args.format)

    print(diff_string)
