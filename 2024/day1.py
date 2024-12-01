from collections import Counter

from aocd import get_data, submit

DAY = 1
DATA = get_data(day=1)

lines = [l for l in DATA.split("\n")]
left, right = [], []
for line in lines:
    l, r = line.split("   ")
    left.append(l)
    right.append(r)


def part1():
    left.sort()
    right.sort()
    return sum(abs(int(ll) - int(rr)) for (ll, rr) in zip(left, right))


def part2():
    counts = Counter(right)
    return sum(int(e) * counts[e] for e in left)


submit(part1(), part="a", day=DAY)
submit(part2(), part="b", day=DAY)
