"""
Each robot's velocity is given as v=x,y where x and y are given in tiles per second. Positive x means the robot is moving to the right, and positive y means the robot is moving down.
"""

from collections import defaultdict

N = 103
M = 101


class Robot:
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel

    def update(self):
        x, y = self.pos
        dx, dy = self.vel
        # Update the position directly
        self.pos = ((x + dx) % M, (y + dy) % N)

    def __str__(self):
        return f"x: {self.pos[0]}, y: {self.pos[1]}"


def calc_safety_factor(robots):
    first = second = third = fourth = 0
    middle_horizontal = N // 2
    middle_vertical = M // 2
    for robot in robots:
        x, y = robot.pos
        if y < middle_horizontal and x < middle_vertical:
            first += 1
        elif y < middle_horizontal and x > middle_vertical:
            second += 1
        elif y > middle_horizontal and x < middle_vertical:
            third += 1
        elif y > middle_horizontal and x > middle_vertical:
            fourth += 1
    return first * second * third * fourth


def compute(s):
    lines = s.splitlines()
    robots = []
    arr = [line.split() for line in lines]
    for item in arr:
        p = item[0].split("=")
        p_x, p_y = list(map(int, p[1].split(",")))
        v = item[1].split("=")
        v_x, v_y = list(map(int, v[1].split(",")))
        robots.append(Robot((p_x, p_y), (v_x, v_y)))

    for _ in range(100):
        for robot in robots:
            robot.update()

    return calc_safety_factor(robots)


def main():
    #     input = """\
    # p=0,4 v=3,-3
    # p=6,3 v=-1,-3
    # p=10,3 v=-1,2
    # p=2,0 v=2,-1
    # p=0,0 v=1,3
    # p=3,0 v=-2,-2
    # p=7,6 v=-1,-3
    # p=3,0 v=-1,-2
    # p=9,3 v=2,3
    # p=7,3 v=-1,2
    # p=2,4 v=2,-3
    # p=9,5 v=-3,-3
    # """
    #     res = compute(input)
    #     print(res)

    file = open("input.txt")
    s = file.read()
    res = compute(s)
    print(res)


if __name__ == "__main__":
    main()
