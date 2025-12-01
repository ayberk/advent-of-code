import logging

from aocd import get_data, submit

DAY = 1
DATA = get_data(day=1)

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

lines = DATA.split("\n")
for line in lines:
    logger.info(line)


def part1():
    pass


def part2():
    pass


submit(part1(), part="a", day=DAY)
submit(part2(), part="b", day=DAY)
