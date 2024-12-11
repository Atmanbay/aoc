from math import log10


def zero_to_one(number):
    if number == 0:
        return True, [1]
    else:
        return False, [number]
    
def split_in_two(number):
    digits = int(log10(number)) + 1
    if digits % 2 == 0:
        num_as_str = str(number)
        return True, [int(num_as_str[:digits//2]), int(num_as_str[digits//2:])]
    else:
        return False, [number]
    
def multiply(number):
    return True, [number * 2024]

RULES = [zero_to_one, split_in_two, multiply]

def parse_input(input):
    return list(map(int, input.split(" ")))


def part1(input):
    stones = parse_input(input)
    
    for blink_index in range(25):
        new_stones = []
        for stone_index, stone in enumerate(stones):
            for rule in RULES:
                executed, result = rule(stone)
                if executed:
                    break

            if executed:
                new_stones.extend(result)
            else:
                new_stones.append(stone)

        stones = new_stones

    return len(stones)


def part2(input):
    stone_count = 0
    stones = parse_input(input)

    for stone_index, stone in enumerate(stones):
        print(f"stone: {stone_index}")
        child_stones = [stone]
        # print(f"stone: {stone}")
        # print(f"child_stones: {child_stones}")
        for blink_index in range(75):
            print(f"  blink: {blink_index}")
            new_stones = []
            for ns in child_stones:
                for rule in RULES:
                    executed, result = rule(ns)
                    if executed:
                        break

                if executed:
                    new_stones.extend(result)
                else:
                    new_stones.append(ns)

            child_stones = new_stones

        stone_count += len(child_stones)

    return stone_count


    # for blink_index in range(1):
    #     print(blink_index)
    #     new_stones = []
    #     for stone_index, stone in enumerate(stones):
    #         for rule in RULES:
    #             executed, result = rule(stone)
    #             if executed:
    #                 break

    #         if executed:
    #             new_stones.extend(result)
    #         else:
    #             new_stones.append(stone)

    #     stones = new_stones

    # return len(stones)