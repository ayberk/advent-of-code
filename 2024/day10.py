from aocd import get_data, submit

DAY = 10
DATA = get_data(day=DAY, year=2024).split("\n")
DATA = [[int(x) for x in row if x.isdigit()] for row in DATA]

STARTS = []
for r in range(len(DATA)):
    for c in range(len(DATA[r])):
        if DATA[r][c] == 0:
            STARTS.append((r, c))


def dfs(r, c, prev, visited, found):
    if not (0 <= r < len(DATA)) or not (0 <= c < len(DATA[r])):
        return 0
    if prev + 1 != DATA[r][c] or (r, c) in visited:
        return 0
    if DATA[r][c] == 9:
        found.add((r, c))
        return 1
    result = 0
    visited.add((r, c))
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        result += dfs(r + dx, c + dy, DATA[r][c], visited, found)
    visited.remove((r, c))
    return result


def get_trails(start_row, start_col):
    return dfs(start_row, start_col, -1, set(), set())


# for part 1
def get_num(start_row, start_col):
    found = set()
    dfs(start_row, start_col, -1, set(), found)
    return len(found)


def part1():
    return sum(get_num(r, c) for (r, c) in STARTS)


def part2():
    return sum(get_trails(r, c) for (r, c) in STARTS)


submit(part1(), part="a", day=DAY, year=2024)
submit(part2(), part="b", day=DAY, year=2024)
