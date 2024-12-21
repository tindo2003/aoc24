def compute_part1(s):
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    lines = s.splitlines()
    grid = [list(map(int, line)) for line in lines]
    N, M = len(grid), len(grid[0])
    counter = 0

    def dfs(r, c, visited):
        nonlocal counter
        if grid[r][c] == 9:
            counter += 1
            return
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and (nr, nc) not in visited:
                new_val = grid[nr][nc]
                old_val = grid[r][c]
                if new_val - old_val == 1:
                    visited.add((nr, nc))
                    dfs(nr, nc, visited)

    res = 0
    for r in range(N):
        for c in range(M):
            if grid[r][c] == 0:
                counter = 0
                my_set = set()
                dfs(r, c, my_set)
                res += counter
    return res


def compute_part2(s):
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    lines = s.splitlines()
    grid = [list(map(int, line)) for line in lines]
    N, M = len(grid), len(grid[0])
    counter = 0

    def dfs(r, c, visited):
        nonlocal counter
        if grid[r][c] == 9:
            counter += 1
            return
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and (nr, nc) not in visited:
                new_val = grid[nr][nc]
                old_val = grid[r][c]
                if new_val - old_val == 1:
                    dfs(nr, nc, visited)

    res = 0
    for r in range(N):
        for c in range(M):
            if grid[r][c] == 0:
                counter = 0
                my_set = set()
                dfs(r, c, my_set)
                res += counter
    return res


def main():
    input = """\
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""
    res = compute_part2(input)
    print(res)

    file = open("input.txt")
    s = file.read()
    res = compute_part2(s)
    print(res)


if __name__ == "__main__":
    main()
