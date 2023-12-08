import regex as re
from math import lcm
import itertools

def part1(input):
  directions = input[0]

  all_input = "\n".join(input)
  node_matches = re.findall(r'(\w{3})\s=\s\((\w{3}),\s(\w{3})\)', all_input)
  nodes = {}
  for node_match in node_matches:
    nodes[node_match[0]] = {
      "L": node_match[1],
      "R": node_match[2]
    }

  node = "AAA"
  steps = 0
  for direction in itertools.cycle(directions):
    steps += 1
    if direction == "L":
      node = nodes[node]["L"]
    else:
      node = nodes[node]["R"]

    if node == "ZZZ":
      return steps

  return steps

def part2(input):
  directions = input[0]

  all_input = "\n".join(input)
  node_matches = re.findall(r'(\w{3})\s=\s\((\w{3}),\s(\w{3})\)', all_input)
  nodes = {}
  for node_match in node_matches:
    nodes[node_match[0]] = {
      "L": node_match[1],
      "R": node_match[2]
    }

  def find_steps(node):
    steps = 0
    for direction in itertools.cycle(directions):
      steps += 1
      if direction == "L":
        node = nodes[node]["L"]
      else:
        node = nodes[node]["R"]

      if node.endswith('Z'):
        return steps

    return steps

  starting_nodes = [n for n in nodes if n.endswith('A')]
  steps = []
  for node in starting_nodes:
    steps.append(find_steps(node))
  return lcm(*steps)