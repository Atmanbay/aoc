CARET_TO_TUPLE = {
    '<': (0, -1),
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
}

DIRECTIONS = list(CARET_TO_TUPLE.values())
BLOCKER = "#"

def parse_input(input):
    grid = []
    blockers = []
    position = None
    direction = None

    for row_index, line in enumerate(input.splitlines()):
        row = list(line)
        grid.append(row)

        for col_index, char in enumerate(row):
            if char in CARET_TO_TUPLE:
                position = (row_index, col_index)
                direction = CARET_TO_TUPLE[char]
            if char == BLOCKER:
                blockers.append((row_index, col_index))

    return grid, position, direction

def move(position, direction):
    return tuple(sum(x) for x in zip(position, direction))

def turn(direction):
    next_index = (DIRECTIONS.index(direction) + 1) % len(DIRECTIONS)
    return DIRECTIONS[next_index]


def part1(input):
    grid, position, direction = parse_input(input)
    visited = set()
    visited.add(position)
    while position:
        new_position = move(position, direction)
        if new_position[0] >= len(grid) or new_position[0] < 0 or new_position[1] >= len(grid[new_position[0]]) or new_position[1] < 0:
            return len(visited)
        elif grid[new_position[0]][new_position[1]] == BLOCKER:
            direction = turn(direction)
        else:
            visited.add(new_position)
            position = new_position


def part2(input):
    return "the correct answer"
