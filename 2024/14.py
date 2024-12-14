# Problem: https://adventofcode.com/2024/day/14

import re
from itertools import count

test_input = False
if test_input:
    file_name = 'input_test.txt'
    max_x, max_y = 11, 7
else:
    file_name = 'input.txt'
    max_x, max_y = 101, 103

times_x = []
times_y = []


def part_1():
    quadrant = [[0, 0], [0, 0]]
    for line in open(file_name, 'r'):
        start_x, start_y, velocity_x, velocity_y = list(map(int, re.findall(r"[-+]?\d+", line)))

        final_x = (start_x + velocity_x * 100) % max_x
        final_y = (start_y + velocity_y * 100) % max_y

        if final_x != max_x // 2 and final_y != max_y // 2:
            quadrant[round(final_x / max_x)][round(final_y / max_y)] += 1

    return quadrant[0][0] * quadrant[0][1] * quadrant[1][0] * quadrant[1][1]


print(f"total_safety_factor: {part_1()}")


def part_2():
    grid = [list(map(int, re.findall(r"[-+]?\d+", line))) for line in open(file_name, 'r')]

    for time in count(1):
        grid_current = [((x + dx * time) % max_x, (y + dy * time) % max_y) for x, y, dx, dy in grid]
        grid_unique = set(grid_current)

        if len(grid_current) != len(grid_unique):
            continue

        for y in range(max_y):
            for x in range(max_x):
                if (x, y) in grid_unique:
                    print("#", end="")
                else:
                    print(".", end="")
            print()

        return time


print(f"total_seconds_elapsed: {part_2()}")
