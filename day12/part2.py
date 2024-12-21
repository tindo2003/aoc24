from collections import deque, defaultdict
from tqdm import tqdm


def compute(s):
    lines = s.splitlines()

    grid = [list(line) for line in lines]
    N, M = len(grid), len(grid[0])
    visited = set()
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    plots = defaultdict(set)

    def dfs(r, c, val, lst):
        nonlocal plots
        for dr, dc in directions:
            nr, nc = r + dr, dc + c
            if (
                0 <= nr < N
                and 0 <= nc < M
                and (nr, nc) not in visited
                and grid[nr][nc] == val
            ):
                visited.add((nr, nc))
                lst.append((nr, nc))
                dfs(nr, nc, val, lst)

    plots = []
    for r in range(N):
        for c in range(M):
            if (r, c) not in visited:
                visited.add((r, c))
                tmp = [(r, c)]
                dfs(r, c, grid[r][c], tmp)
                plots.append(tmp)

    def perim(plot):
        # Iterate through all 2x2 subplots
        corners = [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
            [0, 1, 1, 1],
            [1, 1, 1, 0],
            [1, 0, 1, 1],
            [1, 1, 0, 1],
        ]
        plot = set(plot)

        def test(plot, coors):
            return list(map(int, [item in plot for item in coors]))

        min_r = min(r for r, c in plot)
        max_r = max(r for r, c in plot) + 1
        min_c = min(c for r, c in plot)
        max_c = max(c for r, c in plot) + 1

        ans = 0
        for i in range(min_r - 1, max_r):
            for j in range(min_c - 1, max_c):
                lst = test(plot, [(i, j), (i, j + 1), (i + 1, j), (i + 1, j + 1)])
                has_corner = lst in corners
                has_double_corner = lst in [[1, 0, 0, 1], [0, 1, 1, 0]]
                ans += has_corner + has_double_corner * 2

        return ans

    res = 0
    for plot in tqdm(plots, desc="Processing Plots", unit="plot"):
        print(perim(plot), len(plot))
        res += perim(plot) * len(plot)
    return res


def main():
#     input = """\
# AAAAAA
# AAABBA
# AAABBA
# ABBAAA
# ABBAAA
# AAAAAA
# """
#     res = compute(input)
#     print(res)
    file = open("input.txt")
    s = file.read()
    res = compute(s)
    print(res)


if __name__ == "__main__":
    main()
