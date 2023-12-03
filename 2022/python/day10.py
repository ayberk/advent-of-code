from collections import deque
from collections import namedtuple

Operation = namedtuple("Operation", ["op", "execution_time", "delta"])


class Machine(object):
    def __init__(self):
        self.X = 1
        self.execution = 1
        self.queue = deque()
        self.executing = None
        self.timeline = dict()

    def queue_op(self, op):
        if op == "noop":
            self.queue.append(Operation("noop", 1, 0))
        elif "addx" in op:
            value = int(op.split()[-1])
            self.queue.append(Operation("addx", 2, value))

    def start_execution(self):
        while self.queue:
            next_op = self.queue.popleft()
            for _ in range(next_op.execution_time):
                self.timeline[self.execution] = self.X
                self.execution += 1
            self.X += next_op.delta
        self.timeline[self.execution] = self.X

    def print_queue(self):
        for op in self.queue:
            print(op)


def part1():
    m = Machine()
    with open("input/day10.txt") as f:
        for line in f:
            m.queue_op(line.strip())
    m.start_execution()
    result = 0
    for i in range(20, 221, 40):
        result += i * m.timeline[i]
    print(result)


part1()
