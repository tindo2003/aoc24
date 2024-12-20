def compute(s: str) -> int:
    lst1, lst2 = [], []
    for line in s.splitlines():
        n1_s, n2_s = line.split()
        lst1.append(int(n1_s))
        lst2.append(int(n2_s))
    lst1.sort()
    lst2.sort()
    return sum(abs(n1 - n2) for n1, n2 in zip(lst1, lst2))   

def main():
    f = open("input.txt", "r")
    s = f.read()
    res = compute(s)
    print(res)

if __name__ == "__main__":
    main()