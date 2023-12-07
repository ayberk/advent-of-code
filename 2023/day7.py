from aocd import get_data
from aocd import submit
from dataclasses import dataclass
from collections import Counter


# This solution might actually end my career. I'm going to commit as is so I never forget.
DAY = 7
DATA = get_data(day=DAY, year=2023)

RANKS = [c.strip() for c in "A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2".split(",")]
RANKS2 = [c.strip() for c in "A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J".split(",")]


@dataclass
class Hand:
  cards: str
  bid: int

  def __lt__(self, other):
    this_counts = Counter(self.cards)
    other_counts = Counter(other.cards)
    this_most_common = this_counts.most_common(1)[0]
    other_most_common = other_counts.most_common(1)[0]
    print("Comparing ", self, other)
    print(this_counts, other_counts)
    del this_counts['J']
    del other_counts['J']
    if this_most_common[1] < other_most_common[1]:
      # general win condition
      print("general win a")
      return True
    if this_most_common[1] > other_most_common[1]:
      # general win condition
      print("general win b")
      return False
    if this_most_common[1] == other_most_common[1] == 3:
      # one has three of a kind, other doesn't
      if this_counts.most_common(2)[1][1] < other_counts.most_common(2)[1][1]:
        print("three of a kind a")
        return True
      if this_counts.most_common(2)[1][1] > other_counts.most_common(2)[1][1]:
        print("three of a kind b")
        return False
    if this_most_common[1] == other_most_common[1] == 2:
      # one has two pairs, other doesn't
      if this_counts.most_common(2)[1][1] < other_counts.most_common(2)[1][1]:
        print("two pairs a")
        return True
      if this_counts.most_common(2)[1][1] > other_counts.most_common(2)[1][1]:
        print("two pairs b")
        return False
    # now we have to find the one with the earliest high card
    for i in range(len(self.cards)):
      a, b = RANKS.index(self.cards[i]), RANKS.index(other.cards[i])
      if a != b:
        return a > b


      a, b = RANKS2.index(self.cards[i]), RANKS2.index(other.cards[i])
      if a != b:
        return a > b


def part1():
  hands = []
  for line in DATA.split("\n"):
    fields = line.split()
    hands.append(Hand(fields[0], int(fields[1])))
  hands.sort()
  total = 0
  for i, hand in enumerate(hands):
    total += (i + 1) * hand.bid
  return total




@dataclass
class Hand3:
  cards: str
  bid: int
  processed_cards: str = None

  def get_processed_cards(self):
    if self.processed_cards: return self.processed_cards
    self.processed_cards = list(self.cards)
    counts = Counter(self.cards)
    cnt = 0
    if 'J' in counts:
      cnt = counts['J']
      print(counts)
      if cnt == 5:
        return self.processed_cards
      del counts['J']
    for i, c in enumerate(self.processed_cards):
      if c == 'J':
        print(counts)
        self.processed_cards[i] = counts.most_common(1)[0][0]
    return self.processed_cards


  def __lt__(self, other):
    this_counts = Counter(self.get_processed_cards())
    other_counts = Counter(other.get_processed_cards())
    this_most_common = this_counts.most_common(1)[0]
    other_most_common = other_counts.most_common(1)[0]
    print("Comparing ", self, other)
    print(this_counts, other_counts)
    this_with_j = this_most_common[1] + this_counts['J']
    other_with_j = other_most_common[1] + other_counts['J']
    if other_with_j > 5:
      other_with_j -= other_counts['J']
    if this_with_j > 5:
      this_with_j -= this_counts['J']
    this_second = other_second = 0
    if len(this_counts.most_common(2)) > 1:
      this_second = this_counts.most_common(2)[1][1]
    if len(other_counts.most_common(2)) > 1:
      other_second = other_counts.most_common(2)[1][1]
    print(this_with_j, other_with_j)
    print('seconds', this_second, other_second)
    if this_with_j < other_with_j:
      # general win condition
      print("general win a")
      return True
    if this_with_j > other_with_j:
      # general win condition
      print("general win b")
      return False
    if this_with_j == other_with_j == 3:
      # one has three of a kind, other doesn't
      if this_second < other_second:
        print("three of a kind a")
        return True
      if this_second > other_second:
        print("three of a kind b")
        return False
    if this_with_j == other_with_j == 2:
      # one has two pairs, other doesn't
      if this_second < other_second:
        print("two pairs a")
        return True
      if this_second > other_second:
        print("two pairs b")
        return False
    # now we have to find the one with the earliest high card
    for i in range(len(self.cards)):
      a, b = RANKS2.index(self.cards[i]), RANKS2.index(other.cards[i])
      if a != b:
        return a > b


def part2():
  hands = []
  for line in DATA.split("\n"):
    fields = line.split()
    hands.append(Hand3(fields[0], int(fields[1])))
  hands.sort()
  total = 0
  for i, hand in enumerate(hands):
    total += (i + 1) * hand.bid
  for h in hands:
    print((h.cards, h.bid))
  return total



print(part2())
# a = Hand3('AAAAJ', 0)
# b = Hand3('JJJJJ', 0)
# print()
# # print(a < b)
# a = Hand3(cards='6QQQQ', bid=743)
# b = Hand3(cards='7JJKA', bid=40)
# print(a > b)
# a = Hand3(cards='66QQQ', bid=743)
# b = Hand3(cards='7JJKA', bid=40)
# print(a > b)
# a = Hand3(cards='JJJQQ', bid=743)
# b = Hand3(cards='7JJ77', bid=40)
# print(a < b)
# a = Hand3(cards='6QQQQ', bid=743)
# b = Hand3(cards='7JJKA', bid=40)
# print(a > b)

# b = Hand3('8888J', 0)
# a = Hand3('JJJJJ', 0)
# print(a < b)

# submit(part1(), part="a", day=DAY, year=2023)
# submit(part2(), part="b", day=DAY, year=2023)
