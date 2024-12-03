from itertools import pairwise


def parse_input(input):
    return [
        list(map(int, line.split()))
        for line in input
    ]


def is_safe(report):
    differences = [b - a for a, b in pairwise(report)]

    is_increasing = all(diff > 0 for diff in differences)
    is_decreasing = all(diff < 0 for diff in differences)
    within_range = all(1 <= abs(diff) <= 3 for diff in differences)

    return (is_increasing or is_decreasing) and within_range


def part1(input):
    safe_count = 0
    reports = parse_input(input.splitlines())

    for report in reports:
        if is_safe(report):
            safe_count += 1

    return safe_count


def can_be_safe(report):
    for i in range(len(report)):
        if is_safe(report[:i] + report[i+1:]):
            return True
        
    return False


def part2(input):
    safe_count = 0
    reports = parse_input(input.splitlines())

    for report in reports:
        if is_safe(report) or can_be_safe(report):
            safe_count += 1

    return safe_count