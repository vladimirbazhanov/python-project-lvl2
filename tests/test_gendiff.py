import json

import pytest
from deepdiff import DeepDiff
from gendiff.gendiff import generate_diff


params_set = [
    ['file1.json', 'file2.json', 'json-to-json.txt', 'json'],
    ['file1.json', 'file2.json', 'json-to-plain.txt', 'plain'],
    ['file1.json', 'file2.json', 'json-to-stylish.txt', 'stylish'],
    ['file1.yml', 'file2.yml', 'yml-to-json.txt', 'json'],
    ['file1.yml', 'file2.yml', 'yml-to-plain.txt', 'plain'],
    ['file1.yml', 'file2.yml', 'yml-to-stylish.txt', 'stylish']
]


@pytest.mark.parametrize(argnames='prepared_files', argvalues=params_set, indirect=True)
def test_generate_diff(prepared_files):
    file1_path, file2_path, expected_result, formatter_name = prepared_files

    result = generate_diff(file1_path, file2_path, formatter_name)
    if formatter_name == 'json':
        assert DeepDiff(json.loads(result), json.loads(expected_result), ignore_order=True) == {}
    else:
        assert result == expected_result
