from collections import deque


def compute(s):
    lines = s.splitlines()

    grid = [list(line) for line in lines]
    N, M = len(grid), len(grid[0])
    visited = [[False] * M for _ in range(N)]
    direction = [[0, 1], [1, 0], [-1, 0], [0, -1]]

    def bfs(r, c):
        p = 0
        a = 0
        val = grid[r][c]
        q = deque([(r, c)])
        while q:
            x, y = q.popleft()
            a += 1
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == val:
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny))
                else:
                    p += 1
        return p, a

    res = 0
    for r in range(N):
        for c in range(M):
            if not visited[r][c]:
                visited[r][c] = True
                p, a = bfs(r, c)
                print("p", p, "a", a)
                res += p * a
    return res


def main():
    input = """\
EEEEE
EXXXX
EEEEE
EXXXX
EEEEE
"""
    res = compute(input)
    print(res)
    # file = open("input.txt")
    # s = file.read()
    # res = compute(s)
    # print(res)


if __name__ == "__main__":
    main()
