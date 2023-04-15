import pdb

from gendiff.gendiff import generate_diff

JSON_FILES = [
    'tests/fixtures/json/file_001.json',
    'tests/fixtures/json/file_002.json'
]

R_JSON_FILES = [
    'tests/fixtures/r_json/r_file_001.json',
    'tests/fixtures/r_json/r_file_002.json'
]

YAML_FILES = [
    'tests/fixtures/yaml/file_001.yml',
    'tests/fixtures/yaml/file_002.yml'
]

R_YAML_FILES = [
    'tests/fixtures/r_yaml/r_file_001.yml',
    'tests/fixtures/r_yaml/r_file_002.yml'
]


def test_generate_diff_json_to_plain():
    result = generate_diff(JSON_FILES[0], JSON_FILES[1], 'plain')
    with open('tests/fixtures/json/file_001_file_002.plain.txt', 'r') as fixture:
        expected_result = fixture.read()
        assert result == expected_result


def test_generate_diff_json_to_stylish():
    result = generate_diff(JSON_FILES[0], JSON_FILES[1], 'stylish')
    with open('tests/fixtures/json/file_001_file_002.stylish.txt', 'r') as fixture:
        expected_result = fixture.read()
        assert result == expected_result


def test_generate_diff_recursive_json_to_plain():
    result = generate_diff(R_JSON_FILES[0], R_JSON_FILES[1], 'plain')
    with open('tests/fixtures/r_json/r_file_001_r_file_002.plain.txt', 'r') as fixture:
        expected_result = fixture.read()
        assert result == expected_result


def test_generate_diff_recursive_json_to_stylish():
    result = generate_diff(R_JSON_FILES[0], R_JSON_FILES[1], 'stylish')
    with open('tests/fixtures/r_json/r_file_001_r_file_002.stylish.txt', 'r') as fixture:
        expected_result = fixture.read()
        assert result == expected_result


def test_generate_diff_yaml_to_plain():
    result = generate_diff(YAML_FILES[0], YAML_FILES[1], 'plain')
    with open('tests/fixtures/yaml/file_001_file_002.plain.txt', 'r') as fixture:
        expected_result = fixture.read()
        assert result == expected_result


def test_generate_diff_yaml_to_stylish():
    result = generate_diff(YAML_FILES[0], YAML_FILES[1], 'stylish')
    with open('tests/fixtures/yaml/file_001_file_002.stylish.txt', 'r') as fixture:
        expected_result = fixture.read()
        assert result == expected_result


def test_generate_diff_recursive_yaml_to_plain():
    result = generate_diff(R_YAML_FILES[0], R_YAML_FILES[1], 'plain')
    with open('tests/fixtures/r_yaml/r_file_001_r_file_002.plain.txt', 'r') as fixture:
        expected_result = fixture.read()
        assert result == expected_result


def test_generate_diff_recursive_yaml_to_stylish():
    result = generate_diff(R_YAML_FILES[0], R_YAML_FILES[1], 'stylish')
    with open('tests/fixtures/r_yaml/r_file_001_r_file_002.stylish.txt', 'r') as fixture:
        expected_result = fixture.read()
        assert result == expected_result
