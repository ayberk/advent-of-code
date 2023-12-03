from aocd import get_data
from aocd import submit

DAY = 3
DATA = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

def check_adjacent(row, col, grid):
  for dx,dy in [(-1,-1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
    r, c = row + dx, col + dy
    if 0 <= r < len(grid) and 0 <= c < len(grid[r]):
      v = grid[r][c]
      if not v.isdigit() and v != '.':
        return True

  return False

def part1():
  DATA=get_data(day=3, year=2023)
  grid = []
  result = 0
  for line in DATA.split('\n'):
    grid.append(line)
  row = 0
  while row < len(grid):
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
      if include: result += num
      col += 1
    row += 1
  return result

def get_gears(row, col, grid):
  stars = []
  for dx,dy in [(-1,-1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
    r, c = row + dx, col + dy
    if 0 <= r < len(grid) and 0 <= c < len(grid[r]):
      if grid[r][c] == '*':
        stars.append((r, c))

  return stars

def part2():
  DATA=get_data(day=3, year=2023)
  grid = []
  result =0
  gears = {}
  for line in DATA.split('\n'):
    grid.append(line)
  row = 0
  while row < len(grid):
    col = 0
    while col < len(grid[row]):
      num = 0
      adjacent_stars = []
      while col < len(grid[row]) and grid[row][col].isdigit():
        for x in get_gears(row, col, grid): adjacent_stars.append(x)
        num *= 10
        num += int(grid[row][col])
        col += 1
      for (x, y) in adjacent_stars:
        if (x, y) not in gears: gears[(x,y)] = set()
        gears[(x, y)].add(num)
      col += 1
    row += 1
  for k, v in gears.items():
    if len(v) == 2:
      res = 1
      for vv in v:
        res *= vv
      result += res
  return result


submit(part1(), part="a", day=3, year=2023)
submit(part2(), part="b", day=3, year=2023)
