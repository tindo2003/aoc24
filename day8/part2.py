from itertools import product, combinations
import math 
from collections import defaultdict

def compute(s):
    lines = s.splitlines()
    grid = [line for line in lines]
    N, M = len(grid), len(grid[0])
    my_dict = defaultdict(list)
    for r in range(N):
        for c in range(M):
            if grid[r][c] != ".":
                my_dict[grid[r][c]].append((r, c))
    cnt = 0

    def in_bound(x, y) -> bool:
        return 0 <= x < N and 0 <= y < M 

    def antinode_generator(p1, p2):
        x1, y1 = p1 
        x2, y2 = p2 
        dx = x2 - x1
        dy = y2 - y1 
        offset = 0 
        while in_bound(x1 - offset * dx, y1 - offset * dy):
            yield x1 - offset * dx, y1 - offset * dy
            offset += 1
        offset = 0
        while in_bound(x2 + offset * dx, y2 + offset * dy):
            yield x2 + offset * dx, y2 + offset * dy
            offset += 1
    

    my_set = set()
    for k, v in my_dict.items():
        for p1, p2 in combinations(v, r=2):
            for ax, ay in antinode_generator(p1, p2):
                my_set.add((ax, ay))
    
    return len(my_set)


def main():
    input = """\
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""
    res = compute(input)
    print(res)

    file = open("input.txt")
    s = file.read()
    res = compute(s)
    print(res)


if __name__ == "__main__":
    main()
