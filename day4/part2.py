def compute(s: str) -> int:
    lines = s.splitlines()
    print(lines)
    res = 0

    M = len(lines[0])
    N = len(lines)
    for r, line in enumerate(lines):
        for c, ch in enumerate(line):
            if ch == "A":
                up = r - 1
                down = r + 1
                left = c - 1
                right = c + 1
                if 0 <= up < N and 0 <= down < N and 0 <= left < M and 0 <= right < M:
                    nw = lines[up][left]
                    ne = lines[up][right]
                    sw = lines[down][left]
                    se = lines[down][right]
                    if (nw == "M" and se == "S") or (nw == "S" and se == "M"):
                        if (sw == "M" and ne == "S") or (sw == "S" and ne == "M"):
                            res += 1
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
