from gendiff.cli import args_parse
from gendiff.gendiff import generate_diff


def main():
    args = args_parse()

    diff_string = generate_diff(args.first_file, args.second_file, args.format)

    print(diff_string)
