from re import findall

NEXT_LETTER_MAPPING = {
    "X": "M",
    "M": "A",
    "A": "S"
}


def parse_input(input):
    return [list(line) for line in input.split('\n')]


def check(grid, current_char, row, col, row_diff, col_diff):
    if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
        return 0

    if current_char == "S":
        return 1

    char_to_check = NEXT_LETTER_MAPPING[current_char]

    next_row = row + row_diff
    next_col = col + col_diff

    if not (0 <= next_row < len(grid) and 0 <= next_col < len(grid[0])):
        return 0

    if grid[next_row][next_col] == char_to_check:
        return check(grid, char_to_check, next_row, next_col, row_diff, col_diff)

    return 0


def part1(input):
    occurrences = 0
    grid = parse_input(input)

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "X":
                for row_diff in [-1, 0, 1]:
                    for col_diff in [-1, 0, 1]:
                        if row_diff != 0 or col_diff != 0:
                            occurrences += check(grid, "X", row, col, row_diff, col_diff)

    return occurrences


REGEXS = [
    r"M.S.A.M.S",
    r"M.M.A.S.S",
    r"S.M.A.S.M",
    r"S.S.A.M.M",
]

def part2(input):
    occurrences = 0
    grid = parse_input(input)

    row_count = len(grid)
    col_count = len(grid[0])

    for start_row in range(row_count - 2):
        for start_col in range(col_count - 2): 
            section = ""

            for r in range(start_row, start_row + 3):
                row = ""
                for c in range(start_col, start_col + 3):
                    row += grid[r][c]
                section += row

            for regex in REGEXS:
                result = findall(regex, section)
                if result:
                    occurrences += 1

    return occurrences
