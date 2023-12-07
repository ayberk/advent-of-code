from aocd import get_data
from aocd import submit
from dataclasses import dataclass
from collections import Counter


# Much better.
DAY = 7
DATA = get_data(day=DAY, year=2023)
RANKS = [c.strip() for c in "A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2".split(",")]

@dataclass
class Hand:
  cards: str
  bid: int
  rank: int = None
  replace_j: bool = False

  def get_rank(self):
    if self.rank: return self.rank

    counts = Counter(self.cards)
    if self.replace_j:
      count_j = counts['J']
      del counts['J']
      if count_j == 5:
        counts['A'] = 5  # any card works here, we just five of a kind
      else:
        counts[counts.most_common()[0][0]] += count_j  # consider J as the most common character

    match sorted(counts.values(), reverse=True):
      case [5]:
        self.rank = 6
      case [4, 1]:
        self.rank = 5
      case [3, 2]:
        self.rank = 4
      case [3, 1, 1]:
        self.rank = 3
      case [2, 2, 1]:
        self.rank = 2
      case [2, 1, 1, 1]:
        self.rank = 1
      case _:
        self.rank = 0
    return self.rank


  def __lt__(self, other):
    if self.get_rank() != other.get_rank(): return self.get_rank() < other.get_rank()
    # now we have to find the one with the earliest high card
    for i in range(len(self.cards)):
      a, b = RANKS.index(self.cards[i]), RANKS.index(other.cards[i])
      if self.replace_j and self.cards[i] == 'J': a = 20
      if other.replace_j and other.cards[i] == 'J': b = 20
      if a != b: return a > b  # not sure why removing this changes the result


def solve():
  hands, hands2 = [], []
  result, result2  = 0, 0
  for line in DATA.split("\n"):
    fields = line.split()
    hands.append(Hand(cards=fields[0], bid=int(fields[1])))
    hands2.append(Hand(cards=fields[0], bid=int(fields[1]), replace_j=True))
  for i, h in enumerate((zip(sorted(hands), sorted(hands2)))):
    result += (i + 1) * h[0].bid
    result2 += (i + 1) * h[1].bid
  return result,result2


r1, r2 = solve()
submit(r1, part="a", day=DAY, year=2023)
submit(r2, part="b", day=DAY, year=2023)
