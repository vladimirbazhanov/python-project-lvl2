from gendiff.loader import load_file
from gendiff.parser import generate_tree
from gendiff.formatters.formatter import format_diff


def generate_diff(file_path1, file_path2, format='stylish'):
    file1_content = load_file(file_path1)
    file2_content = load_file(file_path2)

    diff_tree = generate_tree(file1_content, file2_content)
    diff_visualization = format_diff(diff_tree, format)

    return diff_visualization
