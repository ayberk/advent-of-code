from aocd import get_data, submit

DAY = 7
DATA = get_data(day=DAY, year=2024).split("\n")


def generate_operations(num_operations, operands):
    result = []

    def dfs(remaining, current):
        if remaining == 0:
            result.append(current[:])
            return
        for op in operands:
            current.append(op)
            dfs(remaining - 1, current)
            current.pop()

    dfs(num_operations, [])
    return result


def left_to_right(operands, operations_list, target):
    for operations in operations_list:
        total = int(operands[0])
        for i in range(1, len(operands)):
            if operations[i - 1] == "+":
                total += int(operands[i])
            elif operations[i - 1] == "*":
                total *= int(operands[i])
            else:
                total = int(str(total) + operands[i])
        if total == target:
            return True

    return False


def part1():
    result = 0
    for line in DATA:
        target, operands = line.split(":")
        operands = [x for x in operands.split(" ") if x.isdigit()]
        operations = generate_operations(len(operands) - 1, ["+", "*"])
        if left_to_right(operands, operations, int(target)):
            result += int(target)
    return result


def part2():
    result = 0
    for line in DATA:
        target, operands = line.split(":")
        operands = [x for x in operands.split(" ") if x.isdigit()]
        operations = generate_operations(len(operands) - 1, ["+", "*", "||"])
        if left_to_right(operands, operations, int(target)):
            result += int(target)
    return result


submit(part1(), part="a", day=DAY, year=2024)
submit(part2(), part="b", day=DAY, year=2024)
