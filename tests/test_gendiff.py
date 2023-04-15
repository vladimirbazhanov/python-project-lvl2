import json
import yaml
from deepdiff import DeepDiff
from gendiff.gendiff import generate_diff

JSON_DATA = [
    json.loads(open('tests/fixtures/json/file_001.json').read()),
    json.loads(open('tests/fixtures/json/file_002.json').read())
]

RECURSIVE_JSON_DATA = [
    json.loads(open('tests/fixtures/r_json/r_file_001.json').read()),
    json.loads(open('tests/fixtures/r_json/r_file_002.json').read())
]

YAML_DATA = [
    yaml.safe_load(open('tests/fixtures/yaml/file_001.yml').read()),
    yaml.safe_load(open('tests/fixtures/yaml/file_002.yml').read())
]

RECURSIVE_YAML_DATA = [
    yaml.safe_load(open('tests/fixtures/r_yaml/r_file_001.yml').read()),
    yaml.safe_load(open('tests/fixtures/r_yaml/r_file_002.yml').read())
]


def test_generate_diff_json_to_plain():
    result = generate_diff(JSON_DATA[0], JSON_DATA[1], 'plain')
    with open('tests/fixtures/json/file_001_file_002.plain.txt', 'r') as fixture:
        expected_result = fixture.read()
        assert result == expected_result


def test_generate_diff_json_to_stylish():
    result = generate_diff(JSON_DATA[0], JSON_DATA[1], 'stylish')
    with open('tests/fixtures/json/file_001_file_002.stylish.txt', 'r') as fixture:
        expected_result = fixture.read()
        assert result == expected_result


def test_generate_diff_json_to_json():
    result = json.loads(generate_diff(JSON_DATA[0], JSON_DATA[1], 'json'))
    with open('tests/fixtures/json/file_001_file_002.json.txt', 'r') as fixture:
        expected_result = json.loads(fixture.read())
        sorted_result = sorted(result['diff'], key=lambda node: node['key'])
        sorted_expected_result = sorted(expected_result['diff'], key=lambda node: node['key'])
        assert sorted_result == sorted_expected_result


def test_generate_diff_recursive_json_to_plain():
    result = generate_diff(RECURSIVE_JSON_DATA[0], RECURSIVE_JSON_DATA[1], 'plain')
    with open('tests/fixtures/r_json/r_file_001_r_file_002.plain.txt', 'r') as fixture:
        expected_result = fixture.read()
        assert result == expected_result


def test_generate_diff_recursive_json_to_stylish():
    result = generate_diff(RECURSIVE_JSON_DATA[0], RECURSIVE_JSON_DATA[1], 'stylish')
    with open('tests/fixtures/r_json/r_file_001_r_file_002.stylish.txt', 'r') as fixture:
        expected_result = fixture.read()
        assert result == expected_result


def test_generate_diff_recursive_json_to_json():
    result = json.loads(generate_diff(RECURSIVE_JSON_DATA[0], RECURSIVE_JSON_DATA[1], 'json'))
    with open('tests/fixtures/r_json/r_file_001_r_file_002.json.txt', 'r') as fixture:
        expected_result = json.loads(fixture.read())
        assert DeepDiff(result, expected_result, ignore_order=True) == {}


def test_generate_diff_yaml_to_plain():
    result = generate_diff(YAML_DATA[0], YAML_DATA[1], 'plain')
    with open('tests/fixtures/yaml/file_001_file_002.plain.txt', 'r') as fixture:
        expected_result = fixture.read()
        assert result == expected_result


def test_generate_diff_yaml_to_stylish():
    result = generate_diff(YAML_DATA[0], YAML_DATA[1], 'stylish')
    with open('tests/fixtures/yaml/file_001_file_002.stylish.txt', 'r') as fixture:
        expected_result = fixture.read()
        assert result == expected_result


def test_generate_diff_yaml_to_json():
    result = json.loads(generate_diff(YAML_DATA[0], YAML_DATA[1], 'json'))
    with open('tests/fixtures/yaml/file_001_file_002.json.txt', 'r') as fixture:
        expected_result = json.loads(fixture.read())
        sorted_result = sorted(result['diff'], key=lambda node: node['key'])
        sorted_expected_result = sorted(expected_result['diff'], key=lambda node: node['key'])
        assert sorted_result == sorted_expected_result


def test_generate_diff_recursive_yaml_to_plain():
    result = generate_diff(RECURSIVE_YAML_DATA[0], RECURSIVE_YAML_DATA[1], 'plain')
    with open('tests/fixtures/r_yaml/r_file_001_r_file_002.plain.txt', 'r') as fixture:
        expected_result = fixture.read()
        assert result == expected_result


def test_generate_diff_recursive_yaml_to_stylish():
    result = generate_diff(RECURSIVE_YAML_DATA[0], RECURSIVE_YAML_DATA[1], 'stylish')
    with open('tests/fixtures/r_yaml/r_file_001_r_file_002.stylish.txt', 'r') as fixture:
        expected_result = fixture.read()
        assert result == expected_result


def test_generate_diff_recursive_yaml_to_json():
    result = json.loads(generate_diff(RECURSIVE_YAML_DATA[0], RECURSIVE_YAML_DATA[1], 'json'))
    with open('tests/fixtures/r_yaml/r_file_001_r_file_002.json.txt', 'r') as fixture:
        expected_result = json.loads(fixture.read())
        assert DeepDiff(result, expected_result, ignore_order=True) == {}
