from collections import Counter

from aocd import get_data, submit

DAY = 11
DATA = [int(x) for x in get_data(day=DAY, year=2024).split(" ")]


def blink(nums):
    result = []
    for num in nums:
        if num == 0:
            result.append(1)
        elif len(s := str(num)) % 2 == 0:
            mid = len(s) // 2
            result.extend([int(s[:mid]), int(s[mid:])])
        else:
            result.append(num * 2024)

    return result


def part1():
    result = DATA
    for _ in range(25):
        result = blink(result[:])
    return len(result)


def part2():
    stones = Counter(DATA)
    for _ in range(75):
        new_stones = Counter()
        for n, num_stone in stones.items():
            if n == 0:
                new_stones[1] += num_stone
            elif len(s := str(n)) % 2 == 0:
                mid = len(s) // 2
                new_stones[int(s[:mid])] += num_stone
                new_stones[int(s[mid:])] += num_stone
            else:
                new_stones[2024 * n] += num_stone
        stones = new_stones
    return sum(stones.values())


submit(part1(), part="a", day=DAY, year=2024)
submit(part2(), part="b", day=DAY, year=2024)
