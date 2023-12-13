from aocd import get_data
from aocd import submit

DAY = 13
DATA = get_data(day=DAY, year=2023)

def hamming_distance(s1, s2):
  return sum([a != b for a, b in zip(s1, s2)])

def reflection_point(grid, hamming_dist = 0):
  for i in range(1, len(grid)):
    left, right = grid[:i], grid[i:]
    length = min(len(left), len(right))
    left = left[len(left)-length:]
    right = right[:length]

    if hamming_distance("".join(left), "".join(right[::-1])) == hamming_dist:
      return i

  return -1

def solve(dist):
  grids = DATA.split("\n\n")
  total = 0
  for grid in grids:
    grid = grid.split("\n")
    row = reflection_point(grid, dist)
    if row > 0:
      total += 100 * row
    else:
      transposed = ["".join(a) for a in [list(x) for x in zip(*grid)]]
      total += reflection_point(transposed, dist)
  return total

submit(solve(0), part="a", day=DAY, year=2023)
submit(solve(1), part="b", day=DAY, year=2023)
