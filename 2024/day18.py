from collections import deque

from aocd import get_data, submit

DAY = 18
DATA = get_data(day=DAY, year=2024).split("\n")
LEN = 71


def part1():
    blocked = set()
    i = 0
    while i < 1024:
        col, row = DATA[i].split(",")
        blocked.add((int(row), int(col)))
        i += 1
    return is_reachable(blocked)


def is_reachable(blocked):
    visited = {(0, 0)}
    q = deque([(0, 0, 0)])
    while q:
        r, c, cost = q.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            rr, cc = r + dx, c + dy
            if (rr, cc) in blocked or (rr, cc) in visited:
                continue
            if rr < 0 or rr >= LEN or cc < 0 or cc >= LEN:
                continue
            if (rr, cc) == (LEN - 1, LEN - 1):
                return cost + 1
            if (rr, cc) not in visited:
                q.append((rr, cc, cost + 1))
                visited.add((rr, cc))
    return -1


def part2():
    blocked = set()
    i = 0
    while i < len(DATA):
        col, row = DATA[i].split(",")
        blocked.add((int(row), int(col)))
        if is_reachable(blocked) < 0:
            return f"{col},{row}"
        i += 1
    return ""


submit(part1(), part="a", day=DAY, year=2024)
submit(part2(), part="b", day=DAY, year=2024)
