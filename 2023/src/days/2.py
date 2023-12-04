import regex as re

def part1(input):
  sum = 0
  
  bag_contents = {
    'red': 12,
    'green': 13,
    'blue': 14,
  }

  def is_game_valid(pull_results):
    for pull_result in pull_results.split(';'):
      results_by_color = re.findall('(\d+)\s(\w+)', pull_result)
      for [count, color] in results_by_color:
        if int(count) > bag_contents[color]:
          return False

    return True

  for game_result in input:
    [game, pull_results] = re.findall('Game\s(\d+):\s(.*?)$', game_result)[0]
    if (is_game_valid(pull_results)):
      sum += int(game)

  return sum

def part2(input):
  sum = 0

  def get_power(pull_results):
    max_values = {
      'red': 0,
      'green': 0,
      'blue': 0,
    }
    
    for pull_result in pull_results.split(';'):
      results_by_color = re.findall('(\d+)\s(\w+)', pull_result)
      for [count, color] in results_by_color:
        if int(count) > max_values[color]:
          max_values[color] = int(count)

    return max_values['red'] * max_values['green'] * max_values['blue']

  for game_result in input:
    [_, pull_results] = re.findall('Game\s(\d+):\s(.*?)$', game_result)[0]
    sum += get_power(pull_results)

  return sum