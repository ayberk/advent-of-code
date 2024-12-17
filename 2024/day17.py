from aocd import submit

DAY = 17


class Computer:
    def get_combo_operand(self, operand):
        match operand:
            case 4:
                return self.a
            case 5:
                return self.b
            case 6:
                return self.c
            case _:
                return operand

    # totally didn't steal from reddit
    def matching_output(self, program, target):
        a = 0 if len(target) == 1 else 8 * self.matching_output(program, target[1:])

        while self.run_program(program, a) != target:
            a += 1
        return a

    def run_program(self, program, initial_a):
        outputs, ptr = [], 0
        self.a = initial_a
        while ptr < len(program):
            operand = program[ptr + 1]
            match program[ptr]:
                case 0:
                    self.a = self.a // (2 ** self.get_combo_operand(operand))
                case 1:
                    self.b = self.b ^ operand
                case 2:
                    self.b = self.get_combo_operand(operand) % 8
                case 3 if self.a != 0:
                    ptr = operand - 2
                case 4:
                    self.b = self.b ^ self.c
                case 5:
                    outputs.append(self.get_combo_operand(operand) % 8)
                case 6:
                    self.b = self.a // (2 ** self.get_combo_operand(operand))
                case 7:
                    self.c = self.a // (2 ** self.get_combo_operand(operand))
            ptr += 2
        return outputs


def part1():
    """Register A: 32916674
    Register B: 0
    Register C: 0

    Program: 2,4,1,1,7,5,0,3,1,4,4,0,5,5,3,0"""
    program = [2, 4, 1, 1, 7, 5, 0, 3, 1, 4, 4, 0, 5, 5, 3, 0]
    out = Computer().run_program(program, 32916674)
    return ",".join([str(x) for x in out])


def part2():
    program = [2, 4, 1, 1, 7, 5, 0, 3, 1, 4, 4, 0, 5, 5, 3, 0]
    return Computer().matching_output(program, program)


submit(part1(), part="a", day=DAY, year=2024)
submit(part2(), part="b", day=DAY, year=2024)
