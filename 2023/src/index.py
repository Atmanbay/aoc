import importlib
import sys

def main():
  args = sys.argv[1:]
  if len(args) != 1 or args[0] == "--help":
    print("Run it like this: python src/index.py $DAY_NUMBER")
    return

  day = args[0]

  if day == "":
    print("Please supply a day")
    return

  days = importlib.import_module('days')
  day = getattr(days, day)

  print("Paste input below:")
  puzzle_input = []
  while True:
    line = input()
    if line:
      puzzle_input.append(line)
    else:
      break

  print(day.part1(puzzle_input))
  print(day.part2(puzzle_input))

main()