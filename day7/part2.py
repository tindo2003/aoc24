from itertools import product
from tqdm import tqdm

def compute(s: str) -> int:
    def helper(nums, tgt) -> bool:
        for combo in product(["+", "*", "|"], repeat=len(nums) - 1):
            expression = nums[0]
            for idx in range(1, len(nums)):
                cur_num = nums[idx]
                if combo[idx - 1] == "+":
                    expression += cur_num
                elif combo[idx - 1] == "*":
                    expression *= cur_num
                else:
                    l = len(str(cur_num))
                    expression = expression * (10 ** l) + cur_num

                    #expression = int(f"{expression}{cur_num}")
            if expression == tgt:
                return True
        return False

    cnt = 0
    lines = s.strip().splitlines()
    for line in tqdm(lines):
        parts = line.split()
        expected_val = int(parts[0][:-1])
        rest = parts[1:]
        nums = list(map(int, rest))
        if helper(nums, expected_val):
            cnt += expected_val
    return cnt


def main():
    input = """\
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20    
"""
    res = compute(input)
    print(res)

    file = open("input.txt")
    s = file.read()
    res = compute(s)
    print(res)


if __name__ == "__main__":
    main()
