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
    robots = init_robots(s)
    for _ in range(100):
        update(robots)

    return calc_safety_factor(robots)


def init_robots(s):
    lines = s.splitlines()
    robots = []
    arr = [line.split() for line in lines]
    for item in arr:
        p = item[0].split("=")
        p_x, p_y = list(map(int, p[1].split(",")))
        v = item[1].split("=")
        v_x, v_y = list(map(int, v[1].split(",")))
        robots.append(Robot((p_x, p_y), (v_x, v_y)))
    return robots


def update(robots):
    for robot in robots:
        robot.update()


def look_for_trees(s):
    robots = init_robots(s)
    for iter in range(8259):
        update(robots)
        print_grid(robots, iter)


def print_grid(robots, iter):
    # 1) Create an empty grid
    grid = [[0] * M for _ in range(N)]

    # 2) Mark each robot’s position
    for robot in robots:
        x, y = robot.pos
        grid[y][x] += 1

    # 3) Build the output
    res = ""
    for row in grid:
        line = "".join("#" if val != 0 else " " for val in row)
        res += line + "\n"

    # 4) Write it to output file
    with open("output.txt", "a") as f:
        f.write(f"Iteration {iter}: \n")
        f.write(res)
        f.write("\n")  # extra blank line if you want separation


def main():
    file = open("input.txt")
    s = file.read()
    res = compute(s)
    look_for_trees(s)
    print(res)


if __name__ == "__main__":
    main()
