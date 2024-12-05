from aocd import get_data, submit
from collections import defaultdict

DAY = 5
DATA = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47""".split("\n")
DATA = get_data(day=DAY, year=2024).split("\n")


def parse_input():
    ordering = defaultdict(list)
    line_no = 0
    pages = []
    while DATA[line_no]:
        left, right = DATA[line_no].split("|")
        ordering[left].append(right)
        line_no += 1
    line_no += 1
    while line_no < len(DATA):
        pages.append(DATA[line_no].split(","))
        line_no += 1
    return (ordering, pages)


def get_invalid_pages():
    invalid = []
    ordering, pages = parse_input()
    for page in pages:
        valid = True
        for i in range(1, len(page)):
            order = ordering[page[i]]
            # if any of these come before page[i] invalid
            for num in page[:i]:
                if num in order:
                    valid = False
                    break
            if not valid:
                break
        if not valid:
            invalid.append(page)
    return invalid


def is_valid(page, ordering):
    for i in range(1, len(page)):
        order = ordering[page[i]]
        # if any of these come before page[i] invalid
        for j, num in enumerate(page[:i]):
            if num in order:
                return False, i, j
    return True, -1, -1


def part1():
    ordering, pages = parse_input()
    total = 0
    for page in pages:
        valid = True
        for i in range(1, len(page)):
            order = ordering[page[i]]
            # if any of these come before page[i] invalid
            for num in page[:i]:
                if num in order:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            total += int(page[len(page) // 2])
    return total


def part2():
    ordering, pages = parse_input()
    invalid_pages = get_invalid_pages()
    new_valid_pages = []
    for page in invalid_pages:
        temp = page[:]
        res = is_valid(temp, ordering)
        while not res[0]:
            a, b = res[1], res[2]
            temp[a], temp[b] = temp[b], temp[a]
            res = is_valid(temp, ordering)
            if res[0]:
                new_valid_pages.append(temp)
    return sum(int(page[len(page) // 2]) for page in new_valid_pages)


submit(part1(), part="a", day=DAY, year=2024)
submit(part2(), part="b", day=DAY, year=2024)
