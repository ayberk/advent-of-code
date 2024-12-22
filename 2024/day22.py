from collections import Counter

from aocd import get_data, submit

DAY = 22
DATA = get_data(day=DAY, year=2024).split("\n")

LEN = 2000
WINDOW_LEN = 4


def next_number(number):
    number = number ^ (number * 64)
    number = number % 16777216
    number = number ^ (number // 32)
    number = number % 16777216
    number = number ^ (number * 2048)
    return number % 16777216


def part1():
    s = 0
    for l in DATA:
        initial = int(l)
        for _ in range(LEN):
            initial = next_number(initial)
        s += initial
    return s


def part2():
    prices, diffs = [], []
    for l in DATA:
        initial = int(l)
        p, d = [], []
        for _ in range(LEN):
            p.append(initial % 10)
            initial = next_number(initial)
        prices.append(p)
        for a, b in zip(p, p[1:]):
            d.append(b - a)
        diffs.append(d)
    sold = Counter()
    for idx, change in enumerate(diffs):
        seen = set()
        for end in range(WINDOW_LEN - 1, len(change)):
            window = tuple(change[end - 4 - WINDOW_LEN : end + 1])
            if window not in seen:
                sold[window] += prices[idx][end + 1]
                seen.add(window)

    return max(sold.values())


submit(part1(), part="a", day=DAY, year=2024)
submit(part2(), part="b", day=DAY, year=2024)
