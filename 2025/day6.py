import logging

from aocd import get_data, get_puzzle, submit

DAY = 6
DATA = get_data(day=DAY)
EXAMPLE = get_puzzle().examples[0].input_data
LINES = DATA.split("\n")

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def part1():
    matrix = [row.split() for row in LINES]

    operations = dict(enumerate(matrix[-1]))
    results = {i: 0 if op == "+" else 1 for i, op in enumerate(matrix[-1])}

    for row in matrix[: len(matrix) - 1]:
        for i, c in enumerate(row):
            if operations[i] == "+":
                results[i] += int(c)
            else:
                results[i] *= int(c)

    return sum(results.values())


def part2():
    pass


submit(part1(), part="a", day=DAY)
# submit(part2(), part="b", day=DAY)
