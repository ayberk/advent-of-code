from functools import cache

from aocd import get_data, submit

DAY = 19
DATA = get_data(day=DAY, year=2024).split("\n")


towels = [x.strip() for x in DATA[0].split(",")]
designs = [DATA[i].strip() for i in range(2, len(DATA))]


@cache
def is_possible(design):
    if not design:
        return 1
    res = 0
    for towel in towels:
        if design.startswith(towel):
            res += is_possible(design[len(towel) :])
    return res


def part1():
    return sum([1 if is_possible(d) else 0 for d in designs])


def part2():
    return sum(is_possible(d) for d in designs)


submit(part1(), part="a", day=DAY, year=2024)
submit(part2(), part="b", day=DAY, year=2024)
