from aocd import get_data, submit

from collections import defaultdict, deque

DAY = 21
DATA = """129A
176A
169A
805A
208A"""


KEYPAD = [k.split(",") for k in ["7,8,9", "4,5,6", "1,2,3", "-1,0,A"]]
MOVEPAD = [["-1", "^", "A"], ["<", "v", ">"]]


def shortest_path(grid, fr, to):
    q = deque([(fr, "")])
    visited = set()
    while q:
        node, path = q.popleft()
        if node == to:
            return list(path)

        visited.add(node)

        for dx, dy, ch in [(-1, 0, "^"), (1, 0, "v"), (0, 1, ">"), (0, -1, "<")]:
            r, c = node[0] + dx, node[1] + dy
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[r]):
                continue
            if (r, c) in visited:
                continue
            if grid[r][c] == "-1":
                continue
            q.append(((r, c), path + ch))

    return []


def reverse_char(c):
    match c:
        case ">":
            return "<"
        case "<":
            return ">"
        case "^":
            return "v"
        case "v":
            return "^"


def reverse_path(path):
    p = []
    for c in path:
        p.append(reverse_char(c))
    return p


def shortest_paths(grid):
    paths = {}
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            for rr in range(len(grid)):
                for cc in range(len(grid[rr])):
                    if (rr, cc) == (r, c) or grid[rr][cc] == "-1":
                        continue
                    if (r, c) not in paths:
                        paths[(r, c)] = {}
                    paths[(r, c)][(rr, cc)] = shortest_path(grid, (r, c), (rr, cc))

    return paths


def reverse_index(grid):
    idx = {}
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            idx[grid[r][c]] = (r, c)
    return idx


MOVEPAD_PATHS = shortest_paths(MOVEPAD)
KEYPAD_PATHS = shortest_paths(KEYPAD)


def decode_movepad(movement):
    path = []
    reverse_idx = reverse_index(MOVEPAD)
    position = reverse_idx["A"]
    for ch in movement:
        r, c = position
        if ch == "A":
            path.append(MOVEPAD[r][c])
        elif ch == "<":
            position = (r, c - 1)
        elif ch == ">":
            position = (r, c + 1)
        elif ch == "^":
            position = (r - 1, c)
        elif ch == "v":
            position = (r + 1, c)

    return "".join(path)


# this works
def from_code(code):
    path = []
    reverse_idx = reverse_index(KEYPAD)
    position = reverse_idx["A"]
    for c in code:
        target = reverse_idx[c]
        # might need if here like from_directions
        path.append(KEYPAD_PATHS[position][target])
        position = target
        path.append("A")
    return "".join(x for xs in path for x in xs)


def from_directions(direction):
    path = []
    reverse_idx = reverse_index(MOVEPAD)
    position = reverse_idx["A"]
    for c in direction:
        target = reverse_idx[c]
        if target != position:
            path.append(MOVEPAD_PATHS[position][target])
        position = target
        path.append("A")

    return "".join(x for xs in path for x in xs)


def part1():
    # this is the shortest
    first = decode_movepad("<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A")
    print(first)
    second = decode_movepad(first)
    print(second)

    print("---")

    # this is the one i generate
    first2 = decode_movepad(
        "v<A<AA>^>AvA^<Av>A^Av<<A>^>AvA^Av<<A>^>AAv<A>A^A<A>Av<A<A>^>AAA<Av>A^A"
    )
    print(first2)
    second2 = decode_movepad(first2)
    print(second2)

    # first = from_code("029A")
    # second = from_directions(first)
    # third = from_directions(second)
    # print(third)
    # print(second)
    # print(first)

    return (len(first), len(first2), len(second), len(second2))


def part2():
    pass


print(part1())
print(part2())
# submit(part1(), part="a", day=DAY, year=2024)
# submit(part2(), part="b", day=DAY, year=2024)
