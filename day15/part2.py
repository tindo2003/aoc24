def compute(s):
    initial, movements = s.split("\n\n")
    lines = initial.splitlines()
    walls = set()
    boxes = []
    directions = {"^": [-1, 0], ">": [0, 1], "v": [1, 0], "<": [0, -1]}

    N, M = len(lines), len(lines[0])
    print(N, M)
    grid = [list(line) for line in initial.split("\n")]

    movements = list("".join(movements.splitlines()))
    cur_r, cur_c = 0, 0
    for r in range(N):
        for c in range(M):
            cur_ele = grid[r][c]
            if cur_ele == "@":
                cur_r, cur_c = r, 2 * c
                print(cur_r, cur_c)
            elif cur_ele == "#":
                walls.add((r, 2 * c))
                walls.add((r, 2 * c + 1))
            # only add the "[" out of "[]"
            elif cur_ele == "O":
                boxes.append([r, 2 * c])

    def is_in_bound(r, c) -> bool:
        return 0 <= r < N and 0 <= c < 2 * M

    def dfs(cur_r, cur_c, dr, dc):
        stack = []
        visited = set()

        nr, nc = cur_r + dr, cur_c + dc
        if not is_in_bound(nr, nc):
            return (cur_r, cur_c)
        if (nr, nc) in walls:
            return (cur_r, cur_c)

        if [nr, nc] in boxes:
            stack.append((nr, nc))
            visited.add((nr, nc))
        # when the right bracket is touched, check if left bracket is touched
        if [nr, nc - 1] in boxes:
            visited.add((nr, nc - 1))
            stack.append((nr, nc - 1))

        can_move = True
        while stack:
            top_r, top_c = stack.pop()
            nr, nc = top_r + dr, top_c + dc
            if not is_in_bound(nr, nc) or (nr, nc) in walls or (nr, nc + 1) in walls:
                can_move = False
                break

            if [nr, nc] in boxes and (nr, nc) not in visited:
                visited.add((nr, nc))
                stack.append((nr, nc))
            # @[][] -> robot want to move right. top is at the left most left bracket. nr, nc is left most right bracket.
            if [nr, nc + 1] in boxes and (nr, nc + 1) not in visited:
                visited.add((nr, nc + 1))
                stack.append((nr, nc + 1))
            # [][]@ -> robot want to move left. top is at the right most [. nr, nc is left most ]. nr, nc-1 is left most [
            if [nr, nc - 1] in boxes and (nr, nc - 1) not in visited:
                visited.add((nr, nc - 1))
                stack.append((nr, nc - 1))

        if not can_move:
            return (cur_r, cur_c)

        for idx, box in enumerate(boxes):
            if tuple(box) in visited:
                boxes[idx][0] += dr
                boxes[idx][1] += dc
        cur_r += dr
        cur_c += dc
        return (cur_r, cur_c)

    for movement in movements:
        dr, dc = directions[movement]
        cur_r, cur_c = dfs(cur_r, cur_c, dr, dc)

    res = 0
    for box in boxes:
        res += 100 * box[0] + box[1]
    return res

    # res = calculate_gps_box(grid)
    # return res


def calculate_gps_box(my_grid):
    res = 0
    N, M = len(my_grid), len(my_grid[0])
    for r in range(N):
        for c in range(M):
            if my_grid[r][c] == "O":
                res += 100 * (r) + (c)
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

    f = open("input.txt")
    s = f.read()
    res = compute(s)
    print(res)


if __name__ == "__main__":
    main()
