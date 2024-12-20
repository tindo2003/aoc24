import functools


def compute(s: str):
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    lines = s.splitlines()
    lines = [list(line) for line in lines]
    N, M = len(lines), len(lines[0])
    cur = (-1, -1)
    found = False
    direction = -1
    for r in range(N):
        for c in range(M):
            if lines[r][c] == "^":
                direction = 0
                found = True
                cur = (r, c)
                break
        if found:
            break
    visited = set()

    tr, tc = cur
    while 1:
        visited.add((tr, tc))

        dr, dc = directions[direction]
        nr, nc = tr + dr, tc + dc
        if not (0 <= nr < N and 0 <= nc < M):
            break
        if lines[nr][nc] == "#":
            direction = (direction + 1) % 4
            continue
        tr = nr
        tc = nc

    def is_loop(o_r, o_c) -> bool:
        lines[o_r][o_c] = "#"
        visited = set()
        tr, tc = cur
        direction = 0
        while 1:
            if (tr, tc, direction) in visited:
                lines[o_r][o_c] = "."
                return True

            visited.add((tr, tc, direction))

            dr, dc = directions[direction]
            nr, nc = tr + dr, tc + dc
            if not (0 <= nr < N and 0 <= nc < M):
                lines[o_r][o_c] = "."
                return False
            if lines[nr][nc] == "#":
                direction = (direction + 1) % 4
                continue

            (tr, tc) = (nr, nc)

    cnt = 0
    for r, c in visited:
        if is_loop(r, c):
            cnt += 1
    return cnt


def main():
    input = """\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""
    res = compute(input)
    print(res)

    f = open("input.txt", "r")
    s = f.read()
    res = compute(s)
    print(res)


if __name__ == "__main__":
    main()
