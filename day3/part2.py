import re

PAT = re.compile(r"mul\((\d+),(\d+)\)")


def compute(s: str) -> int:
    lst = PAT.findall(s)
    res = sum(int(n1) * int(n2) for n1, n2 in lst)
    return res


def main():
    f = open("input.txt", "r")
    s = f.read()
    res = compute(s)
    print(res)

    input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    tmp = compute(input)
    print(tmp)


if __name__ == "__main__":
    main()
