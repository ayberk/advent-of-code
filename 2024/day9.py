from aocd import get_data, submit
from dataclasses import dataclass
from collections import deque

DAY = 9
DATA = get_data(day=DAY, year=2024)
# DATA = "2333133121414131402"


@dataclass(frozen=True)
class Interval:
    start: int
    length: int
    assigned_id: int


def calculate_checksum(blocks):
    result = 0
    idx = 0
    while idx < len(blocks):
        if blocks[idx] != ".":
            result += blocks[idx] * idx
        idx += 1
    return result


def build_blocks2():
    id = 0
    blocks = []
    current_idx = 0
    data = DATA if len(DATA) % 2 == 0 else DATA + "0"
    idx = 0
    full = deque()
    empty = deque()
    while idx < len(data) - 1:
        full_len, empty_len = int(data[idx]), int(data[idx + 1])
        full.append(Interval(current_idx, full_len, id))
        for _ in range(full_len):
            blocks.append(id)
            current_idx += 1
        empty.append(Interval(current_idx, empty_len, -1))
        for _ in range(empty_len):
            blocks.append(".")
            current_idx += 1
        idx += 2
        id += 1
    return blocks, empty, full


def build_blocks():
    id = 0
    blocks = []
    current_idx = 0
    data = DATA if len(DATA) % 2 == 0 else DATA + "0"
    idx = 0
    while idx < len(data) - 1:
        for _ in range(int(data[idx])):
            blocks.append(id)
            current_idx += 1
        for _ in range(int(data[idx + 1])):
            blocks.append(".")
            current_idx += 1
        idx += 2
        id += 1
    return blocks


def part1():
    blocks = build_blocks()
    to_write, to_read = 0, len(blocks) - 1
    while to_write < to_read:
        while to_write < to_read and blocks[to_write] != ".":
            to_write += 1
        while to_write < to_read and blocks[to_read] == ".":
            to_read -= 1
        blocks[to_write] = blocks[to_read]
        blocks[to_read] = "."
        to_write += 1
    return calculate_checksum(blocks)


def part2():
    blocks, empty, full = build_blocks2()
    while True:
        change_made = False
        full_idx = len(full) - 1
        while 0 <= full_idx < len(full):
            empty_idx = 0
            # print(full[full_idx])
            while empty_idx < len(empty) and empty[empty_idx].length < full[full_idx].length:
                empty_idx += 1
            if empty_idx < len(empty):
                e = empty[empty_idx]
                t = full[full_idx]
                # print("filling empty", empty[empty_idx], empty)
                for i in range(e.start, e.start + t.length):
                    blocks[i] = t.assigned_id
                for i in range(t.start, t.start + t.length):
                    blocks[i] = "."
                change_made = True
                del empty[empty_idx]
                del full[full_idx]
                if t.length != e.length:
                    n = Interval(e.start + t.length, e.length - t.length, -1)
                    empty.appendleft(n)
                    srt = list(empty)
                    srt.sort(key=lambda i: (i.start, i.length))
                    empty = deque(srt)
                    # print("adding new empty", n, empty)
            else:
                full_idx -= 1
        if not change_made:
            break

    # print(blocks)
    return calculate_checksum(blocks)


print(part2())
submit(part1(), part="a", day=DAY, year=2024)
submit(part2(), part="b", day=DAY, year=2024)
