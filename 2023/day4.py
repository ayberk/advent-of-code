from aocd import get_data
from aocd import submit
from collections import defaultdict

DAY = 4
DATA = get_data(day=DAY, year=2023)
# DATA = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


def part1():
  result = 0
  for line in DATA.split('\n'):
      numbers = line.split(":")[1]
      winning, owned = numbers.split("|")
      match = set(winning.split()) & set(owned.split())
      if len(match) > 0:
        result += (2**(len(match) - 1))
  return result


def part2():
  card_counts = defaultdict(int)
  current = 0
  for line in DATA.split('\n'):
      card_counts[current] += 1
      numbers = line.split(":")[1]
      winning, owned = numbers.split("|")
      match = set(winning.split()) & set(owned.split())
      for i in range(current + 1, current + len(match) + 1):
        card_counts[i] += card_counts[current]
      current += 1
  return sum(v for v in card_counts.values())

submit(part1(), part="a", day=DAY, year=2023)
submit(part2(), part="b", day=DAY, year=2023)
