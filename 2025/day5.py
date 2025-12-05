import logging
from collections import deque

from aocd import get_data, get_puzzle, submit

DAY = 5
DATA = get_data(day=DAY)
EXAMPLE = get_puzzle().examples[0].input_data
LINES = DATA.split("\n")

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class Interval:
    def __init__(self, left, right):
        if left > right:
            left, right = right, left
        self.left = left
        self.right = right

    def contains(self, number):
        return self.left <= number <= self.right

    def __str__(self):
        return f"[{self.left}, {self.right}]"

    def __repr__(self):
        return f"[{self.left}, {self.right}]"


def part1():
    intervals = []
    for i in range(len(LINES)):
        s = LINES[i]
        if s:
            left, right = s.split("-")
            intervals.append(Interval(int(left), int(right)))
        else:
            break

    total = 0
    for i in range(len(intervals) + 1, len(LINES)):
        for interval in intervals:
            if interval.contains(int(LINES[i])):
                total += 1
                break

    return total


def part2():
    intervals = []
    for i in range(len(LINES)):
        s = LINES[i]
        if s:
            left, right = s.split("-")
            intervals.append(Interval(int(left), int(right)))
        else:
            break

    # merge the intervals
    intervals.sort(key=lambda x: (x.left, x.right))
    intervals = deque(intervals)
    idx = 0
    while True:
        a, b = intervals[idx], intervals[idx + 1]
        if a.right >= b.left:
            del intervals[idx]
            del intervals[idx]
            aa = min(a.left, b.left)
            bb = max(a.right, b.right)
            intervals.insert(idx, Interval(aa, bb))
        else:
            idx += 1
        if idx >= len(intervals) - 1:
            break

    return sum(a.right - a.left + 1 for a in intervals)


submit(part1(), part="a", day=DAY)
submit(part2(), part="b", day=DAY)
