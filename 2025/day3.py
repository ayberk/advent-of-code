import logging

from aocd import get_data, get_puzzle, submit

DAY = 3
DATA = get_data(day=DAY)
EXAMPLE = get_puzzle().examples[0]
LINES = DATA.split("\n")

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def part1():
    total = 0
    for jolts in LINES:
        current = 0
        for i, c in enumerate(jolts):
            for k in jolts[i + 1 :]:
                current = max(current, int(c + k))
        total += current
    return total


def part2():
    pass


submit(part1(), part="a", day=DAY)
# submit(part2(), part="b", day=DAY)
