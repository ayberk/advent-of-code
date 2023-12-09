from aocd import get_data
from aocd import submit

DAY = 9
DATA = get_data(day=DAY, year=2023)

def process_row(nums):
  last_cols = []
  while not all(num == 0 for num in nums):
    new_rows = []
    last_cols.append(nums[-1])
    for a, b in zip(nums, nums[1:]):
      new_rows.append(b-a)
    nums = new_rows
  return sum(last_cols)

def part1():
  result = 0
  for row in DATA.split("\n"):
    nums = [int(v) for v in row.split()]
    result += process_row(nums)
  return result


def process_row2(nums):
  first_cols = []
  while not all(num == 0 for num in nums):
    new_rows = []
    first_cols.append(nums[0])
    for a, b in zip(nums, nums[1:]):
      new_rows.append(b - a)
    nums = new_rows
  for r in range(len(first_cols)-1, -1, -1):
    first_cols[r-1] = first_cols[r-1] - first_cols[r]
  return first_cols[0]


def part2():
  result = 0
  for row in DATA.split("\n"):
    nums = [int(v) for v in row.split()]
    result += process_row2(nums)
  return result


submit(part1(), part="a", day=DAY, year=2023)
submit(part2(), part="b", day=DAY, year=2023)
