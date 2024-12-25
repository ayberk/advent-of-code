from aocd import get_data, submit

DAY = 15
DATA = get_data(day=DAY, year=2024)


def move(grid, robot, d):
    i, j = robot
    match d:
        case "<":
            k = j - 1
            while grid[i][k] == "O":
                k -= 1
            if grid[i][k] == ".":
                grid[i][k], grid[i][j - 1] = grid[i][j - 1], grid[i][k]
                robot = (i, j - 1)
        case ">":
            k = j + 1
            while grid[i][k] == "O":
                k += 1
            if grid[i][k] == ".":
                grid[i][k], grid[i][j + 1] = grid[i][j + 1], grid[i][k]
                robot = (i, j + 1)
        case "^":
            k = i - 1
            while grid[k][j] == "O":
                k -= 1
            if grid[k][j] == ".":
                grid[k][j], grid[i - 1][j] = grid[i - 1][j], grid[k][j]
                robot = (i - 1, j)
        case "v":
            k = i + 1
            while grid[k][j] == "O":
                k += 1
            if grid[k][j] == ".":
                grid[k][j], grid[i + 1][j] = grid[i + 1][j], grid[k][j]
                robot = (i + 1, j)

    return robot


def part1():
    grid, directions = DATA.split("\n\n")
    grid = [list(r) for r in grid.split("\n")]
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == "@":
                robot = (r, c)
                grid[r][c] = "."

    for d in directions[:]:
        robot = move(grid, robot, d)

    total = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == "O":
                total += 100 * r + c

    return total


def part2():
    pass


# submit(part1(), part="a", day=DAY, year=2024)
# submit(part2(), part="b", day=DAY, year=2024)
