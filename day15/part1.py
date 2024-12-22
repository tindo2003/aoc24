def compute(s):
    initial, movements = s.split("\n\n")
    lines = initial.splitlines()

    N, M = len(lines) - 2, len(lines[0]) - 2
    grid = [[-1] * M for _ in range(N)]
    for r in range(1, N + 1):
        for c in range(1, M + 1):
            grid[r - 1][c - 1] = lines[r][c]
    movements = list("".join(movements.splitlines()))
    cur_pos = (-1, -1)
    for r in range(N):
        for c in range(M):
            if grid[r][c] == "@":
                cur_pos = (r, c)

    for movement in movements:
        r, c = cur_pos
        if movement == "<":
            new_r, new_c = r, c - 1
            if 0 <= new_r < N and 0 <= new_c < M:
                # 3 cases:
                # 1 empty space, do nothing.
                if grid[new_r][new_c] == "#":
                    continue
                # 2 box
                if grid[new_r][new_c] == "O":
                    tmp_r, tmp_c = new_r, new_c - 1
                    while tmp_c >= 0 and grid[tmp_r][tmp_c] not in ["#", "."]:
                        tmp_c -= 1
                    if tmp_c < 0 or grid[tmp_r][tmp_c] == "#":
                        continue
                    while tmp_c != new_c:
                        grid[tmp_r][tmp_c] = "O"
                        tmp_c += 1
                # box next to empty slot
                grid[r][c] = "."
                cur_pos = new_r, new_c
        elif movement == ">":
            new_r, new_c = r, c + 1
            if 0 <= new_r < N and 0 <= new_c < M:
                # 3 cases:
                # 1 empty space, do nothing.
                if grid[new_r][new_c] == "#":
                    continue
                # 2 box
                if grid[new_r][new_c] == "O":
                    tmp_r, tmp_c = new_r, new_c + 1
                    while tmp_c < M and grid[tmp_r][tmp_c] not in ["#", "."]:
                        tmp_c += 1
                    if tmp_c >= M or grid[tmp_r][tmp_c] == "#":
                        continue
                    while tmp_c != new_c:
                        grid[tmp_r][tmp_c] = "O"
                        tmp_c -= 1
                # box next to empty slot
                grid[r][c] = "."
                cur_pos = new_r, new_c
        elif movement == "^":
            new_r, new_c = r - 1, c
            if 0 <= new_r < N and 0 <= new_c < M:
                # 3 cases:
                # 1 empty space, do nothing.
                if grid[new_r][new_c] == "#":
                    continue
                # 2 box
                if grid[new_r][new_c] == "O":
                    tmp_r, tmp_c = new_r - 1, new_c
                    while tmp_r >= 0 and grid[tmp_r][tmp_c] not in ["#", "."]:
                        tmp_r -= 1
                    if tmp_r < 0 or grid[tmp_r][tmp_c] == "#":
                        continue
                    while tmp_r != new_r:
                        grid[tmp_r][tmp_c] = "O"
                        tmp_r += 1
                # box next to empty slot
                grid[r][c] = "."
                cur_pos = new_r, new_c
        else:
            new_r, new_c = r + 1, c
            if 0 <= new_r < N and 0 <= new_c < M:
                # 3 cases:
                # 1 empty space, do nothing.
                if grid[new_r][new_c] == "#":
                    continue
                # 2 box
                if grid[new_r][new_c] == "O":
                    tmp_r, tmp_c = new_r + 1, new_c
                    while tmp_r < N and grid[tmp_r][tmp_c] not in ["#", "."]:
                        tmp_r += 1
                    if tmp_r >= N or grid[tmp_r][tmp_c] == "#":
                        continue
                    while tmp_r != new_r:
                        grid[tmp_r][tmp_c] = "O"
                        tmp_r -= 1
                # box next to empty slot
                grid[r][c] = "."
                cur_pos = new_r, new_c

    res = calculate_gps_box(grid)
    return res




def calculate_gps_box(my_grid):
    res = 0
    N, M = len(my_grid), len(my_grid[0])
    for r in range(N):
        for c in range(M):
            if my_grid[r][c] == "O":
                res += 100 * (r + 1) + (c + 1)
    return res


def main():
    input = """\
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
"""
    res = compute(input)
    print(res)

    file = open("input.txt")
    s = file.read()
    res = compute(s)
    print(res)


if __name__ == "__main__":
    main()
