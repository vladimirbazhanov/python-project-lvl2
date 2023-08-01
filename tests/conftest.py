import pytest
import os


@pytest.fixture(scope='function')
def prepared_files(request):
    file1_path, file2_path, result_file_path, formatter_name = request.param
    fixtures_path = os.path.join(os.path.dirname(__file__), 'fixtures')
    expected_result = open(os.path.join(fixtures_path, result_file_path)).read()

    return (os.path.join(fixtures_path, file1_path),
            os.path.join(fixtures_path, file2_path),
            expected_result,
            formatter_name)
