from aocd import get_data
from aocd import submit

DAY = 9
DATA = get_data(day=DAY, year=2023)


# returns all elements in `col`th column in a list.
def process_row(nums, col):
  cols = []
  while not all(num == 0 for num in nums):
    new_rows = []
    cols.append(nums[col])
    for a, b in zip(nums, nums[1:]):
      new_rows.append(b-a)
    nums = new_rows
  return cols

def part1():
  result = 0
  for row in DATA.split("\n"):
    nums = [int(v) for v in row.split()]
    result += sum(process_row(nums, -1))
  return result

def part2():
  result = 0
  for row in DATA.split("\n"):
    nums = [int(v) for v in row.split()]
    first_cols = process_row(nums, 0)
    for r in range(len(first_cols) - 1, -1, -1):
      first_cols[r - 1] = first_cols[r - 1] - first_cols[r]
    result += first_cols[0]
  return result

submit(part1(), part="a", day=DAY, year=2023)
submit(part2(), part="b", day=DAY, year=2023)
