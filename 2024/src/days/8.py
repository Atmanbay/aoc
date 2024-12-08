from itertools import combinations


def parse_input(input):
    node_dict = {}
    lines = input.splitlines()
    for row_index, line in enumerate(lines):
        for col_index, char in enumerate(line):
            if char.isalnum():
                node_dict.setdefault(char, []).append((row_index, col_index))
    grid_height = len(lines)
    grid_width = len(lines[0])
    return node_dict, grid_height, grid_width


def sub_coords(coordsA, coordsB):
    return tuple(a - b for a, b in zip(coordsA, coordsB))


def add_coords(coordsA, coordsB):
    return tuple(sum(x) for x in zip(coordsA, coordsB))


def get_antinodes(coords):
    diff = sub_coords(coords[0], coords[1])
    return [add_coords(coords[0], diff), sub_coords(coords[1], diff)]


def get_antinodes_p2(coords, grid_height, grid_width):
    antinodes = []
    diff = sub_coords(coords[0], coords[1])

    antinodes.append(coords[0])
    antinodes.append(coords[1])

    antinode_a = add_coords(coords[0], diff)
    while is_within_bounds(antinode_a, grid_height, grid_width):
        antinodes.append(antinode_a)
        antinode_a = add_coords(antinode_a, diff)

    antinode_b = sub_coords(coords[1], diff)
    while is_within_bounds(antinode_b, grid_height, grid_width):
        antinodes.append(antinode_b)
        antinode_b = sub_coords(antinode_b, diff)

    return antinodes


def is_within_bounds(coords, grid_height, grid_width):
    row, col = coords
    return 0 <= row < grid_height and 0 <= col < grid_width


def part1(input):
    antinodes = set()
    node_dict, grid_height, grid_width = parse_input(input)
    for locations in node_dict.values():
        for coord_combo in list(combinations(locations, 2)):
            possible_antinodes = get_antinodes(coord_combo)
            for antinode in possible_antinodes:
                if is_within_bounds(antinode, grid_height, grid_width):
                    antinodes.add(antinode)

    return len(antinodes)


def part2(input):
    antinodes = set()
    node_dict, grid_height, grid_width = parse_input(input)
    for locations in node_dict.values():
        for coord_combo in list(combinations(locations, 2)):
            possible_antinodes = get_antinodes_p2(coord_combo, grid_height, grid_width)
            for antinode in possible_antinodes:
                if is_within_bounds(antinode, grid_height, grid_width):
                    antinodes.add(antinode)
            
    return len(antinodes)