import json
import pytest
from deepdiff import DeepDiff
from gendiff.gendiff import generate_diff
from conftests import file_set_1, file_set_2

@pytest.mark.parametrize("file_1,file_2,format,expected_result", file_set_1)
def test_generate_diff(file_1, file_2, format, expected_result):
    result = generate_diff(file_1, file_2, format)

    assert result == expected_result


@pytest.mark.parametrize("file_1,file_2,format,expected_result", file_set_2)
def test_generate_diff_json(file_1, file_2, format, expected_result):
    result_json = json.loads(generate_diff(file_1, file_2, format))
    expected_result_json = json.loads(expected_result)

    assert DeepDiff(result_json, expected_result_json, ignore_order=True) == {}

