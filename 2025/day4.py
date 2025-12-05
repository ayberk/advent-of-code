import logging

from aocd import get_data, get_puzzle, submit

DAY = 4
DATA = get_data(day=DAY)
EXAMPLE = get_puzzle().examples[0]
LINES = DATA.split("\n")

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, 1), (0, -1)]


def count_removed():
    can_reach = set()
    for r in range(len(LINES)):
        for c in range(len(LINES[r])):
            if LINES[r][c] != "@":
                continue
            neighbors = 0
            for dx, dy in DIRECTIONS:
                x, y = r + dx, c + dy
                if 0 <= x < len(LINES) and 0 <= y < len(LINES[x]) and LINES[x][y] == "@":
                    neighbors += 1
            if neighbors < 4:
                can_reach.add((r, c))

    return can_reach


def part1():
    can_reach = set()
    for r in range(len(LINES)):
        for c in range(len(LINES[r])):
            if LINES[r][c] != "@":
                continue
            neighbors = 0
            for dx, dy in DIRECTIONS:
                x, y = r + dx, c + dy
                if 0 <= x < len(LINES) and 0 <= y < len(LINES[x]) and LINES[x][y] == "@":
                    neighbors += 1
            if neighbors < 4:
                can_reach.add((r, c))

    return len(can_reach)


def part2():
    for i in range(len(LINES)):
        LINES[i] = list(LINES[i])
    total = 0
    while True:
        can_reach = count_removed()
        if not can_reach:
            return total
        total += len(can_reach)
        for r, c in can_reach:
            LINES[r][c] = "."
    return total


submit(part1(), part="a", day=DAY)
submit(part2(), part="b", day=DAY)
