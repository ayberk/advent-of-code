from aocd import get_data, submit

DAY = 9
DATA = get_data(day=DAY, year=2024)


def calculate_checksum(blocks):
    result = 0
    idx = 0
    while idx < len(blocks):
        if blocks[idx] != ".":
            result += blocks[idx] * idx
        idx += 1
    return result


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
    blocks = build_blocks()
    back = len(blocks) - 1

    while back >= 0:
        curr = -1
        from_indexes = []
        to_indexes = []
        while back >= 0:
            item = blocks[back]
            if item != "." and (curr < 0 or curr == item):
                curr = item
                from_indexes.append(back)
                back -= 1
            elif item == "." and len(from_indexes) == 0:
                back -= 1
            else:
                break

        front = 0
        while front <= back:
            item = blocks[front]
            if item == ".":
                to_indexes.append(front)
                if len(to_indexes) == len(from_indexes):
                    for a, b in zip(from_indexes, to_indexes):
                        blocks[a], blocks[b] = blocks[b], blocks[a]
                    break
            else:
                to_indexes = []
            front += 1

    return calculate_checksum(blocks)


submit(part1(), part="a", day=DAY, year=2024)
submit(part2(), part="b", day=DAY, year=2024)
