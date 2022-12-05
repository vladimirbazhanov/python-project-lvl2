import json


def generate_diff(file_path1, file_path2):
    file1_json_content = json.load(open(file_path1))
    file2_json_content = json.load(open(file_path2))

    diff = {}

    for key in file1_json_content:
        if key in file2_json_content:
            if file1_json_content[key] == file2_json_content[key]:
                diff['  ' + key] = file1_json_content[key]
            else:
                diff['- ' + key] = file1_json_content[key]
                diff['+ ' + key] = file2_json_content[key]
        elif key not in file2_json_content:
            diff['- ' + key] = file1_json_content[key]
    for key in file2_json_content.keys() - file1_json_content.keys():
        diff['+ ' + key] = file2_json_content[key]

    return diff
