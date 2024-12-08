from collections import defaultdict

from aocd import get_data, submit

DAY = 8
DATA = get_data(day=DAY, year=2024)
DATA = DATA.split("\n")


def get_antennas():
    antennas = defaultdict(list)
    for r, row in enumerate(DATA):
        for i, c in enumerate(row):
            if c != ".":
                antennas[c].append((r, i))
    return antennas


def get_antinodes(a, b, part1):
    n, m = len(DATA), len(DATA[0])
    dx, dy = a[0] - b[0], a[1] - b[1]
    antinodes = set()

    def get_locations(x, y, dx, dy):
        antinodes = set()
        while n > x >= 0 and m > y >= 0:
            antinodes.add((x, y))
            if part1:
                return antinodes
            x -= dx
            y -= dy
        return antinodes

    x, y = a[0] - dx, a[1] - dy
    antinodes.update(get_locations(x, y, dx, dy))
    x, y = b[0] - dx, b[1] - dy
    antinodes.update(get_locations(x, y, dx, dy))
    x, y = a[0] + dx, a[1] + dy
    antinodes.update(get_locations(x, y, -dx, -dy))
    x, y = b[0] + dx, b[1] + dy
    antinodes.update(get_locations(x, y, -dx, -dy))

    if part1:
        antinodes.remove(a)
        antinodes.remove(b)
    return antinodes


def part1():
    antinodes = set()
    for antenna in get_antennas().values():
        for i, a in enumerate(antenna):
            for j in antenna[i + 1 :]:
                for v in get_antinodes(a, j, part1=True):
                    antinodes.add(v)
    return len(antinodes)


def part2():
    antinodes = set()
    for antenna in get_antennas().values():
        for i, a in enumerate(antenna):
            for j in antenna[i + 1 :]:
                for v in get_antinodes(a, j, part1=False):
                    antinodes.add(v)
    return len(antinodes)


submit(part1(), part="a", day=DAY, year=2024)
submit(part2(), part="b", day=DAY, year=2024)
