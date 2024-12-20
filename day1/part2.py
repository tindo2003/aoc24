from collections import Counter 

def compute(s):
    lst1, lst2 = [], []
    for line in s.splitlines():
        n1_s, n2_s = line.split()
        lst1.append(int(n1_s))
        lst2.append(int(n2_s))
    lst2_freq = Counter(lst2)
    res = 0
    for num in lst1:
        res += (lst2_freq[num] * num)
    return res


def main():
    f = open("input.txt", "r")
    s = f.read()
    res = compute(s)
    print(res)

if __name__ == "__main__":
    main()