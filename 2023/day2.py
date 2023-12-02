from aocd import get_data
from aocd import submit


def get_counts(counts):
  # [r, g, b]
  res = [0, 0, 0,]
  num, color = counts.strip().split()
  match color.lower():
    case 'red':
      res[0] = int(num)
    case 'green':
      res[1] = int(num)
    case 'blue':
      res[2] = int(num)
  return res


def part1():
  id = 0
  max_values = [12, 13, 14]
  possible = []
  for line in get_data(day=2, year=2023).split('\n'):
    id += 1
    sets = line.split(':')[1]
    games = sets.split(';')
    valid = True
    for game in games:
      for cubes in game.split(','):
        counts = get_counts(cubes)
        for actual, max in zip(counts, max_values):
          if actual > max:
            valid = False
      if not valid:
        break
    if valid:
      possible.append(id)
  return sum(int(p) for p in possible)


def part2():
  id = 0
  powers = []
  for line in get_data(day=2, year=2023).split('\n'):
    id += 1
    sets = line.split(':')[1]
    games = sets.split(';')
    r = g = b = 0
    for game in games:
      for cubes in game.split(','):
        counts = get_counts(cubes)
        r = max(r, counts[0])
        g = max(g, counts[1])
        b = max(b, counts[2])
    powers.append(r * g * b)
  return sum(int(p) for p in powers)


submit(part1(), part="a", day=2, year=2023)
submit(part2(), part="b", day=2, year=2023)
