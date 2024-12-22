from collections import deque

from aocd import get_data, submit

DAY = 12
DATA = get_data(day=DAY, year=2024)
DATA = DATA.split("\n")


def check_boundary(r, c):
    return 0 <= r < len(DATA) and 0 <= c < len(DATA[r])


def bfs(r, c, t):
    visited = set()
    perimeter = area = 0
    q = deque([(r, c)])
    while q:
        x, y = q.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        area += 1
        perimeter += 4
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            rr, cc = x + dx, y + dy
            if check_boundary(rr, cc) and DATA[rr][cc] == t:
                perimeter -= 1
                q.append((rr, cc))
    return (area, perimeter, visited)


def part1():
    visited = set()
    res = 0
    for r in range(len(DATA)):
        for c in range(len(DATA[r])):
            if (r, c) not in visited:
                area, perimeter, points = bfs(r, c, DATA[r][c])
                res += area * perimeter
                visited |= points
    return res


# thank you dear reddit person. no way i was going to implement this myself
def calc_edges(region):
    edges = 0
    for r, c in region:
        north_n = (r - 1, c)
        west_n = (r, c - 1)
        nw_n = (r - 1, c - 1)
        if north_n not in region:
            # Top is an edge. But is it a new edge?
            # it's the same edge if the spot west of plot is in_bounds
            # and the NW plot is not the same plant (or is out of bounds)
            same_edge = (west_n in region) and (nw_n not in region)
            if not same_edge:
                edges += 1

        south_n = (r + 1, c)
        sw_n = (r + 1, c - 1)
        if south_n not in region:
            # bottom is an edge
            same_edge = (west_n in region) and (sw_n not in region)
            if not same_edge:
                edges += 1

        if west_n not in region:
            # left is an edge
            same_edge = (north_n in region) and (nw_n not in region)
            if not same_edge:
                edges += 1

        east_n = (r, c + 1)
        ne_n = (r - 1, c + 1)
        if east_n not in region:
            same_edge = (north_n in region) and (ne_n not in region)
            if not same_edge:
                edges += 1
    return edges


def part2():
    res = 0
    visited = set()
    for r in range(len(DATA)):
        for c in range(len(DATA[r])):
            if (r, c) not in visited:
                area, perimeter, points = bfs(r, c, DATA[r][c])
                visited |= points
                res += area * calc_edges(points)
    return res


submit(part1(), part="a", day=DAY, year=2024)
submit(part2(), part="b", day=DAY, year=2024)
