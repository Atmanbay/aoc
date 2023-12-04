import regex as re

def part1(input):
  sum = 0

  for line in input:
    match = re.findall('\d', line)
    val = int(f'{match[0]}{match[-1]}')
    sum += val

  return sum

def part2(input):
  sum = 0

  converter = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
  }

  def convert(val):
    if val.isnumeric():
      return val
    else:
      return converter[val]

  for line in input:
    match = re.findall('\d|one|two|three|four|five|six|seven|eight|nine', line, overlapped=True)
    first_val = convert(match[0])
    last_val = convert(match[-1])
    val = int(f'{first_val}{last_val}')
    sum += val

  return sum