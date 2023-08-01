import pathlib
import json
import yaml


def load_file(file_path):
    file_type = pathlib.Path(file_path).suffix
    file_content = open(file_path).read()

    return parse_file_content(file_content, file_type)


def parse_file_content(file_content, file_type):
    parsers = {
        '.json': parse_json,
        '.yml': parse_yaml,
        '.yaml': parse_yaml
    }

    parser = parsers.get(file_type, parser_not_supported)

    return parser(file_content)


def parse_json(data):
    return json.loads(data)


def parse_yaml(data):
    return yaml.safe_load(data)


def parser_not_supported(data):
    Exception('File type not supported: ' + file_path)
