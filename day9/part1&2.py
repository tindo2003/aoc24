from math import inf
from collections import defaultdict

max_id = -inf
loc = defaultdict(int)
size = defaultdict(int)


def calculate_checksum(n_s):
    res = 0
    for idx, val in enumerate(n_s):
        if val != ".":
            res += int(val) * idx
    return res


def make_fs(s):
    global max_id, loc, size
    id = 0
    my_str = []
    for idx, val in enumerate(s):
        val = int(val)
        if idx % 2 == 0:
            loc[id] = len(my_str)
            size[id] = val
            my_str += [str(id)] * val
            id += 1
        else:
            my_str += ["."] * val
    max_id = id - 1
    return my_str


def compute_part1(s):
    lines = s.strip()
    fs = make_fs(lines)

    N = len(fs)
    l, r = 0, N - 1
    while l <= r:
        while l < N and fs[l] != ".":
            l += 1
        while r >= 0 and fs[r] == ".":
            r -= 1
        if l >= r:
            break
        if l < N:
            fs[l] = fs[r]
            fs[r] = "."
            l += 1
            r -= 1
    print(loc, size)
    return calculate_checksum(fs)


def compute_part2(s):
    lines = s.strip()
    fs = make_fs(lines)
    N = len(fs)
    for id in range(max_id, 0, -1):
        # try first_free from index 0 every time
        first_free, free_space = 0, 0
        # only move from end of array to the left, not left to right
        while first_free < loc[id] and free_space < size[id]:
            first_free += free_space
            free_space = 0
            while fs[first_free] != ".":
                first_free += 1
            while first_free + free_space < N and fs[first_free + free_space] == ".":
                free_space += 1
        if first_free > loc[id]:
            continue
        for offset in range(size[id]):
            fs[first_free + offset] = fs[loc[id] + offset]
        for offset in range(size[id]):
            fs[loc[id] + offset] = "."
    return calculate_checksum(fs)


def main():
    file = open("input.txt")
    s = file.read()
    res = compute_part2(s)
    print(res)
    input = """\
2333133121414131402
"""
    res = compute_part2(input)
    print(res)


if __name__ == "__main__":
    main()
