import regex as re

def part1(input):
  converters = {}
  matches = re.finditer(r'(?P<source_category>\w+)-to-(?P<destination_category>\w+)\smap:\n(?P<mappings>(((\w+)(\s?)){3})+)', "\n".join(input))

  for match in matches:
    source_category = match.group("source_category")
    mappings = [{
      "source": int(m[1]),
      "destination": int(m[0]),
      "count": int(m[2]),
    } for m in (n.split() for n in match.group("mappings").split("\n") if len(n) > 0)]

    converters[source_category] = []

    for mapping in mappings:
      converters[source_category].append(mapping)

  def convert_position(pos, converter):
    for mapping in converter:
      if pos >= mapping["source"] and pos < mapping["source"] + mapping["count"]:
        return pos - mapping["source"] + mapping["destination"]
      
    return pos

  locations = []
  seeds = input[0].replace("seeds: ", "").split()
  for seed in seeds:
    pos = int(seed)
    for category, converter in converters.items():
      pos = convert_position(pos, converter)

    locations.append(pos)

  return min(locations)

def part2(input):
  converters = []
  matches = re.finditer(r'(\w+)-to-(\w+)\smap:\n(?P<mappings>(((\w+)(\s?)){3})+)', "\n".join(input))

  for match in matches:
    mappings = [{
      "source": int(m[1]),
      "destination": int(m[0]),
      "count": int(m[2]),
    } for m in (n.split() for n in match.group("mappings").split("\n") if len(n) > 0)]

    converters.insert(0, mappings)

  seed_mappings = input[0].replace("seeds: ", "").split()
  seed_ranges = []
  for i in range(0, len(seed_mappings), 2):
    seed_ranges.append({
      "start": int(seed_mappings[i]),
      "length": int(seed_mappings[i + 1])
    })

  def convert_position(pos, converter):
    for mapping in converter:
      if pos >= mapping["destination"] and pos < mapping["destination"] + mapping["count"]:
        return pos - mapping["destination"] + mapping["source"]
      
    return pos

  location = 0
  while True:
    print(f'Checking location {location}')
    pos = location
    for converter in converters:
      pos = convert_position(pos, converter)

    for seed_range in seed_ranges:
      if pos >= seed_range["start"] and pos < seed_range["start"] + seed_range["length"]:
        return location

    location += 1