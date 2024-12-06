from aocd import get_data, submit

DAY = 6
DATA = get_data(day=DAY, year=2024)
DATA = [list(s) for s in DATA.split("\n")]
SIZE = len(DATA) * len(DATA[0])


def find_start():
    for i in range(len(DATA)):
        for j in range(len(DATA[i])):
            if DATA[i][j] == "^":
                return (i, j)
    return (-1, -1)


def turn(direction):
    match direction:
        case (-1, 0):
            return (0, 1)
        case (0, 1):
            return (1, 0)
        case (1, 0):
            return (0, -1)
        case (0, -1):
            return (-1, 0)


def part1():
    visited = set()
    r, c = find_start()
    direction = (-1, 0)
    while True:
        if r < 0 or r >= len(DATA) or c < 0 or c >= len(DATA[0]):
            return visited
        if DATA[r][c] == "#":
            r, c = r - direction[0], c - direction[1]
            direction = turn(direction)
            continue
        visited.add((r, c))
        r, c = r + direction[0], c + direction[1]

    return visited


def is_cycle(r, c):
    direction = (-1, 0)
    steps_taken = 0
    while steps_taken < SIZE // 2:
        if r < 0 or r >= len(DATA) or c < 0 or c >= len(DATA[0]):
            return 0
        if DATA[r][c] == "#":
            r, c = r - direction[0], c - direction[1]
            direction = turn(direction)
            continue
        steps_taken += 1
        r, c = r + direction[0], c + direction[1]

    return 1


# this is slow
def part2():
    r, c = find_start()
    result = 0
    visited = part1()

    for j, row in enumerate(DATA):
        for i, cc in enumerate(row):
            if cc == "." and (j, i) in visited:
                row[i] = "#"
                result += is_cycle(r, c)
                row[i] = "."

    return result


submit(len(part1()), part="a", day=DAY, year=2024)
submit(part2(), part="b", day=DAY, year=2024)
