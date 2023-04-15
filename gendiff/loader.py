import pathlib
import json
import yaml


def load_file(file_path):
    file_extension = pathlib.Path(file_path).suffix

    with (open(file_path)) as file:
        if file_extension == '.json':
            file_content = json.load(file)
        elif file_extension in ['.yml', '.yaml']:
            file_content = yaml.safe_load(file)
        else:
            raise Exception('File type not supported: ' + file_path)

    return file_content
