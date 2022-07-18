from gendiff.generate_diff import generate_diff

import pytest


@pytest.fixture
def data():
    file1 = "tests/fixtures/input/file1.json"
    file2 = "tests/fixtures/input/file2.json"
    return file1, file2


def test_generate_diff(data):
    file1, file2 = data
    with open("tests/fixtures/output/file1_fil2_diff.txt") as text:
        diff_result = text.read()
    assert generate_diff(file1, file2) == diff_result
