import re


def part1(input):
    return sum([int(a) * int(b) for a, b in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", input)])


def part2(input):
    enabled = True
    sum = 0
    tokens = re.findall(r"(don't|do|mul)\((?:(\d{1,3}),(\d{1,3}))?\)", input)

    for token in tokens:
        keyword, val1, val2 = token
        if keyword == "do":
            enabled = True
        elif keyword == "don't":
            enabled = False
        elif keyword == "mul" and enabled:
            sum += int(val1) * int(val2)

    return sum
