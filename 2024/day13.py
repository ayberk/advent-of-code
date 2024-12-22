from aocd import get_data, submit

from functools import cache

import re

DAY = 13
DATA = get_data(day=DAY, year=2024)
DATA = DATA.split("\n")


def calculate(A, B, P):
    minimum = float("inf")

    @cache
    def helper(X, Y, total):
        nonlocal minimum
        if X < 0 or Y < 0:
            return
        if (X, Y) == B:
            minimum = min(minimum, total + 1)
            return
        if (X, Y) == A:
            minimum = min(minimum, total + 3)
            return

        helper(X - A[0], Y - A[1], total + 3)
        helper(X - B[0], Y - B[1], total + 1)

    helper(P[0], P[1], 0)
    return minimum


def calculate2(A, B, P):
    @cache
    def helper(X, Y):
        print(X, Y)
        if X < 0 or Y < 0:
            return (-1, False)
        if (X, Y) == B:
            return (1, True)
        if (X, Y) == A:
            return (3, True)

        res = (-1, False)
        a = helper(X - A[0], Y - A[1])
        if a[1]:
            res = (a[0] + 1, True)
        b = helper(X - B[0], Y - B[1])
        if b[1] and (b[0] + 3 <= res[0]):
            res = (b[0] + 3, True)
        return res

    return helper(P[0], P[1])


def part1():
    res = 0
    for i in range(0, len(DATA), 4):
        A = [int(s) for s in re.findall(r"\d+", DATA[i])]
        B = [int(s) for s in re.findall(r"\d+", DATA[i + 1])]
        P = [int(s) for s in re.findall(r"\d+", DATA[i + 2])]
        c = calculate((A[0], A[1]), (B[0], B[1]), (P[0], P[1]))
        if c < float("inf"):
            res += c
    return res


def part2():
    res = 0
    tolerance = 0.0001
    for i in range(0, len(DATA), 4):
        ax, ay = [int(s) for s in re.findall(r"\d+", DATA[i])]
        bx, by = [int(s) for s in re.findall(r"\d+", DATA[i + 1])]
        x, y = [10000000000000 + int(s) for s in re.findall(r"\d+", DATA[i + 2])]
        a = (bx * y - by * x) / (bx * ay - by * ax)
        b = (x - ax * a) / bx
        if abs(a - round(a)) < tolerance and abs(b - round(b)) < tolerance:
            res += 3 * a + b
    return int(res)


submit(part1(), part="a", day=DAY, year=2024)
submit(part2(), part="b", day=DAY, year=2024)
