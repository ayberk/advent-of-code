import logging

from aocd import get_data, get_puzzle, submit

DAY = 1
DATA = get_data(day=1)
EXAMPLE = get_puzzle().examples[0]

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def part1():
    dial = 50
    result = 0
    lines = DATA.split("\n")
    for line in lines:
        coef = -1 if line.startswith("L") else 1
        dial += coef * int(line[1:])
        dial = dial % 100
        if dial == 0:
            result += 1
    return result


def part2():
    dial = 50
    result = 0
    lines = DATA.split("\n")
    for line in lines:
        start = dial
        coef = -1 if line.startswith("L") else 1
        amount = int(line[1:])
        end = dial + (coef * amount)
        if coef == 1:
            crossings = (end // 100) - (start // 100)
        else:
            crossings = ((start - 1) // 100) - ((end - 1) // 100)

        result += crossings
        dial = end
    return result


submit(part1(), part="a", day=DAY)
submit(part2(), part="b", day=DAY)
