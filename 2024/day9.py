from aocd import get_data, submit
from dataclasses import dataclass
from collections import deque

DAY = 9
DATA = get_data(day=DAY, year=2024)
# DATA = "2333133121414131402"


@dataclass(frozen=True)
class Interval:
    start: int
    end: int
    assigned_id: int


def part1():
    id = 0
    blocks = []
    empty = deque()
    current_idx = 0
    data = DATA if len(DATA) % 2 == 0 else DATA + "0"
    idx = 0
    while idx < len(data) - 1:
        for _ in range(int(data[idx])):
            blocks.append(id)
            current_idx += 1
        for _ in range(int(data[idx + 1])):
            blocks.append(".")
            empty.append(current_idx)
            current_idx += 1
        idx += 2
        id += 1
    to_write, to_read = 0, len(blocks) - 1
    while to_write < to_read:
        while to_write < to_read and blocks[to_write] != ".":
            to_write += 1
        while to_write < to_read and blocks[to_read] == ".":
            to_read -= 1
        blocks[to_write] = blocks[to_read]
        blocks[to_read] = "."
        to_write += 1
    result = 0
    idx = 0
    while idx < len(blocks) and blocks[idx] != ".":
        result += blocks[idx] * idx
        idx += 1
    return result


def part2():
    pass


print(part2())
submit(part1(), part="a", day=DAY, year=2024)
# submit(part2(), part="b", day=DAY, year=2024)
