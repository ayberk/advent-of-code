from aocd import get_data, submit

DAY = 24
DATA = get_data(day=DAY, year=2024)


def do_operation(left, right, op):
    match op:
        case "XOR":
            return left != right
        case "OR":
            return left or right
        case "AND":
            return left and right
        case _:
            return False


class Gate:
    def __init__(self, name, value=None):
        self.name = name
        self.dependencies = []
        self.value = value

    def add_dependency(self, dependency):
        self.dependencies.append(dependency)

    def get_value(self, graph):
        if self.value is None:
            # they all have one :(
            left, op, right = self.dependencies[0]
            l = graph[left].get_value(graph)
            r = graph[right].get_value(graph)
            self.value = 1 if do_operation(l, r, op) else 0
        return self.value

    def __str__(self):
        return f"name:{self.name} -> deps:{self.dependencies} | val:{self.value}"


def process_input():
    gates = {}
    for line in DATA.split("\n"):
        if ":" in line:
            gate, value = line.split(":")[0].strip(), line.split(":")[1].strip()
            gates[gate] = Gate(gate, int(value))
        elif "->" in line:
            left, gate = line.split("->")[0].strip(), line.split("->")[1].strip()
            if gate not in gates:
                gates[gate] = Gate(gate)
            g = gates[gate]
            g.add_dependency(tuple(left.split(" ")))

    return gates


def part1():
    gates = process_input()
    result = []
    for k, v in gates.items():
        result.append((k, v.get_value(gates)))

    bits = [str(v[1]) for v in filter(lambda x: x[0].startswith("z"), sorted(result))]
    return int("".join(reversed(bits)), 2)


# I copy pasted this from this kind soul, because there's no way I do this myself.
# https://github.com/p3rki3/AoC2024/blob/main/Day24_solution.py
def part2():
    Lines = DATA.split("\n\n")
    Wires, Logic = dict(), []
    for line in Lines[0].split("\n"):
        wire, val = line.split(":")
        Wires[wire] = int(val.strip())
    for line in Lines[1].split("\n"):
        wire1, op, wire2, _, wire3 = line.split(" ")
        if wire1 > wire2:
            wire1, wire2 = wire2, wire1
        Logic.append([wire1, wire2, op, wire3, 1, 0])
    answer = []
    for logic in Logic:
        if logic[2] == "AND" and logic[0][0] == "x" and logic[1][0] == "y":  # Rule 1
            if logic[3][0] == "z" and logic[3] != "z00":
                answer.append(logic[3])
                logic[5] = 1
        elif (
            logic[2] == "XOR" and logic[0][0] != "x" and logic[1][0] != "y" and logic[3][0] != "z"
        ):  # Rule 2
            answer.append(logic[3])
            logic[5] = 1
        elif logic[3][0] == "z" and logic[2] != "XOR" and logic[3] != "z45":  # Rule 3
            answer.append(logic[3])
            logic[5] = 1
        if (
            logic[5] == 0
            and logic[2] == "AND"
            and logic[0][0] == "x"
            and logic[1][0] == "y"
            and logic[0] != "x00"
        ):  # Rule 4
            found = False
            for logic2 in Logic:
                if logic2[2] == "OR" and (logic[3] == logic2[0] or logic[3] == logic2[1]):
                    found = True
            if found is not True:
                answer.append(logic[3])
        elif (
            logic[5] == 0
            and logic[2] == "XOR"
            and logic[0][0] == "x"
            and logic[1][0] == "y"
            and logic[0] != "x00"
        ):  # Rule 5
            found = False
            for logic2 in Logic:
                if logic2[2] == "AND" and (logic[3] == logic2[0] or logic[3] == logic2[1]):
                    found = True
            if found is not True:
                answer.append(logic[3])
    return ",".join(sorted(answer))


submit(part1(), part="a", day=DAY, year=2024)
submit(part2(), part="b", day=DAY, year=2024)
