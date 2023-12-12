from aocd import get_data
from aocd import submit
from functools import cache


DAY = 12
DATA = get_data(day=DAY, year=2023)


def is_valid(row, nums):
  counts = []
  for token in row.split("."): # all lines have .
    if "#" in token:
      counts.append(len(token))
  return counts == nums

# brute force for part1
def count_arrangements(row, nums):

  total = sum(nums)
  arrangements = set()

  def helper(current):
    if len(current) == len(row):
      arrangements.add("".join(current))
      return

    if current.count('#') > total:
      return

    steps = len(current)
    if row[steps] != "?":
      current.append(row[steps])
      helper(current[:])
      return

    current.append("#")
    helper(current[:])
    current[-1] = "."
    helper(current[:])
    current.pop()

  helper([])

  return sum(is_valid(v, nums) for v in arrangements)

def part1():
  res = 0
  for line in DATA.split("\n"):
    row, nums = line.split()
    nums = [int(v) for v in nums.split(",")]
    res += count_arrangements2(row + 'X', nums)  # extra char is necessary :(
  return res


# DP(ugh) for part2
def count_arrangements2(row, nums):

  @cache
  def helper(current, running_count, finished):
    if current == len(row):
      return len(nums) == finished

    c = row[current]
    current += 1
    if c == '#':
      return helper(current, running_count + 1, finished)

    if c == '.':
      if finished < len(nums) and nums[finished] == running_count:
        return helper(current, 0, finished + 1)
      else:
        return 0 if running_count != 0 else helper(current, 0, finished)

    if finished == len(nums):
      return 0 if running_count != 0 else helper(current, 0, finished)

    # ? case
    with_dot, run_finished = 0, running_count == nums[finished]
    if run_finished or running_count == 0:
      with_dot = helper(current, 0, finished + run_finished)
    with_hash = helper(current, running_count + 1, finished)
    return with_hash + with_dot

  return helper(0, 0, 0)


def part2():
  res = 0
  for line in DATA.split("\n"):
    row, nums = line.split()
    nums = [int(v) for v in nums.split(",")] * 5
    row = '?'.join([row] * 5)
    res += count_arrangements2(row + 'X', nums)  # extra char is necessary :(
  return res


submit(part1(), part="a", day=DAY, year=2023)
submit(part2(), part="b", day=DAY, year=2023)
