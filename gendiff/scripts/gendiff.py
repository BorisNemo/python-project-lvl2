#!/usr/bin/env python3
from gendiff.cli import args
from gendiff.generate_diff import generate_diff


def main():
    args_ = args()
    result_of_different = generate_diff(args_.first_file, args_.second_file)
    print(result_of_different)


if __name__ == '__main__':
    main()
