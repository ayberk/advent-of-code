from aocd import get_data
from aocd import submit

DAY = 10
DATA = get_data(day=DAY, year=2023)
PIPE_DIRECTION = {
    'F': {(1, 0), (0, 1)},
    'J': {(-1, 0), (0, -1)},
    'L': {(-1, 0), (0, 1)},
    '7': {(0, -1), (1, 0)},
    '-': {(0, 1), (0, -1)},
    '|': {(1, 0), (-1, 0)},
    'S': {(1, 0), (-1, 0)},
}


def get_start(grid):
  start = (0, 0)
  for r in range(len(grid)):
    grid[r] = list(grid[r]) # might as well
    if 'S' in grid[r]:
      start = (r, grid[r].index('S'))
  return start


def get_loop_nodes(grid):
  start = get_start(grid)
  visited = set()
  while start not in visited:
    visited.add(start)

    r, c = start
    for dx, dy in PIPE_DIRECTION[grid[r][c]]:
        rr, cc = r + dx, c + dy
        if (rr, cc) not in visited:
          start = (rr, cc)
          break
  return visited


def part1():
  grid = DATA.split("\n")
  return len(get_loop_nodes(grid)) // 2


def part2():
  grid = DATA.split("\n")
  start = get_start(grid)
  visited, result = get_loop_nodes(grid), 0
  grid[start[0]][start[1]] = '|' # absolute no shame
  parity_changers = ['|', 'F', '7']
  for r in range(len(grid)):
    parity = 0
    for c in range(len(grid[r])):
      if (r, c) not in visited:  # not part of the loop
        result += (parity % 2)
        continue
      if grid[r][c] in parity_changers:
        parity += 1

  return result


submit(part1(), part="a", day=DAY, year=2023)
submit(part2(), part="b", day=DAY, year=2023)
