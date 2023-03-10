import json
import pdb

def generate_diff(file_path1, file_path2):
    file1_json_content = json.load(open(file_path1))
    file2_json_content = json.load(open(file_path2))

    diff = {}

    for key in file1_json_content.keys() | file2_json_content.keys():
        diff[key] = {}
        diff[key]['file1_value'] = file1_json_content.get(key)
        diff[key]['file2_value'] = file2_json_content.get(key)
        if not diff[key]['file1_value']:
            diff[key]['action'] = 'added'
        if not diff[key]['file2_value']:
            diff[key]['action'] = 'removed'
        if diff[key]['file1_value'] == diff[key]['file2_value']:
            diff[key]['action'] = 'unchanged'
        if diff[key]['file1_value'] and diff[key]['file2_value']:
            if diff[key]['file1_value'] != diff[key]['file2_value']:
                diff[key]['action'] = 'changed'

    return diff
