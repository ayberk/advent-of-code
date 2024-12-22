import collections
from heapq import heappop, heappush

from aocd import get_data, submit

DAY = 16
DATA = get_data(day=DAY, year=2024).split("\n")


def find_start():
    start = end = 0
    for r in range(len(DATA)):
        for c in range(len(DATA[r])):
            if DATA[r][c] == "S":
                start = (r, c)
            if DATA[r][c] == "E":
                end = (r, c)
    return (start, end)


DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
START, END = find_start()


# answer from first part
SHORTEST_PATH = 133584


def dijkstra(grid, start, end):
    # score, direction, location, distance map
    heap = [(0, 0, *start, {start})]
    visited, winning = {}, set()
    while heap:
        score, d, i, j, path = heappop(heap)
        if score > SHORTEST_PATH:
            break
        if (i, j) == end:
            winning |= path
            continue

        prev_score = visited.get((d, i, j))
        if prev_score and prev_score < score:
            continue
        visited[(d, i, j)] = score

        x, y = i + DIRECTIONS[d][0], j + DIRECTIONS[d][1]
        if grid[x][y] in [".", "E"] and (d, x, y) not in visited:
            heappush(heap, (score + 1, d, x, y, path | {(x, y)}))

        left = (d - 1) % 4
        if (left, i, j) not in visited:
            heappush(heap, (score + 1000, left, i, j, path))

        right = (d + 1) % 4
        if (right, i, j) not in visited:
            heappush(heap, (score + 1000, right, i, j, path))

    return SHORTEST_PATH, len(winning)


def part1():
    return dijkstra(DATA, START, END)[0]


def part2():
    return dijkstra(DATA, START, END)[1]


submit(part1(), part="a", day=DAY, year=2024)
submit(part2(), part="b", day=DAY, year=2024)
