from itertools import product
from re import findall


def parse_input(input):
    pattern = r"(\d+)"
    return [list(map(int, findall(pattern, line))) for line in input.splitlines()]


def evaluate_config(numbers, operators):
    result = numbers[0]
    for i, operator in enumerate(operators):
        if operator == "+":
            result += numbers[i + 1]
        elif operator == "*":
            result *= numbers[i + 1]
        elif operator == "||":
            result = int(f"{result}{numbers[i + 1]}")
    
    return result


def is_valid_equation(target, numbers, operator_list):
    operator_count = len(numbers) - 1
    for operators in product(operator_list, repeat=operator_count):
        if evaluate_config(numbers, operators) == target:
            return True
    
    return False


def part1(input):
    equations = parse_input(input)
    result = 0
    operator_list = ["+", "*"]
    for equation in equations:
        target = equation[0]
        numbers = equation[1:]
        if is_valid_equation(target, numbers, operator_list):
            result += target
    return result


def part2(input):
    equations = parse_input(input)
    result = 0
    operator_list = ["+", "*", "||"]
    for equation in equations:
        target = equation[0]
        numbers = equation[1:]
        if is_valid_equation(target, numbers, operator_list):
            result += target
    return result