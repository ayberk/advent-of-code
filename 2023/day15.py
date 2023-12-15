from aocd import get_data
from aocd import submit
from collections import defaultdict
from collections import deque

DAY = 15
DATA = get_data(day=DAY, year=2023)

def hash(instr):
  result = 0
  for c in instr:
    result += ord(c)
    result *= 17
    result %= 256
  return result

def part1():
  return sum(hash(t) for t in DATA.split(","))

def part2():
  # boxes[i] is a deque
  boxes = defaultdict(deque)
  for token in DATA.split(","):
    if "=" in token:
      label, focal = token.split("=")
      h = hash(label)
      f = True
      for i, (a, _) in enumerate(boxes[h]):
        if a == label:
          boxes[h][i] = (a, focal)
          f = False
          break
      if f:
        boxes[h].append((label, focal))
    elif "-" in token:
      label = token[:-1]
      h = hash(label)
      idx = -1
      for i in range(len(boxes[h])):
        if boxes[h][i][0] == label:
          idx = i
          break
      if idx >= 0:
        del boxes[h][idx]
  total = 0
  for k, q in boxes.items():
    for i in range(len(q)):
      val = (int(k)+1) * (i+1) * int(q[i][1])
      total += val
  return total

submit(part1(), part="a", day=DAY, year=2023)
submit(part2(), part="b", day=DAY, year=2023)
