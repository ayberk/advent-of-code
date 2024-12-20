from collections import deque

from aocd import get_data, submit

DAY = 20
DATA = get_data(day=DAY, year=2024).split()

walls = []
start = end = (0, 0)


for r in range(1, len(DATA)):
    for c in range(1, len(DATA[r])):
        match DATA[r][c]:
            case "#":
                walls.append((r, c))
            case "S":
                start = (r, c)
            case "E":
                end = (r, c)


def bfs(grid, start, end, cheat=None, actual=float("inf")):
    q = deque([(start, 0)])
    path = []
    visited = set()
    while q:
        node, distance = q.popleft()
        path.append(node)
        visited.add(node)
        if node == end:
            return distance, path
        if distance >= actual:
            continue
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            r, c = node[0] + dx, node[1] + dy
            if (r, c) in visited:
                continue
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[r]):
                continue
            if grid[r][c] == "#" and (r, c) != cheat:
                continue
            q.append(((r, c), distance + 1))

    return float("inf"), []


# very slow
def part1_native():
    grid = DATA[:]
    actual, _ = bfs(grid, start, end)
    return sum(actual - bfs(grid, start, end, wall, actual)[0] >= 100 for wall in walls)


# Stole this from reddit. Smart.
def solve(cheats):
    grid = DATA[:]
    _, path = bfs(grid, start, end)
    result = 0
    for i in range(len(path) - 1):
        for j in range(i + 1, len(path)):
            skipped = j - i
            first, second = path[i], path[j]
            dx = abs(first[0] - second[0])
            dy = abs(first[1] - second[1])
            manhattan = dx + dy

            if dx + dy <= cheats and skipped - manhattan >= 100:
                result += 1
    return result


submit(solve(2), part="a", day=DAY, year=2024)
submit(solve(20), part="b", day=DAY, year=2024)
