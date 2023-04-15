from gendiff.gendiff import generate_diff


def test_generate_diff_json_to_plain():
    result = generate_diff(
        'tests/fixtures/json/file_001.json',
        'tests/fixtures/json/file_002.json', 'plain'
    )
    with open('tests/fixtures/json/file_001_file_002.plain.txt', 'r') as fixture:
        expected_result = fixture.read()
        assert result == expected_result


def test_generate_diff_json_to_stylish():
    result = generate_diff(
        'tests/fixtures/json/file_001.json',
        'tests/fixtures/json/file_002.json',
        'stylish'
    )
    with open('tests/fixtures/json/file_001_file_002.stylish.txt', 'r') as fixture:
        expected_result = fixture.read()
        assert result == expected_result


def test_generate_diff_recursive_json_to_plain():
    result = generate_diff(
        'tests/fixtures/r_json/r_file_001.json',
        'tests/fixtures/r_json/r_file_002.json',
        'plain'
    )
    with open('tests/fixtures/r_json/r_file_001_r_file_002.plain.txt', 'r') as fixture:
        expected_result = fixture.read()
        assert result == expected_result


def test_generate_diff_recursive_json_to_stylish():
    result = generate_diff(
        'tests/fixtures/r_json/r_file_001.json',
        'tests/fixtures/r_json/r_file_002.json',
        'stylish'
    )
    with open('tests/fixtures/r_json/r_file_001_r_file_002.stylish.txt', 'r') as fixture:
        expected_result = fixture.read()
        assert result == expected_result


def test_generate_diff_yaml_to_stylish():
    result = generate_diff(
        'tests/fixtures/yaml/file_001.yml',
        'tests/fixtures/yaml/file_002.yml',
        'stylish'
    )
    with open('tests/fixtures/yaml/file_001_file_002.stylish.txt', 'r') as fixture:
        expected_result = fixture.read()
        assert result == expected_result
