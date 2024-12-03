import re

from aocd import get_data, submit

DAY = 3
DATA = get_data(day=DAY, year=2024)


def get_total(operations):
    # no negative numbers
    mul = re.compile(r"mul\(\d+,\d+\)")
    numbers = re.compile(r"\d+")
    result = 0
    for operation in mul.finditer(operations):
        left, right = numbers.findall(operation.group())
        result += int(left) * int(right)
    return result


def part1():
    return get_total(DATA)


def part2():
    p = re.compile(r"(mul\(\d+,\d+\)|do\(\)|don't\(\))")
    all_operations, doing = [], True
    for nxt in p.finditer(DATA):
        match nxt.group():
            case "don't()":
                doing = False
            case "do()":
                doing = True
            case _ if doing:
                all_operations.append(nxt.group())
    return get_total("".join(all_operations))


submit(part1(), part="a", day=DAY, year=2024)
submit(part2(), part="b", day=DAY, year=2024)
