from gendiff.gendiff import generate_diff
import pytest


def test_generate_diff():
    result = generate_diff('tests/fixtures/file_001.json', 'tests/fixtures/file_002.json')
    f = open('tests/fixtures/file_001_file_002.txt', 'r')
    expected_result = f.read()
    f.close()
    assert result == expected_result
