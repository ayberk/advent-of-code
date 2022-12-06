import strutils
import std/sets


proc marker(input: string, target: int): int =
    let limit = target-1
    var right = limit
    while right < len(input):
        let indexes = toHashSet(input[right-limit..right])
        if len(indexes) == target:
            return right+1
        right += 1


let lines = readFile("../input/day6.txt").splitLines()
for line in lines:
    echo marker(line, 4) # part1
    echo marker(line, 14) # part2
