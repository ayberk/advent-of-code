from aocd import get_data
from aocd import submit

DAY = 14
DATA = get_data(day=DAY, year=2023)


def tilt(rocks):
  # tilts north and returns the load. redundant after part2 solution
  transposed = [list(x) for x in zip(*rocks)]
  total = 0
  for row in transposed:
    insert_idx = 0
    for i, c in enumerate(row):
      if c == 'O':
        total += len(row) - insert_idx
        insert_idx += 1
      elif c == '#':
        insert_idx = i + 1
  return total

def cycle(rocks):
  # I'm sure there's a better way, but alas I am too sleepy
  # actually I can just rotate and always tilt north. But again see above.

  # north
  for col in range(len(rocks[0])):
    idx = 0
    for row in range(len(rocks)):
      c = rocks[row][col]
      if c == 'O':
        rocks[idx][col] = 'O'
        if idx != row:
          rocks[row][col] = '.'
        idx += 1
      elif c == '#':
        idx = row + 1

  # west
  for row in range(len(rocks)):
    idx = 0
    for col in range(len(rocks[row])):
      c = rocks[row][col]
      if c == 'O':
        rocks[row][idx] = 'O'
        if idx != col:
          rocks[row][col] = '.'
        idx += 1
      elif c == '#':
        idx = col + 1

  # south
  for col in range(len(rocks[0])):
    idx = len(rocks) - 1
    for row in range(len(rocks) - 1, -1, -1):
      c = rocks[row][col]
      if c == 'O':
        rocks[idx][col] = 'O'
        if idx != row:
          rocks[row][col] = '.'
        idx -= 1
      elif c == '#':
        idx = row - 1

  # east
  for row in range(len(rocks)):
    idx = len(rocks[row]) - 1
    for col in range(len(rocks[row]) - 1, -1, -1):
      c = rocks[row][col]
      if c == 'O':
        rocks[row][idx] = 'O'
        if idx != col:
          rocks[row][col] = '.'
        idx -= 1
      elif c == '#':
        idx = col - 1


def part1():
  return tilt(DATA.split("\n"))

def part2():
  rocks = [list(r) for r in DATA.split("\n")]
  string_rocks = "\n".join(["".join(a) for a in rocks])
  seen = {string_rocks: 0}
  iteration = 0
  LIMIT = 1_000_000_000

  while iteration < LIMIT:
    iteration += 1
    cycle(rocks)
    string_rocks = "\n".join(["".join(a) for a in rocks])
    if string_rocks in seen:
      cycle_length = iteration - seen[string_rocks]
      iteration += (((LIMIT - iteration) // cycle_length) * cycle_length)
    seen[string_rocks] = iteration

  load = 0
  for col in range(len(rocks[0])):
    for i, row in enumerate(rocks):
      if row[col] == 'O':
        load += len(rocks) - i

  return load


submit(part1(), part="a", day=DAY, year=2023)
submit(part2(), part="b", day=DAY, year=2023)
