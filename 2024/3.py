# Problem: https://adventofcode.com/2024/day/3

import re


def get_multiplications(multiplications):
    total_multiplications = 0
    for multiplication in multiplications:
        X, Y = map(int, re.findall("\d{1,3}", multiplication))
        total_multiplications += X * Y
    return total_multiplications


def get_conditional_multiplications(instructions):
    multiplications = []
    is_multiplication_enabled = True
    for instruction in instructions:
        if instruction == "do()":
            is_multiplication_enabled = True
        elif instruction == "don't()":
            is_multiplication_enabled = False
        elif is_multiplication_enabled:
            multiplications.append(instruction)

    return get_multiplications(multiplications)


memory = open("input.txt").read().replace('\n', ' ')

# Part-1
print('total_multiplications', re.findall("mul\(\d{1,3},\d{1,3}\)", memory))

# Part-2
print(
    'total_conditional_multiplications',
    get_conditional_multiplications(re.findall("mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", memory))
)
