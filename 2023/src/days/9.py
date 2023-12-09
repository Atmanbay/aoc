from itertools import groupby

def all_equal(iterable):
  g = groupby(iterable)
  return next(g, True) and not next(g, False)

def part1(input):
  sum = 0

  for line in input:
    nums = [int(n) for n in line.split()]
    sum += nums[-1]
    while not all_equal(nums):
      temp_nums = []
      for i in range(1, len(nums)):
        temp_nums.append(nums[i] - nums[i - 1])

      sum += temp_nums[-1]
      nums = temp_nums

  return sum

def part2(input):
  sum = 0

  for line in input:
    print(line)
    nums = [int(n) for n in line.split()]
    sum += nums[0]
    counter = 1
    while not all_equal(nums):
      temp_nums = []
      for i in range(1, len(nums)):
        temp_nums.append(nums[i] - nums[i - 1])

      if (counter % 2 == 0):
        sum += temp_nums[0]
      else:
        sum -= temp_nums[0]
      
      counter += 1
      nums = temp_nums

  return sum