def parse_input(input):
    return [list(line) for line in input.splitlines()]


def get_region_cost(grid, coord, plant_type, visited):
    row_count = len(grid)
    col_count = len(grid[0])
    stack = [coord]
    region = []
    perimeter = 0

    while stack:
        row, col = stack.pop()

        if (row, col) in visited:
            continue
        visited.add((row, col))
        region.append((row, col))

        for row_diff, col_diff in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row = row + row_diff
            new_col = col + col_diff
            if 0 <= new_row < row_count and 0 <= new_col < col_count:
                if grid[new_row][new_col] == plant_type:
                    stack.append((new_row, new_col))
                else:
                    perimeter += 1
            else:
                perimeter += 1

    return len(region) * perimeter


def get_total_cost(grid):
    visited = set()
    total_cost = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row, col) not in visited:
                plant_type = grid[row][col]
                total_cost += get_region_cost(grid, (row, col), plant_type, visited)

    return total_cost


def part1(input):
    grid = parse_input(input)
    return get_total_cost(grid)


def part2(input):
    pass