from aocd import get_data
from aocd import submit
import sys

sys.setrecursionlimit(10000)


DAY = 23
DATA = """#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#"""
DATA = get_data(day=DAY, year=2023)

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(grid, start, end):

  def helper(x, y, visited, curr_len):
    res = float('-inf')
    if (x, y) in visited:
      return res
    if not (0 <= x < len(grid)) or not (0 <= y < len(grid[0])):
      return res
    visited.add((x, y))
    if (x, y) == end:
      return curr_len
    c = grid[x][y]
    if c == '#':
      return res
    elif c == '>':
      res = helper(x, y + 1, visited, curr_len + 1)
    elif c == '<':
      res = helper(x, y - 1, visited, curr_len + 1)
    elif c == 'v':
      res = helper(x + 1, y, visited, curr_len + 1)
    elif c == '^':
      res = helper(x - 1, y, visited, curr_len + 1)
    else:
      for dx, dy in DIRECTIONS:
        if (x + dx, y + dy) not in visited and 0<= x < len(grid) and 0 <= y < len(grid[0]):
          res = max(res, helper(x + dx, y + dy, visited, curr_len + 1))
    visited.remove((x, y))
    return res

  return helper(start[0], start[1], set(), 0)


def part1():
  grid = [list(s) for s in DATA.split('\n')]
  start = (0, grid[0].index('.'))
  end = (len(grid) - 1, grid[-1].index('.'))
  return dfs(grid, start, end)


def part2():
  grid = DATA.split('\n')
  new_grid = []
  start = (0, grid[0].index('.'))
  end = (len(grid) - 1, grid[-1].index('.'))
  for row in grid:
    for c in ['<', '>', '^', 'v']:
      row = row.replace(c, '.')
    new_grid.append(row)
  new_grid = [list(s) for s in new_grid]
  return dfs(new_grid, start, end)


print(part2())

# submit(part1(), part="a", day=DAY, year=2023)
# submit(part2(), part="b", day=DAY, year=2023)
