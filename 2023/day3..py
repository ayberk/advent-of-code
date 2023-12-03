from aocd import get_data
from aocd import submit
from collections import defaultdict

DATA = get_data(day=3, year=2023)

DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def check_adjacent(row, col, grid):
  for dx, dy in DIRECTIONS:
    r, c = row + dx, col + dy
    if 0 <= r < len(grid) and 0 <= c < len(grid[r]):
      v = grid[r][c]
      if not v.isdigit() and v != '.':
        return True

  return False


def part1():
  grid = []
  result = 0
  for line in DATA.split('\n'):
    grid.append(line)
  for row in range(len(grid)):
    col = 0
    while col < len(grid[row]):
      num = 0
      include = False
      while col < len(grid[row]) and grid[row][col].isdigit():
        if not include:
          include = check_adjacent(row, col, grid)
        num *= 10
        num += int(grid[row][col])
        col += 1
      if include:
        result += num
      col += 1
  return result


# Get all stars adjacent to this digit
def get_gears(row, col, grid):
  stars = []
  for dx, dy in DIRECTIONS:
    r, c = row + dx, col + dy
    if 0 <= r < len(grid) and 0 <= c < len(grid[r]):
      if grid[r][c] == '*':
        stars.append((r, c))

  return stars


def part2():
  grid = []
  result = 0
  gears = defaultdict(set)
  for line in DATA.split('\n'):
    grid.append(line)
  for row in range(len(grid)):
    col = 0
    while col < len(grid[row]):
      num = 0
      adjacent_stars = []
      while col < len(grid[row]) and grid[row][col].isdigit():
        adjacent_stars.extend(get_gears(row, col, grid))
        num *= 10
        num += int(grid[row][col])
        col += 1
      # adjacent_stars has all *'s adjacent to this number. now we're reversing the mapping.
      for (x, y) in adjacent_stars:
        gears[(x, y)].add(num)
      col += 1
  # gears holds adjacent numbers to each '*'. key is the (r, c) of the '*', and values is the set of
  # adjacent numbers.
  for nums in [list(v) for v in gears.values()]:
    if len(nums) == 2:
      result += (nums[0] * nums[1])
  return result


print(part1())
print(part2())
submit(part1(), part="a", day=3, year=2023)
submit(part2(), part="b", day=3, year=2023)
