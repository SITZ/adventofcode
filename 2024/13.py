# Problem: https://adventofcode.com/2024/day/12

import re
import sys

lines = open('input.txt', 'r').readlines()
print(lines)


def tokens_part1(button_a, button_b, prize):
    # Brute force
    token_count = sys.maxsize
    for count_a in range(100):
        for count_b in range(100):
            if (
                    button_a[0] * count_a + button_b[0] * count_b == prize[0] and
                    button_a[1] * count_a + button_b[1] * count_b == prize[1]
            ):
                token_count = min(token_count, count_a * 3 + count_b * 1)

    return token_count if token_count != sys.maxsize else 0


def tokens_part2(a, b, prize):
    # Cramer's rule
    D = a[0] * b[1] - a[1] * b[0]
    Dx = prize[0] * b[1] - prize[1] * b[0]
    Dy = a[0] * prize[1] - a[1] * prize[0]

    if D != 0:
        x_float = Dx / D
        y_float = Dy / D

        if x_float.is_integer() and y_float.is_integer():
            return 3 * int(x_float) + int(y_float)
    return 0


total_token_part1 = 0
total_token_part2 = 0
for index in range(len(lines) // 4 + 1):
    button_a = tuple(map(int, re.findall(r'\d+', lines[index * 4 + 0])))
    button_b = tuple(map(int, re.findall(r'\d+', lines[index * 4 + 1])))
    prize = tuple(map(int, re.findall(r'\d+', lines[index * 4 + 2])))

    total_token_part1 += tokens_part1(button_a, button_b, prize)
    total_token_part2 += tokens_part2(button_a, button_b, (prize[0] + 10000000000000, prize[1] + 10000000000000))

    print(f"total_tokens_part1: {total_token_part1}, total_tokens_part2: {total_token_part2}")
