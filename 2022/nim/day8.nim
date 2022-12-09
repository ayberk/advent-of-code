import strutils

proc isVisible(grid: seq[seq[int]], idx: (int, int)): bool =
    if idx[0] == 0 or idx[1] == 0: return true
    if idx[0] == (len(grid)-1) or idx[1] == (len(grid[idx[0]])-1): return true

    let value = grid[idx[0]][idx[1]]
    var row = idx[0]-1
    var col = idx[1]-1
    var visible = true
    while row >= 0:
        if grid[row][idx[1]] >= value:
            visible = false
            break
        row -= 1
    if visible: return true
    visible = true
    row = idx[0]+1
    while row < len(grid):
        if grid[row][idx[1]] >= value:
            visible = false
            break
        row += 1
    if visible: return true
    visible = true
    while col >= 0:
        if grid[idx[0]][col] >= value:
            visible = false
            break
        col -= 1
    if visible: return true
    visible = true
    col = idx[1]+1
    while col < len(grid[idx[0]]):
        if grid[idx[0]][col] >= value:
            visible = false
            break
        col += 1
    return visible

proc getViewScore(grid: seq[seq[int]], row: int, col: int): int =
    if row == 0 or col == 0 or row == len(grid)-1 or col == len(grid[
            row])-1: return 0

    var left = col-1
    var right = col+1
    var up = row-1
    var down = row+1

    while left > 0 and grid[row][left] < grid[row][col]:
        left -= 1
    while right < len(grid[row])-1 and grid[row][right] < grid[row][col]:
        right += 1
    while up > 0 and grid[up][col] < grid[row][col]:
        up -= 1
    while down < len(grid)-1 and grid[down][col] < grid[row][col]:
        down += 1

    return (col-left) * (right-col) * (row-up) * (down-row)

proc part1(grid: seq[seq[int]]): int =
    var r, c = 0
    while r < len(grid):
        while c < len(grid[r]):
            if (isVisible(grid, (r, c))):
                result += 1
            c+=1
        r+=1
        c = 0

proc part2(grid: seq[seq[int]]): int =
    var r, c = 0
    while r < len(grid):
        while c < len(grid[r]):
            if (isVisible(grid, (r, c))):
                let a = getViewScore(grid, r, c)
                if a > result:
                    result = a
                    echo r, " ", c, " ", result
            c+=1
        r+=1
        c = 0

var grid: seq[seq[int]]
let lines = readFile("../input/day8.txt").splitLines()
for line in lines:
    if line.isEmptyOrWhitespace(): continue
    grid.add(@[])
    for c in line:
        grid[^1].add(int(c) - int('0'))

echo part2(grid)
