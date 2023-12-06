import regex as re
import math

def get_winning_combos(time, distance):
    ways_to_beat = 0
    middle = math.ceil(time / 2)
    for time_held in range(middle, time):
      if (time_held * (time - time_held) > distance):
        ways_to_beat += 1
      else:
        break

    if time % 2 == 0:
      return (ways_to_beat * 2) - 1
    else:
      return ways_to_beat * 2

def part1(input):
  answer = 1

  [times_str, distances_str] = re.findall(r'Time:\s+(.*?)\nDistance:\s+(.*?)$', "\n".join(input))[0]
  times = times_str.split()
  distances = distances_str.split()

  for i in range(0, len(times)):
    time = int(times[i])
    distance = int(distances[i])
    answer *= get_winning_combos(time, distance)

  return answer

def part2(input):
  [times_str, distances_str] = re.findall(r'Time:\s+(.*?)\nDistance:\s+(.*?)$', "\n".join(input))[0]
  time = int("".join(times_str.split()))
  distance = int("".join(distances_str.split()))

  return get_winning_combos(time, distance)