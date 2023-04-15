from gendiff.parser import generate_tree
from gendiff.formatters.formatter import format_diff


def generate_diff(file1_content, file2_content, format='stylish'):
    diff_tree = generate_tree(file1_content, file2_content)
    diff_visualization = format_diff(diff_tree, format)

    return diff_visualization
