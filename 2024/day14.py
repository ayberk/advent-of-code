import re
from collections import defaultdict
from dataclasses import dataclass
from functools import reduce

from aocd import get_data, submit

DAY = 14
DATA = get_data(day=DAY, year=2024)

ROWS = 103
COLS = 101


@dataclass
class Robot:
    velocity: tuple[int, int]
    position: list[int]

    def move(self, seconds):
        self.position[0] += seconds * self.velocity[0]
        self.position[1] += seconds * self.velocity[1]
        self.position[0] %= ROWS
        self.position[1] %= COLS

    @staticmethod
    def from_list(values):
        return Robot((values[3], values[2]), [values[1], values[0]])


def part1():
    counts = defaultdict(int)
    for line in DATA.split("\n"):
        values = [int(s) for s in re.findall(r"-?\d+", line)]
        robot = Robot.from_list(values)
        robot.move(100)
        x, y = robot.position
        if x == ROWS // 2 or y == COLS // 2:
            continue
        a, b = x < ROWS // 2, y < COLS // 2
        counts[(a, b)] += 1
    return reduce((lambda x, y: x * y), counts.values())


def print_robots(robots):
    grid = [["."] * COLS for _ in range(ROWS)]
    for robot in robots:
        x, y = robot.position
        grid[x][y] = "#"
    # work smarter, not harder
    should_print = any("##########" in "".join(row) for row in grid)
    if should_print:
        for row in grid:
            print("".join(row))
    return should_print


def part2():
    robots = []
    for line in DATA.split("\n"):
        values = [int(s) for s in re.findall(r"-?\d+", line)]
        robots.append(Robot.from_list(values))
    cnt = 0
    while not print_robots(robots):
        for robot in robots:
            robot.move(1)
        cnt += 1
    return cnt


submit(part1(), part="a", day=DAY, year=2024)
submit(part2(), part="b", day=DAY, year=2024)
