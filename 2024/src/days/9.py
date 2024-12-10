
def parse_input(input):
    nums = map(int, input)
    expanded = []
    id = 0

    for is_file, num in zip([True, False] * len(input), nums):
        expanded.extend(str(id) if is_file else None for _ in range(num))
        if is_file:
            id += 1

    return expanded


def get_last_id(nums: list):
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] is not None:
            val = nums[i]
            nums[i] = None
            return int(val), i
    return None, None


def part1(input):
    expanded = parse_input(input)
    result = 0

    for index, entry in enumerate(expanded):
        if entry:
            result += index * int(entry)
        else:
            last_id, last_id_index = get_last_id(expanded)
            if last_id and index < last_id_index:
                result += index * last_id
    return result    


def get_new_location(file, spaces):
    for space_index, space in enumerate(spaces):
        if space >= file:
            return True, space_index

    return False, None


def get_index_from_space(space_index, files, spaces, spaces_filled):
    files_o = files[:(space_index + 1)]
    spaces_o = spaces[:(space_index)]
    relevant_spaces_filled = [value for key, value in spaces_filled.items() if key < space_index]
    return sum(files_o) + sum(spaces_o) + sum(relevant_spaces_filled)


def get_index_from_file(file_index, files, spaces, spaces_filled):
    files_o = files[:(file_index)]
    spaces_o = spaces[:(file_index)]
    relevant_spaces_filled = [value for key, value in spaces_filled.items() if key < file_index]
    return sum(files_o) + sum(spaces_o) + sum(relevant_spaces_filled)


def part2(input):
    # this works for the example but not my input. might revisit
    checksum = 0
    chars = list(input)

    files = [int(chars[i]) for i in range(len(chars)) if i % 2 == 0]
    spaces = [int(chars[i]) for i in range(len(chars)) if i % 2 != 0]
    spaces_filled = {} # key matches `spaces` index but value is the count of how many of those spaces at that index have been filled already

    for file_index in range(len(files) - 1, -1, -1):
        file_length = files[file_index]
        can_move, space_index = get_new_location(file_length, spaces)
        if can_move:
            spaces[space_index] = spaces[space_index] - file_length
            master_index = get_index_from_space(space_index, files, spaces, spaces_filled)
            index_to_check = master_index
            if space_index in spaces_filled:
                index_to_check += spaces_filled[space_index]
            for offset in range(file_length):
                new_sum = (index_to_check + offset) * file_index
                
                checksum += new_sum

            if space_index not in spaces_filled:
                spaces_filled[space_index] = file_length
            else:
                spaces_filled[space_index] += file_length
        else:
            master_index = get_index_from_file(file_index, files, spaces, spaces_filled)
            for offset in range(file_length):
                new_sum = (master_index + offset) * file_index
                checksum += new_sum

    return checksum