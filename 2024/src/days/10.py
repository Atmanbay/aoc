offsets = [
    (-1, 0),  # Up
    (1, 0),   # Down
    (0, -1),  # Left
    (0, 1)    # Right
]

def parse_input(input):
    grid = []
    trailheads = []

    for row_index, line in enumerate(input.splitlines()):
        row = list(line)
        for col_index, cell in enumerate(row):
            if cell == "0":
                trailheads.append((row_index, col_index))
        grid.append(row)

    return grid, trailheads

def follow_trail(current, grid, visited, is_part_2 = False):
    rows = len(grid)
    cols = len(grid[0])
    trail_score = 0

    for row_diff, col_diff in offsets:
        new_row, new_col = current[0] + row_diff, current[1] + col_diff
        if 0 <= new_row < rows and 0 <= new_col < cols:
            new_cell = (new_row, new_col)
            if new_cell not in visited:
                current_val = int(grid[current[0]][current[1]])
                new_val = int(grid[new_row][new_col])
                if new_val == current_val + 1:
                    visited.add(new_cell)
                    if new_val == 9: 
                        trail_score += 1
                    else:
                        trail_score += follow_trail(new_cell, grid, visited, is_part_2)
                    if is_part_2:
                        visited.remove(new_cell)

    return trail_score

def get_trailhead_score(trailhead, grid, is_part_2 = False):
    visited = set()
    visited.add(trailhead)
    return follow_trail(trailhead, grid, visited, is_part_2)

def part1(input):
    grid, trailheads = parse_input(input)
    total_score = 0

    for trailhead in trailheads:
        total_score += get_trailhead_score(trailhead, grid)

    return total_score

def part2(input):
    grid, trailheads = parse_input(input)
    total_score = 0

    for trailhead in trailheads:
        total_score += get_trailhead_score(trailhead, grid, True)

    return total_score
