import functools


def compute(s: str):
    sorted_rules_s, rest = s.split("\n\n")
    sort_rules = set(
        tuple(int(n) for n in line.split("|")) for line in sorted_rules_s.splitlines()
    )

    @functools.cmp_to_key
    def key_func(o1, o2) -> int:
        if o1 == o2:
            return 0
        if (o1, o2) in sort_rules:
            return -1
        else:
            return 1

    res = 0
    for line in rest.splitlines():
        nums = [int(item) for item in line.split(",")]
        new_nums = sorted(nums, key=key_func)
        if new_nums != nums:
            res += new_nums[len(new_nums) // 2]
    return res


def main():
    f = open("input.txt", "r")
    s = f.read()
    res = compute(s)
    print(res)

    input = '''\
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
'''

    # tmp = compute(input)
    # print(tmp)


if __name__ == "__main__":
    main()
