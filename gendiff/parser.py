def parse(file1_content, file2_content):
    diff_dict = {}

    for key in file1_content.keys() | file2_content.keys():
        diff_dict[key] = {}
        diff_dict[key]['file1_value'] = file1_content.get(key)
        diff_dict[key]['file2_value'] = file2_content.get(key)
        if not diff_dict[key]['file1_value']:
            diff_dict[key]['action'] = 'added'
        if not diff_dict[key]['file2_value']:
            diff_dict[key]['action'] = 'removed'
        if diff_dict[key]['file1_value'] == diff_dict[key]['file2_value']:
            diff_dict[key]['action'] = 'unchanged'
        if diff_dict[key]['file1_value'] and diff_dict[key]['file2_value']:
            if diff_dict[key]['file1_value'] != diff_dict[key]['file2_value']:
                diff_dict[key]['action'] = 'changed'

    return diff_dict
