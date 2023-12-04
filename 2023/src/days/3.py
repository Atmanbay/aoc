import regex as re
from functools import reduce
from operator import mul

def part1(input):
  sum = 0

  matches = []
  for line in input:
    matches.append({
      "numbers": list(re.finditer(r'\d+', line)),
      "symbols": list(re.finditer(r'([^\w\d.])', line))
    })

  def get_row_sum(row, offset, symbol_col):
    row_to_check = row + offset
    if (row_to_check < 0 or row_to_check >= len(matches)):
      return

    to_remove = []
    row_sum = 0
    for i, number_match in enumerate(matches[row_to_check]['numbers']):
      if offset == 0:
        if (symbol_col == (number_match.end() - 1) + 1 or symbol_col == number_match.start() - 1):
          row_sum += int(number_match.group())
          to_remove.append(i)
      else:
        if (symbol_col >= number_match.start() - 1 and symbol_col <= (number_match.end() - 1) + 1):
          row_sum += int(number_match.group())
          to_remove.append(i)
    
    matches[row_to_check]['numbers'] = [x for i, x in enumerate(matches[row_to_check]['numbers']) if not i in to_remove]
    return row_sum

  for i, row in enumerate(matches):
    for symbol_match in row['symbols']:
      sum += get_row_sum(i, -1, symbol_match.start())
      sum += get_row_sum(i, 0, symbol_match.start())
      sum += get_row_sum(i, 1, symbol_match.start())

  return sum

def part2(input):
  sum = 0

  matches = []
  for line in input:
    matches.append({
      "numbers": list(re.finditer(r'\d+', line)),
      "gears": list(re.finditer(r'\*', line))
    })

  def get_numbers_from_row(row, offset, symbol_col):
    row_to_check = row + offset
    to_remove = []
    numbers = []
    for i, number_match in enumerate(matches[row_to_check]['numbers']):
      if offset == 0:
        if (symbol_col == (number_match.end() - 1) + 1 or symbol_col == number_match.start() - 1):
          numbers.append(int(number_match.group()))
          to_remove.append(i)
      else:
        if (symbol_col >= number_match.start() - 1 and symbol_col <= (number_match.end() - 1) + 1):
          numbers.append(int(number_match.group()))
          to_remove.append(i)

    return [numbers, to_remove]

  for i, row in enumerate(matches):
    for gear_match in row['gears']:
      all_numbers = []
      all_to_remove = []
      for offset in range(-1, 2):
        if (i + offset < 0 or i + offset >= len(matches)):
          continue

        [numbers, to_remove] = get_numbers_from_row(i, offset, gear_match.start())
        all_numbers.extend(numbers)
        all_to_remove.append((i + offset, to_remove))

      if len(all_numbers) >= 2:
        gear_ratio = reduce(mul, all_numbers, 1)
        sum += gear_ratio
        for [row, to_remove] in all_to_remove:
          matches[row]['numbers'] = [x for i, x in enumerate(matches[row]['numbers']) if not i in to_remove]

  return sum