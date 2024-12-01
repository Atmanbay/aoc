import re
from collections import Counter


def parse_input(input):
    left, right = zip(*(
        map(int, re.findall(r"\d+", line))
        for line in input
    ))
    return list(left), list(right)


def part1(input):
    left, right = parse_input(input)
    left_sorted = sorted(left)
    right_sorted = sorted(right)
    return sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))


def part2(input):
    left, right = parse_input(input)
    right_counts = Counter(right)
    return sum(num * right_counts[num] for num in left)