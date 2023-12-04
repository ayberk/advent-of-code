from aocd import get_data
from aocd import submit
from collections import defaultdict

DAY = 4
DATA = get_data(day=DAY, year=2023)


def get_num_matches(line):
  numbers = line.split(":")[1]
  winning, owned = numbers.split("|")
  match = set(winning.split()) & set(owned.split())
  return len(match)


def part1():
  result = 0
  for line in DATA.split('\n'):
    match = get_num_matches(line)
    if match > 0:
      result += (2**(match - 1))
  return result


def part2():
  card_counts = defaultdict(int)
  current_card = 0
  for line in DATA.split('\n'):
    card_counts[current_card] += 1
    match = get_num_matches(line)
    for i in range(1, match + 1):
      card_counts[current_card + i] += card_counts[current_card]
    current_card += 1
  return sum(card_counts.values())


submit(part1(), part="a", day=DAY, year=2023)
submit(part2(), part="b", day=DAY, year=2023)
