#!/usr/bin/env python3


def compare_versions(first_version, second_version):
    """
    Compares two version strings, returning:
    -1 if first_version < second_version, 
    0 if first_version = second_version and
    1 if first_version > second_version
    """

    if first_version == second_version:
        return 0

    first_version_numbers = [int(s) for s in first_version.split('.')]
    second_version_numbers = [int(s) for s in second_version.split('.')]

    first_array_size = len(first_version_numbers)
    second_array_size = len(second_version_numbers)
    n = max(first_array_size, second_array_size)

    for i in range(0, n):
        first = -1
        if i < first_array_size:
            first = first_version_numbers[i]

        second = -1
        if i < second_array_size:
            second = second_version_numbers[i]

        if first > second:
            return 1
        elif first < second:
            return -1


if __name__ == '__main__':
    from sys import stdin

    for line in stdin:
        first_version, second_version = line.strip().split(' ')

        result = compare_versions(first_version, second_version)

        if result == 0:
            print("Same version")
        elif result == 1:
            print("First version is newer than second version")
        else:
            print("First version is older than second version")
