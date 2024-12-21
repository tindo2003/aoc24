def compute(s):
    initial, movements = s.split("\n\n")
    lines = initial.splitlines()
    print(lines)
    N, M = len(lines) - 2, len(lines[0]) - 2
    print(N, M)
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
            if 0 <= new_c < N and 0 <= new_c < M:
                # 3 cases: 
                # 1 empty space, do nothing. 
                if grid[new_r][new_c] == "#": continue
                # 2 box 
                if grid[new_r][new_c] == "O": 
                    tmp_r, tmp_c = new_r, new_c - 1
                    while tmp_c >= 0 and grid[tmp_c] not in ["#", "."]:
                        tmp_c -= 1
                    if grid[new_r][tmp_c] == "#" or tmp_c < 0: continue
                    else:
                        while tmp_c != new_c:
                            grid[new_r][tmp_c] = "O"
                            tmp_c += 1
                # box next to other box 
                cur_pos = new_r, new_c
        elif movement == ">":
            new_r, new_c = r, c + 1
        elif movement == "^":
            new_r, new_c = r - 1, c
        else: 
            new_r, new_c = r + 1, c
        
    print(cur_pos)


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


if __name__ == "__main__":
    main()
