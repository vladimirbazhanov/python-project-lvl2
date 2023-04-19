import os


json_files = [
    os.path.join(os.path.dirname(__file__), 'fixtures/json/file_1.json'),
    os.path.join(os.path.dirname(__file__), 'fixtures/json/file_2.json')
]

yaml_files = [
    os.path.join(os.path.dirname(__file__), 'fixtures/yaml/file_1.yml'),
    os.path.join(os.path.dirname(__file__), 'fixtures/yaml/file_2.yml')
]


def read_expected_result(from_format, to_format):
    return open(
        os.path.join(
            os.path.dirname(__file__), f"fixtures/{from_format}/result.{to_format}.txt"
        )
    ).read()


file_set_1 = [
    [json_files[0], json_files[1], 'plain', read_expected_result('json', 'plain')],
    [json_files[0], json_files[1], 'stylish', read_expected_result('json', 'stylish')],
    [yaml_files[0], yaml_files[1], 'plain', read_expected_result('yaml', 'plain')],
    [yaml_files[0], yaml_files[1], 'stylish', read_expected_result('yaml', 'stylish')]
]

file_set_2 = [
    [json_files[0], json_files[1], 'json', read_expected_result('json', 'json')],
    [yaml_files[0], yaml_files[1], 'json', read_expected_result('yaml', 'json')]
]
