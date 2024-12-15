from aocd import get_data,submit

from collections import deque, defaultdict

DAY=12
DATA = get_data(day=DAY, year=2024)
DATA = """EEEEE
EXXXX
EEEEE
EXXXX
EEEEE"""
DATA = DATA.split("\n")


def check_boundary(r, c):
    return 0 <= r < len(DATA) and 0 <= c < len(DATA[r])

def part1():
    visited = set()
    def bfs(r, c, t):
        perimeter = 0
        area = 0
        q = deque([(r, c)])
        while q:
            x, y = q.popleft()
            if (x, y) in visited:
                continue
            visited.add((x,y))
            area += 1
            perimeter += 4
            for dx,dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                rr, cc = x+dx, y+dy
                if check_boundary(rr, cc) and DATA[rr][cc] == t:
                    perimeter -= 1
                    q.append((rr, cc))
        return (area, perimeter)

    t = 0
    for r in range(len(DATA)):
        for c in range(len(DATA[r])):
            if (r, c) not in visited:
                x, y = bfs(r, c, DATA[r][c])
                t += (x*y)

    return t



def part2():
    visited = set()
    def bfs(r, c, t):
        rows = defaultdict(int)
        cols = defaultdict(int)
        area = 0
        q = deque([(r, c)])
        while q:
            x, y = q.popleft()
            if (x, y) in visited:
                continue
            visited.add((x,y))
            area += 1
            for dx,dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                rr, cc = x+dx, y+dy
                if check_boundary(rr, cc) and DATA[rr][cc] == t:
                    q.append((rr, cc))
                elif rr != x:
                    rows[(x, rr)] += 1
                elif cc != y:
                    cols[(y, cc)] += 1
        return (area, rows, cols)

    t = 0
    for r in range(len(DATA)):
        for c in range(len(DATA[r])):
            if (r, c) not in visited:
                x, y,z = bfs(r, c, DATA[r][c])
                print((r,c), y, z)
                t += (x * (sum(y.values()) + sum(z.values())))
    return t

print(part2())
# submit(part1(), part="a", day=DAY, year=2024)
# submit(part2(), part="b", day=DAY, year=2024)
