import strutils


let lines  = readFile("../input/day1.txt").splitLines()
var current = 0
var sums: seq[int] = @[]
for line in lines:
    if line == "":
        sums.add(current)
        current = 0
    else:
        current += parseInt(line)

echo max(sums)
