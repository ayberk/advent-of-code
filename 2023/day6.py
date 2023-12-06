
from aocd import get_data
from aocd import submit


DAY = 6
DATA = get_data(day=DAY, year=2023)


def counts(time, distance):
  result = 0
  for i in range(0, time):
    if (time - i) * i > distance:
      result += 1
  return result


def part1():
  times, distances = DATA.split("\n")
  times = [int(t) for t in times.split(":")[1].split()]
  distances = [int(t) for t in distances.split(":")[1].split()]
  # after N seconds, your speed is N m/s
  # you travel (time-N)*N meters
  # find all N such that (time-N)*N > distance
  result = 1
  for (time, distance) in zip(times, distances):
    result *= counts(time, distance)

  return result


def part2():
  times, distances = DATA.split("\n")
  times = [t for t in times.split(":")[1].split()]
  distances = [t for t in distances.split(":")[1].split()]
  time = int("".join(times))
  distance = int("".join(distances))
  return counts(time, distance)


submit(part1(), part="a", day=DAY, year=2023)
submit(part2(), part="b", day=DAY, year=2023)
