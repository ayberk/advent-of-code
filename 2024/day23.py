import random
from collections import defaultdict

from aocd import get_data, submit

DAY = 23
DATA = get_data(day=DAY, year=2024).split("\n")

graph = defaultdict(list)
for line in DATA:
    a, b = line.split("-")
    graph[a].append(b)
    graph[b].append(a)


def part1():
    res = set()
    for k, v in graph.items():
        if k.startswith("t") and len(v) >= 2:
            for i in range(len(v)):
                for j in range(i + 1, len(v)):
                    a, b = v[i], v[j]
                    if a in graph[b] and b in graph[a]:
                        res.add(tuple(sorted([a, b, k])))
    return len(res)


def part2():
    best, keys = [], list(graph.keys())
    for _ in range(100):
        random.shuffle(keys)
        clique = []
        for x in keys:
            include = True
            for y in clique:
                if x not in graph[y]:
                    include = False
            if include:
                clique.append(x)
        if not best or len(clique) > len(best):
            best = clique
    return ",".join(sorted(best))


submit(part1(), part="a", day=DAY, year=2024)
submit(part2(), part="b", day=DAY, year=2024)
