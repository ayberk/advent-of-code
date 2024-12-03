from aocd import get_data, submit

DAY = 2
DATA = get_data(day=DAY, year=2024)

LEVELS = []
for level in DATA.split("\n"):
    l = [int(e) for e in level.split(" ")]
    LEVELS.append(l)


def is_safe(level):
    increasing = level[1] > level[0]
    for prev, next in zip(level, level[1:]):
        if not (1 <= abs(prev - next) <= 3):
            return False
        if increasing and next < prev:
            return False
        if (not increasing) and next > prev:
            return False
    return True


def is_safe_with_removal(level):
    for deleted in range(len(level)):
        new_list = level[:deleted] + level[deleted + 1 :]
        if is_safe(new_list):
            return True
    return False


def part1():
    return sum(is_safe(l) for l in LEVELS)


def part2():
    return sum(is_safe(l) or is_safe_with_removal(l) for l in LEVELS)


submit(part1(), part="a", day=DAY, year=2024)
submit(part2(), part="b", day=DAY, year=2024)
