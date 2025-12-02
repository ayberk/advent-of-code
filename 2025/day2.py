import logging
import textwrap

from aocd import get_data, get_puzzle, submit

DAY = 2
DATA = get_data(day=DAY)
EXAMPLE = get_puzzle().examples[0]
LINES = DATA.split("\n")

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def part1():
    ids = DATA.split(",")
    total = 0
    for r in ids:
        left, right = r.split("-")
        start = int(left)
        l = len(str(start))
        if l % 2 != 0:
            start = 10**l
        for i in range(start, int(right) + 1):
            s = str(i)
            a, b = s[: len(s) // 2], s[len(s) // 2 :]
            if a == b:
                total += i
    return total


def part2():
    ids = DATA.split(",")
    total = 0
    for r in ids:
        left, right = r.split("-")
        start = int(left)
        if start < 10:
            start = 11
        for i in range(start, int(right) + 1):
            for l in range(1, len(str(i)) // 2 + 1):
                parts = textwrap.wrap(str(i), l)
                if len(set(parts)) == 1:
                    total += i
                    break
    return total


submit(part1(), part="a", day=DAY)
submit(part2(), part="b", day=DAY)
