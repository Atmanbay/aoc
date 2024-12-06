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

def add_coords(position, direction):
    return tuple(sum(x) for x in zip(position, direction))

def turn(direction):
    next_index = (DIRECTIONS.index(direction) + 1) % len(DIRECTIONS)
    return DIRECTIONS[next_index]

def is_within_grid(position, grid):
    row, col = position
    return 0 <= row < len(grid) and 0 <= col < len(grid[row])

def part1(input):
    return None
    # grid, position, direction = parse_input(input)
    # visited = set()
    # visited.add(position)
    # while position:
    #     new_position = add_coords(position, direction)
    #     if new_position[0] >= len(grid) or new_position[0] < 0 or new_position[1] >= len(grid[new_position[0]]) or new_position[1] < 0:
    #         return len(visited)
    #     elif grid[new_position[0]][new_position[1]] == BLOCKER:
    #         direction = turn(direction)
    #     else:
    #         visited.add(new_position)
    #         position = new_position

def part2(input):
    grid, position, direction = parse_input(input)
    original_col = position[1]
    blockers_hit = []
    created_blockers = set()

    while position:
        new_position = add_coords(position, direction)

        if not is_within_grid(new_position, grid):
            return len(created_blockers)

        if grid[new_position[0]][new_position[1]] == BLOCKER:
            blockers_hit.append(new_position)

            if len(blockers_hit) >= 3:
                newest_row, newest_col = blockers_hit[-1]  # most recent
                second_row, second_col = blockers_hit[-2]  # second most
                oldest_row, oldest_col = blockers_hit[-3]  # third most

                print(f"\nNewest {newest_row}, {newest_col}")
                print(f"Middle {second_row}, {second_col}")
                print(f"Oldest {oldest_row}, {oldest_col}\n")

                if (newest_row + 1 == second_row and second_col + 1 == oldest_col):  # Place at Top Left
                    created_blocker = (oldest_row - 1, newest_col + 1)
                elif (newest_col + 1 == second_col and second_row - 1 == oldest_row):  # Place at Bottom Left
                    created_blocker = (newest_row - 1, oldest_col - 1)
                elif (newest_col - 1 == second_col and second_row + 1 == oldest_row):  # Place at Top Right
                    created_blocker = (newest_row - 1, oldest_col + 1)
                elif (newest_row - 1 == second_row and second_col - 1 == oldest_col):  # Place at Bottom Right
                    created_blocker = (oldest_row + 1, newest_col - 1)
                else:
                    created_blocker = None

                if created_blocker and created_blocker != position and is_within_grid(created_blocker, grid):
                    print(created_blocker)
                    created_blockers.add(created_blocker)

            direction = turn(direction)
        else:
            position = new_position

    return len(created_blockers)