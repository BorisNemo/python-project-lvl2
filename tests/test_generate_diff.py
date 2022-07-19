from gendiff.core.generate_diff import generate_diff

import pytest


@pytest.fixture
def data():
    return [
        ["tests/fixtures/input/file1.json", "tests/fixtures/input/file2.json"],
        ["tests/fixtures/input/file1.yml", "tests/fixtures/input/file2.yml"],
        ["tests/fixtures/input/file1.yaml", "tests/fixtures/input/file2.yaml"]
    ]


def test_generate_diff(data):
    for files in data:
        file1, file2 = files
        with open("tests/fixtures/output/file1_file2_json_yml_diff.txt") as text:
            diff_result = text.read()
            assert generate_diff(file1, file2) == diff_result
