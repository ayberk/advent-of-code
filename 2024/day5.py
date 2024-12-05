from collections import defaultdict

from aocd import get_data, submit

DAY = 5
DATA = get_data(day=DAY, year=2024).split("\n")


def parse_input():
    ordering = defaultdict(list)
    line_no = 0
    pages = []
    while DATA[line_no]:
        left, right = DATA[line_no].split("|")
        ordering[int(left)].append(int(right))
        line_no += 1
    line_no += 1  # skip the empty line
    while line_no < len(DATA):
        pages.append([int(x) for x in DATA[line_no].split(",")])
        line_no += 1
    return (ordering, pages)


def get_invalid_pages():
    ordering, pages = parse_input()
    return [page for page in pages if not is_valid(page, ordering)[0]]


def is_valid(page, ordering):
    for i in range(1, len(page)):
        order = ordering[page[i]]
        # if any of these come before page[i] invalid
        for j, num in enumerate(page[:i]):
            if num in order:
                return False, i, j  # return the out-of-order indices
    return True, -1, -1


def part1():
    ordering, pages = parse_input()
    return sum(page[len(page) // 2] for page in pages if is_valid(page, ordering)[0])


def part2():
    ordering, pages = parse_input()
    invalid_pages = get_invalid_pages()
    new_valid_pages = []
    for page in invalid_pages:
        temp = page[:]
        res = is_valid(temp, ordering)
        # brute force until it's ordered'
        while not res[0]:
            a, b = res[1], res[2]
            temp[a], temp[b] = temp[b], temp[a]
            res = is_valid(temp, ordering)
            if res[0]:
                new_valid_pages.append(temp)
    return sum(page[len(page) // 2] for page in new_valid_pages)


submit(part1(), part="a", day=DAY, year=2024)
submit(part2(), part="b", day=DAY, year=2024)
