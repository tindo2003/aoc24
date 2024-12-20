def compute(s: str) -> int:
    all_lst = []
    for line in s.splitlines():
        all_lst.append([int(item) for item in line.split()])
    cnt = 0
    for lst in all_lst:
        for i in range(len(lst)):
            if f(lst[0:i] + lst[i+1:]): 
                cnt += 1
                break 
    return cnt 

def f(lst) -> bool:
    direction = 1 if lst[1] - lst[0] > 0 else -1 
    N = len(lst)
    for n1, n2 in zip(lst[:N-1], lst[1:]):
        d = direction * (n2 - n1)
        if not (1 <= d <= 3):
            return False 
    return True 

def main():
    f = open("input.txt", "r")
    s = f.read()
    res = compute(s)
    print(res)

if __name__ == "__main__":
    main()
