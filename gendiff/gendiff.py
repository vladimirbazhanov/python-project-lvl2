import json
import ipdb


def generate_diff(file_path1, file_path2):
    file1_json_content = json.load(open(file_path1))
    file2_json_content = json.load(open(file_path2))

    diff = {}

    for key in sorted(file1_json_content):
        if key in file2_json_content and file1_json_content[key] == file2_json_content[key]:
            diff[key] = file1_json_content[key]

    return diff
