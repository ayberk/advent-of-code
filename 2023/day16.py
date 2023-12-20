from typing import List
from aocd import get_data
from aocd import submit

DAY = 16
DATA = get_data(day=DAY, year=2023)
DIRECTIONS = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}
visited = set()

def print_after(grid, energized):
  for r in range(len(grid)):
    for c in range(len(grid[r])):
      if (r, c) in energized: print("#", end="")
      else: print(".", end="")
    print()

def get_mirrored(direction, mirror) -> str:
  match (mirror, direction):
    case ('/', 'U'): return 'R'
    case ('/', 'D'): return 'L'
    case ('/', 'L'): return 'D'
    case ('/', 'R'): return 'U'
    case ('\\', 'U'): return 'L'
    case ('\\', 'D'): return 'R'
    case ('\\', 'L'): return 'U'
    case ('\\', 'R'): return 'D'

def get_split(direction, splitter) -> List[str]:
  if direction in {'U', 'D'} and splitter == "-":
    return ['L', 'R']
  elif direction in {'L', 'R'} and splitter == "|":
    return ['U', 'D']
  else:
    return [direction]

def move(r, c, direction) -> tuple:
  return (r + DIRECTIONS[direction][0], c + DIRECTIONS[direction][1])

def energize(grid, start, direction, energized):
  if (start,direction) in visited: return
  visited.add((start,direction))
  r, c = start
  while r < len(grid) and c < len(grid[r]) and c >= 0 and r >=0:
    char = grid[r][c]
    energized.add((r, c))
    if char in {'-', '|'}:
      for dir in get_split(direction, char):
        energize(grid, move(r, c, dir), dir, energized)
      return
    elif char in {"/", "\\"}:
      new_direction = get_mirrored(direction, char)
      energize(grid, move(r, c, new_direction), new_direction, energized)
      return
    r += DIRECTIONS[direction][0]
    c += DIRECTIONS[direction][1]

def part1(dbg = False):
  grid = DATA.split("\n")
  energized = set()
  energize(grid, (0,0), "R", energized)
  if dbg: print_after(grid, energized)
  return len(energized)

def part2():
  grid = DATA.split("\n")
  result = 0
  N, M = len(grid), len(grid[0])
  for r in range(len(grid)):
    energized = set()
    visited.clear()
    energize(grid, (r, 0), "R", energized)
    result = max(result, len(energized))
    energized = set()
    visited.clear()
    energize(grid, (r, M-1), "L", energized)
    result = max(result, len(energized))

  for c in range(len(grid[0])):
    energized = set()
    visited.clear()
    energize(grid, (0, c), "D", energized)
    result = max(result, len(energized))
    energized = set()
    visited.clear()
    energize(grid, (N-1, c), "U", energized)
    result = max(result, len(energized))

  return result

submit(part1(), part="a", day=DAY, year=2023)
submit(part2(), part="b", day=DAY, year=2023)
