from aocd import get_data
from aocd import submit
from collections import defaultdict
from bisect import insort

DAY = 18
DIRECTIONS = {
  'U': (-1, 0),
  'D': (1, 0),
  'L': (0, -1),
  'R': (0, 1),
}
DATA = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""
DATA = get_data(day=DAY, year=2023)


def move(location, direction):
  return (location[0] + DIRECTIONS[direction][0], location[1] + DIRECTIONS[direction][1])


def rindex(lst, value):
    return len(lst) - lst[::-1].index(value) - 1


ROWS = 280
COLS = 490


def part1_2():
  rows, columns = defaultdict(list), defaultdict(list)

  grid = [['.'] * COLS for _ in range(ROWS)]
  r, c = 190, 288
  grid[r][c] = '#'
  rows[r].append(c)
  columns[c].append(r)
  for line in DATA.split("\n"):
    dir, cnt, _ = line.split()
    for _ in range(int(cnt)):
      r, c = move((r, c), dir)
      grid[r][c] = '#'
      rows[r].append(c)
      columns[c].append(r)
  total = 0
  for r, row in enumerate(grid):
    print("".join(row))
    if '#' in row:
      rows[r].sort()
      i = 0
      while i < len(rows[r])-1:
        l, rr = rows[r][i], rows[r][i+1]
        while l < rr:
          grid[r][l] = '#'
          l += 1
        i += 1
  print("-------------")
  for row in grid:
    print("".join(row))

  return total


def part1():
  visited, location = {(0, 0)}, (0, 0)
  for line in DATA.split("\n"):
    dir, cnt, _ = line.split()
    for _ in range(int(cnt)):
      visited.add(location)
      location = move(location, dir)

  rows, columns = defaultdict(list), defaultdict(list)

  for (r, c) in visited:
    rows[r].append(c)
    columns[c].append(r)

  for row, c in sorted(rows.items()):
    # print(row, l, r)
    c.sort()
    # print(row, c)
    i = 0
    while i < len(c) - 1:
      l, r = c[i], c[i + 1]
      while l <= r:
        visited.add((row, l))
        l += 1
      i += 2

  # print()
  # for col, r in sorted(columns.items()):
  #   u, d = min(r), max(r)
  #   # print(col, u, d)
  #   while u <= d:
  #     visited.add((u, col))
  #     u+=1

  return len(visited)


def part2():
  pass

# print(part1())
print(part1_2())
# submit(part1_2(), part="a", day=DAY, year=2023)
# submit(part2(), part="b", day=DAY, year=2023)
