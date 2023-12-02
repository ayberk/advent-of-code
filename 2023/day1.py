from aocd import get_data
from aocd import submit

DIGITS = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def part1():
  numbers = []
  for line in get_data(day=1, year=2023).split('\n'):
    digits = [d for d in line if d.isdigit()]
    numbers.append(digits[0] + digits[-1])
  return sum(int(n) for n in numbers)


def part2():
  numbers = []
  for line in get_data(day=1, year=2023).split('\n'):
    line = line.strip().replace("eightwo", "82")
    line = line.replace("eighthree", "83")
    line = line.replace("oneight", "18")
    line = line.replace("fiveight", "58")
    line = line.replace("nineeight", "98")
    line = line.replace("threeight", "38")
    line = line.replace("twone", "21")
    line = line.replace("zerone", "01")
    line = line.replace("sevenine", "79")
    for k, v in DIGITS.items():
      line = line.replace(k, v)
    digits = [d for d in line if d.isdigit()]
    numbers.append(digits[0] + digits[-1])
  return sum(int(n) for n in numbers)


submit(part1(), part="a", day=1, year=2023)
submit(part2(), part="b", day=1, year=2023)
