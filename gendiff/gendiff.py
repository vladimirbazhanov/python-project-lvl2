from gendiff.loader import load_file
from gendiff.parser import generate_tree
from gendiff.formatters.stylish import get_stylish


def generate_diff(file_path1, file_path2):
    file1_content = load_file(file_path1)
    file2_content = load_file(file_path2)

    diff_dict = generate_tree(file1_content, file2_content)

    return get_stylish(diff_dict)
