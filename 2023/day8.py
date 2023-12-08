from aocd import get_data
from aocd import submit
from multiprocessing import Process, Queue
from math import lcm


DAY = 8
DATA = get_data(day=DAY, year=2023)


def parse(lines):
  directions, starting_nodes = lines[0], []
  lefts, rights = dict(), dict()
  for line in lines[2:]:
    a, b = line.split("=")
    src = a.strip()
    if src.endswith('A'): starting_nodes.append(src)
    left = b.split(",")[0].strip().strip("(")
    right = b.split(",")[1].strip().strip(")")
    lefts[src], rights[src] = left, right
  return directions, lefts, rights, starting_nodes

def get_steps(src, lefts, rights, directions, predicate, q=None):
  steps = 0
  while not predicate(src):
    idx = steps % len(directions)
    if directions[idx] == 'L': src = lefts[src]
    else: src = rights[src]
    steps += 1
  if q: q.put(steps)
  return steps

def part1():
  directions, lefts, rights, _ = parse(DATA.split("\n"))
  return get_steps('AAA', lefts, rights, directions, lambda x: x == 'ZZZ')

# stupid python doesn't allow anon functions into Process for some reason
def wrapped_pred(x):
    return x.endswith('Z')

def part2(q):
  directions, lefts, rights, starting_nodes = parse(DATA.split("\n"))
  processes = []
  for starting_node in starting_nodes:
    p = Process(target=get_steps, args=(starting_node, lefts, rights, directions, wrapped_pred, q))
    processes.append(p)
    p.start()
  return processes


if __name__ == '__main__':
  submit(part1(), part="a", day=DAY, year=2023)
  q = Queue()
  processes = part2(q)
  steps = []
  for proc in processes:
    steps.append(q.get())
    proc.join()
  submit(lcm(*steps), part="b", day=DAY, year=2023)
