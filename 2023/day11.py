from aocd import get_data
from aocd import submit

DAY = 11
DATA = get_data(day=DAY, year=2023)


def find_expansions(grid):
  rows, columns = [], []
  for r in range(len(grid)):
    if '#' not in grid[r]:
      rows.append(r)
  for c in range(len(grid[0])):
    found = False
    for r in range(len(grid)):
      if grid[r][c] == '#':
        found = True
        break
    if not found:
      columns.append(c)
  rows.sort()
  columns.sort()
  return rows, columns

# used only for part 1, not really needed after part2
def expand(grid):
  rows, columns = find_expansions(grid)
  row_string = '.' * len(grid[0])
  for i, r in enumerate(rows):
    grid.insert(r + i, row_string)
  for r in range(len(grid)):
    grid[r] = list(grid[r])
  for i, c in enumerate(columns):
    for r in range(len(grid)):
      grid[r].insert(i + c, '.')
  return rows, columns


def find_galaxies(grid):
  galaxies = []
  for r in range(len(grid)):
    for c in range(len(grid[r])):
      if grid[r][c] == '#':
        galaxies.append((r, c))
  return galaxies


def part1():
  grid = DATA.split("\n")
  expand(grid)
  galaxies = find_galaxies(grid)
  result = 0
  for i in range(len(galaxies)):
    x, y = galaxies[i]
    for xx, yy in galaxies[i + 1:]:
      result += (abs(x - xx) + abs(y - yy))
  return result


def part2():
  grid = DATA.split("\n")
  rows, columns = find_expansions(grid)
  galaxies = find_galaxies(grid)
  result = 0
  for i in range(len(galaxies)):
    x, y = galaxies[i]
    for xx, yy in galaxies[i + 1:]:
      left, right = min(x, xx), max(x, xx)
      top, bottom = min(y, yy), max(y, yy)
      for r in rows:
        if left < r < right:
          result += 999999
      for c in columns:
        if top < c < bottom:
          result += 999999

      result += (abs(x - xx) + abs(y - yy))
  return result


submit(part1(), part="a", day=DAY, year=2023)
submit(part2(), part="b", day=DAY, year=2023)
