from aocd import get_data, submit

DAY = 7
DATA = get_data(day=DAY, year=2024).split("\n")


def dfs(operands, operations, target):
    def do_dfs(current_num, index):
        if current_num == target:
            return True
        if current_num > target or index >= len(operands):
            return False

        for op in operations:
            n = int(operands[index])
            if op == "*" and do_dfs(current_num * n, index + 1):
                return True
            if op == "+" and do_dfs(current_num + n, index + 1):
                return True
            if op == "||" and do_dfs(current_num * (10 ** len(operands[index])) + n, index + 1):
                return True

        return False

    return do_dfs(int(operands[0]), 1)


def parse_input():
    lines = []
    for line in DATA:
        target, operands = line.split(":")
        operands = [x for x in operands.split(" ") if x.isdigit()]
        lines.append((int(target), operands))
    return lines


def part1():
    result = 0
    for line in parse_input():
        target, operands = line
        if dfs(operands, ["+", "*"], target):
            result += target
    return result


def part2():
    result = 0
    for line in parse_input():
        target, operands = line
        if dfs(operands, ["||", "+", "*"], target):
            result += target
    return result


submit(part1(), part="a", day=DAY, year=2024)
submit(part2(), part="b", day=DAY, year=2024)
