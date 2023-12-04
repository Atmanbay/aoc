import regex as re
import math

def part1(input):
  sum = 0
  
  for card in input:
    [_, winning_numbers_str, numbers_you_have_str] = re.findall(r'Card\s+(\d+):\s(.*)\s\|\s(.*)$', card)[0]
    winning_numbers = winning_numbers_str.split()
    numbers_you_have = numbers_you_have_str.split()

    intersection = [n for n in numbers_you_have if n in winning_numbers]
    if (len(intersection) > 0):
      sum += int(math.pow(2, len(intersection) - 1))

  return sum

def part2(input):
  sum = 0
  duplicate_counts = {}
  
  def handle_card(card_number, winning_numbers, numbers_you_have):
    intersection = [n for n in numbers_you_have if n in winning_numbers]
    for offset in range(1, len(intersection) + 1):
      won_card = int(card_number) + offset
      if won_card in duplicate_counts:
        duplicate_counts[won_card] += 1
      else:
        duplicate_counts[won_card] = 1

  for card in input:
    [card_number_str, winning_numbers_str, numbers_you_have_str] = re.findall(r'Card\s+(\d+):\s(.*)\s\|\s(.*)$', card)[0]

    card_number = int(card_number_str)
    winning_numbers = winning_numbers_str.split()
    numbers_you_have = numbers_you_have_str.split()

    handle_card(card_number, winning_numbers, numbers_you_have)
    if card_number in duplicate_counts:
      for i in range(0, duplicate_counts[card_number]):
        handle_card(card_number, winning_numbers, numbers_you_have)

    
  sum += len(input)
  for key, value in duplicate_counts.items():
    sum += value

  return sum