from aocd import get_data
from aocd import submit
from dataclasses import dataclass


DAY = 5
DATA = get_data(day=DAY, year=2023)


@dataclass
class Interval:
  source: int
  dest: int
  length: int


class Mapping:
  def __init__(self, lines):
    self.intervals = []
    # lines is in the form dest, source, length
    for line in lines:
      dest, src, length = line.split()
      interval = Interval(int(src), int(dest), int(length))
      self.intervals.append(interval)

  def get_value(self, num):
    for interval in self.intervals:
      if interval.source <= num < interval.source + interval.length:
        return interval.dest + (num - interval.source)
    return num

  def print_mapping(self):
    print(len(self.intervals))
    for interval in self.intervals:
      print(interval)


def get_mappings(all_lines):
  mappings_in_order = []
  initial_seeds = [int(v) for v in all_lines[0].split(":")[1].split()]
  i = 1
  while i < len(all_lines):
    line = all_lines[i]
    lines = []
    if ":" in line:
      i += 1
      while i < len(all_lines) and all_lines[i]:
        line = all_lines[i]
        lines.append(line)
        i += 1
      if lines:
        mappings_in_order.append(Mapping(lines))
    i += 1
  return initial_seeds, mappings_in_order


def part1():
  all_lines = DATA.split('\n')
  initial_seeds, mappings_in_order = get_mappings(all_lines)

  lowest = float('inf')
  for seed in initial_seeds:
    for mapping in mappings_in_order:
      seed = mapping.get_value(seed)
    lowest = min(lowest, seed)
  return lowest


def part2():
  initial_seeds = []
  all_lines = DATA.split('\n')
  initial_seeds, mappings_in_order = get_mappings(all_lines)
  lowest = float('inf')
  i = 0
  for i in range(0, len(initial_seeds) - 1, 2):
    seed, rng = initial_seeds[i], initial_seeds[i + 1]
    for a in range(seed, rng + seed):
      for mapping in mappings_in_order:
        a = mapping.get_value(a)
      if a < lowest:
        print("found minimum ", a, " with seed ", seed)
      lowest = min(lowest, a)
  return lowest


print(part2())

# submit(part1(), part="a", day=DAY, year=2023)
# submit(part2(), part="b", day=DAY, year=2023)
