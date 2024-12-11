from math import log10


def zero_to_one(number):
    if number == 0:
        return [1]
    return None
    
    
def split_in_two(number):
    digits = int(log10(number)) + 1
    if digits % 2 == 0:
        num_as_str = str(number)
        return [int(num_as_str[:digits // 2]), int(num_as_str[digits // 2:])]
    return None
    

def multiply(number):
    return [number * 2024]


RULES = [zero_to_one, split_in_two, multiply]


def parse_input(input):
    return list(map(int, input.split(" ")))


def apply_rules(number):
    for rule in RULES:
        result = rule(number)
        if result is not None:
            return result
    return [number]


def count_stones(memo, number, blinks_left):
    if (number, blinks_left) in memo:
        return memo[(number, blinks_left)]
    
    if blinks_left == 0:
        return 1 # just count the given number
    
    count = 0
    for new_number in apply_rules(number):
        count += count_stones(memo, new_number, blinks_left - 1)
    
    memo[(number, blinks_left)] = count
    return count


def watch_stones(input, blink_count):
    total_stones = 0
    memo = {}
    
    for stone in parse_input(input):
        total_stones += count_stones(memo, stone, blink_count)
    
    return total_stones


def part1(input):
    return watch_stones(input, 25)


def part2(input):
    return watch_stones(input, 75)
