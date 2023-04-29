import json
import os

import pytest
from deepdiff import DeepDiff
from gendiff.gendiff import generate_diff


@pytest.fixture(scope='function')
def prepared_files(request):
    file1_path, file2_path, result_file_path, formatter_name = request.param
    fixtures_path = os.path.join(os.path.dirname(__file__), 'fixtures')
    expected_result = open(os.path.join(fixtures_path, result_file_path)).read()

    return os.path.join(fixtures_path, file1_path), os.path.join(fixtures_path, file2_path), expected_result, formatter_name


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
