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

  with open("in.txt", "r") as file:
    puzzle_input = file.read()

  print("")
  print(f'Part 1: {day.part1(puzzle_input)}')
  print(f'Part 2: {day.part2(puzzle_input)}')

main()