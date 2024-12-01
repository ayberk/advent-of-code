from aocd import get_data
from aocd import submit
from collections import deque

DAY=21
DATA = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
..........."""
DATA = get_data(day=DAY, year=2023)

def part1():
  grid = DATA.split("\n")
  start = (0,0)
  for i in range(len(grid)):
    if 'S' in grid[i]:
      start = (i, grid[i].index('S'))
      break

  step = 0
  q = deque([start])
  while q and step < 64:
    cnt = len(q)
    while cnt > 0:
      r, c = q.popleft()
      for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x, y = r+dx, c+dy
        if 0 <= x < len(grid) and 0 <= y < len(grid[x]) and grid[x][y] != "#":
          if (x, y) not in q:
            q.append((x, y))
      cnt -= 1
    step += 1

  return len(q)

def part2():
  pass

print(part1())
#submit(part1(), part="a", day=DAY, year=2023)
#submit(part2(), part="b", day=DAY, year=2023)
