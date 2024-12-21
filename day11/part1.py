from collections import defaultdict, Counter


def compute(s):
    cnt = 75
    lst = s.split()
    lst = list(map(int, lst))
    old_dict = Counter(lst)
    for _ in range(cnt):
        old_dict = blink(old_dict)
    res = 0
    for k, v in old_dict.items():
        res += v
    return res


def blink(old_dict: dict):
    new_dict = defaultdict(int)
    for item in old_dict:
        item_str = str(item)
        N = len(item_str)
        if item == 0:
            new_dict[1] += old_dict[0]
        elif N % 2 == 0:
            middle = N // 2
            new_dict[int(item_str[0:middle])] += old_dict[item]
            new_dict[int(item_str[middle:])] += old_dict[item]
        else:
            new_dict[item * 2024] += old_dict[item]
    return new_dict


def main():
#     input = """\
# 125 17
# """
#     res = compute(input)
#     print(res)
    file = open("input.txt")
    s = file.read()
    res = compute(s)
    print(res)


if __name__ == "__main__":
    main()
