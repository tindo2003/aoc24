import functools


def compute(s: str):
    directions = [[-1,0],[0,1],[1,0],[0,-1]]
    lines = s.splitlines()
    N, M = len(lines), len(lines[0])
    cur = (-1,-1)
    found = False
    direction = -1
    for r in range(N):
        for c in range(M):
            if lines[r][c] == "^":
                direction = 0 
            elif lines[r][c] == ">":
                direction = 1
            elif lines[r][c] == "v":
                direction = 2
            elif lines[r][c] == "<":
                direction = 3
            if lines[r][c] in ["^", ">", "v", "<"]:
                found = True  
                cur = (r, c)
                break 
        if found:
            break 
    res = set()

    while 1:
        res.add(cur)
        print(cur)
        r, c = cur 
        if r == 0 or r == N - 1 or c == 0 or c == M - 1:
            break
        dr, dc = directions[direction]
        nr, nc = r + dr, c + dc 
        if lines[nr][nc] == "#":
            direction = (direction + 1) % 4
            continue 
        cur = (nr, nc)

    return len(res)


def main():
    f = open("input.txt", "r")
    s = f.read()
    res = compute(s)
    print(res)

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

    tmp = compute(input)
    print(tmp)


if __name__ == "__main__":
    main()
