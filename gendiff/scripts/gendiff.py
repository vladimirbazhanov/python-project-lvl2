import argparse


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')

    parser.add_argument('first_file', type=argparse.FileType('r'))
    parser.add_argument('second_file', type=argparse.FileType('r'))
    parser.add_argument('--format', required=False, metavar='FORMAT', default='plain', help='set format of output')

    args = parser.parse_args()
    print(args.accumulate(args.integers))
