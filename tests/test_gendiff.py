from gendiff.gendiff import generate_diff
import pytest


def test_generate_diff_json():
    result = generate_diff('tests/fixtures/json/file_001.json', 'tests/fixtures/json/file_002.json')
    f = open('tests/fixtures/json/file_001_file_002.result.txt', 'r')
    expected_result = f.read()
    f.close()
    assert result == expected_result

def test_generate_diff_yaml():
    result = generate_diff('tests/fixtures/yaml/file_001.yml', 'tests/fixtures/yaml/file_002.yml')
    f = open('tests/fixtures/yaml/file_001_file_002.result.txt', 'r')
    expected_result = f.read()
    f.close()
    assert result == expected_result