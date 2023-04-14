import pdb

from gendiff.gendiff import generate_diff

def test_generate_diff_json():
    result = generate_diff('tests/fixtures/json/file_001.json', 'tests/fixtures/json/file_002.json')
    with open('tests/fixtures/json/file_001_file_002.result.txt', 'r') as fixture:
        expected_result = fixture.read()
        assert result == expected_result


def test_generate_diff_r_json():
    result = generate_diff('tests/fixtures/r_json/r_file_001.json', 'tests/fixtures/r_json/r_file_002.json')
    with open('tests/fixtures/r_json/r_file_001_r_file_002.result.txt', 'r') as fixture:
        expected_result = fixture.read()
        assert result == expected_result


def test_generate_diff_yaml():
    result = generate_diff('tests/fixtures/yaml/file_001.yml', 'tests/fixtures/yaml/file_002.yml')
    with open('tests/fixtures/yaml/file_001_file_002.result.txt', 'r') as fixture:
        expected_result = fixture.read()
        assert result == expected_result