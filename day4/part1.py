def compute(s: str) -> int:
    lines = s.splitlines()
    res = 0
    def f(start_x, start_y, dx, dy) -> bool:
        for i, c in enumerate("XMAS"):
            nx = start_x + dx * i 
            ny = start_y + dy * i 
            if 0 <= nx < len(lines[0]) and 0 <= ny < len(lines):
                if lines[ny][nx] != c: 
                    return False 
            else: return False
        return True 

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            for dx in [-1,0,1]:
                for dy in [-1,0,1]:
                    if dx == dy == 0: continue 
                    if f(x, y, dx, dy): res += 1
    return res


def main():
    f = open("input.txt", "r")
    s = f.read()
    res = compute(s)
    print(res)

    input = "MMMSXXMASM\nMSAMXMSMSA\nAMXSXMAAMM\nMSAMASMSMX\nXMASAMXAMM\nXXAMMXXAMA\nSMSMSASXSS\nSAXAMASAAA\nMAMMMXMMMM\nMXMXAXMASX"
    tmp = compute(input)
    print(tmp)


if __name__ == "__main__":
    main()
