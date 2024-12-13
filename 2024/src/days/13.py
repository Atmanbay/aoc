from re import findall


def parse_input(input):
    pattern = r"Button\sA:\sX(\+|\-)(\d+),\sY(\+|\-)(\d+)\nButton\sB:\sX(\+|\-)(\d+),\sY(\+|\-)(\d+)\nPrize:\sX=(\d+),\sY=(\d+)"
    
    return [(
        (
            int(m[1]),
            int(m[3])
        ),
        (
            int(m[5]),
            int(m[7])
        ),
        (
            int(m[8]),
            int(m[9])
        )
    ) for m in findall(pattern, input)]


def is_divisible(prize, button):
    prize_x, prize_y = prize
    button_x, button_y = button

    return prize_x % button_x == 0 and button_x * 100 >= prize_x and prize_y % button_y == 0 and button_y * 100 >= prize_y


def get_minimum_tokens_reverse(machine):
    tokens = 0
    a, b, prize = machine
    location = prize

    for _ in range(100):
        location = (location[0] - b[0], location[1] - b[1])
        tokens += 3
        if is_divisible(location, a):
            break
    else:
        return 0

    for _ in range(100):
        location = (location[0] - a[0], location[1] - a[1])
        tokens += 1
        if location == (0, 0):
            break
    else:
        return 0

    return tokens



def get_minimum_tokens(machine):
    a, b, prize = machine

    location_a_first = prize
    tokens_a_first = 0
    for _ in range(100):
        location_a_first = (location_a_first[0] - a[0], location_a_first[1] - a[1])
        tokens_a_first += 3
        if is_divisible(location_a_first, b):
            break

    if not is_divisible(location_a_first, b):
        tokens_a_first = float('inf')
    else:
        for _ in range(100):
            location_a_first = (location_a_first[0] - b[0], location_a_first[1] - b[1])
            tokens_a_first += 1
            if location_a_first == (0, 0):
                break
        
    if location_a_first != (0, 0):
        tokens_a_first = float('inf')

    location_b_first = prize
    tokens_b_first = 0
    for _ in range(100):
        location_b_first = (location_b_first[0] - b[0], location_b_first[1] - b[1])
        tokens_b_first += 1
        if is_divisible(location_b_first, a):
            break

    if not is_divisible(location_b_first, a):
        tokens_b_first = float('inf')
    else:
        for _ in range(100):
            location_b_first = (location_b_first[0] - a[0], location_b_first[1] - a[1])
            tokens_b_first += 3
            if location_b_first == (0, 0):
                break        
    
    if location_b_first != (0, 0):
        tokens_b_first = float('inf')

    minimum_tokens = min(tokens_a_first, tokens_b_first)
    return minimum_tokens if minimum_tokens != float('inf') else 0


def part1(input):
    tokens = 0
    machines = parse_input(input)
    
    for machine in machines:
        tokens += get_minimum_tokens(machine)

    return tokens


def part2(input):
    pass