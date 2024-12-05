def fix_recursively(page, rules_dict, seen, corrected_group, pages):
    if page in seen:
        return
    seen.add(page)

    if page in rules_dict:
        for before in rules_dict[page]:
            if before in pages and before not in corrected_group:
                fix_recursively(before, rules_dict, seen, corrected_group, pages)

    if page not in corrected_group:
        corrected_group.append(page)


def get_corrected_group_value(group, rules_dict):
    corrected_group = []
    seen = set()

    pages = [int(x) for x in group.split(",")]

    for page in pages:
        fix_recursively(page, rules_dict, seen, corrected_group, pages)
    
    return corrected_group[len(corrected_group) // 2]


def get_group_value(group, rules_dict, fixed_groups_only=False):
    pages = [int(x) for x in group.split(",")]
    group_length = len(pages)
    for i in range(group_length):
        page = pages[i]
        if page in rules_dict:
            befores = set(rules_dict[page])
            to_check = set(pages[i:])
            intersection = list(befores & to_check)
            if intersection:
                if fixed_groups_only:
                    return get_corrected_group_value(group, rules_dict)
                else:
                    return 0
            
    if fixed_groups_only:
        return 0
    else:
        return pages[group_length // 2]


def solve(input, fixed_groups_only=False):
    page_rules, page_groups = [x.splitlines() for x in input.split('\n\n')]

    rules_dict = {} # key is After, val is array of Befores
    for rule in page_rules:
        before, after = [int(x) for x in rule.split("|")]
        
        if after not in rules_dict:
            rules_dict[after] = []

        rules_dict[after].append(before)

    middle_page_sum = 0
    for group in page_groups:
        middle_page_sum += get_group_value(group, rules_dict, fixed_groups_only)

    return middle_page_sum


def part1(input):
    return solve(input)


def part2(input):
    return solve(input, True)
