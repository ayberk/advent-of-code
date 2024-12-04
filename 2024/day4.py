from aocd import get_data, submit

DAY = 4
DATA = get_data(day=DAY, year=2024).split("\n")

DIAGONAL_DIRECTIONS = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
DIRECTIONS = [(-1, 0), (0, -1), (0, 1), (1, 0), *DIAGONAL_DIRECTIONS]
TARGET = "XMAS"


def check_boundary(row, col):
    return 0 <= row < len(DATA) and 0 <= col < len(DATA[row])


def solve():
    def dfs(row, col, direction, current_str):
        if current_str == TARGET:
            return 1
        if not check_boundary(row, col) or len(current_str) >= len(TARGET):
            return 0
        if DATA[row][col] != TARGET[len(current_str) - 1]:
            return 0

        if direction:
            next_row, next_col = row + direction[0], col + direction[1]
            if not check_boundary(next_row, next_col):
                return 0
            return dfs(
                next_row,
                next_col,
                direction,
                current_str + DATA[next_row][next_col],
            )

        total = 0
        for dx, dy in DIRECTIONS:
            next_row, next_col = row + dx, col + dy
            if check_boundary(next_row, next_col):
                total += dfs(
                    next_row,
                    next_col,
                    (dx, dy),
                    current_str + DATA[next_row][next_col],
                )
        return total

    result = 0
    for i in range(len(DATA)):
        for j in range(len(DATA[i])):
            if DATA[i][j] == TARGET[0]:
                result += dfs(i, j, None, "X")
    return result


def part1():
    result = 0
    for row in range(len(DATA)):
        for col in range(len(DATA[row])):
            if DATA[row][col] == "X":
                for dx, dy in DIRECTIONS:
                    r, c = row, col
                    length = 1
                    for letter in TARGET[1:]:
                        r += dx
                        c += dy
                        if check_boundary(r, c) and DATA[r][c] == letter:
                            length += 1
                            continue
                        break
                    if length == len(TARGET):
                        result += 1
    return result


def part2():
    result = 0
    for row in range(len(DATA)):
        for col in range(len(DATA[row])):
            if DATA[row][col] == "A":
                for dx1, dy1 in DIAGONAL_DIRECTIONS:
                    r_m1, c_m1 = row + dx1, col + dy1
                    if check_boundary(r_m1, c_m1) and DATA[r_m1][c_m1] == "M":
                        r_s1, c_s1 = row - dx1, col - dy1
                        dx2, dy2 = dy1, -dx1
                        r_m2, c_m2 = row + dx2, col + dy2
                        r_s2, c_s2 = row - dx2, col - dy2

                        s1 = check_boundary(r_s1, c_s1) and DATA[r_s1][c_s1] == "S"
                        m2 = check_boundary(r_m2, c_m2) and DATA[r_m2][c_m2] == "M"
                        s2 = check_boundary(r_s2, c_s2) and DATA[r_s2][c_s2] == "S"
                        if s1 and m2 and s2:
                            result += 1

    return result


submit(solve(), part="a", day=DAY, year=2024)
submit(part2(), part="b", day=DAY, year=2024)
