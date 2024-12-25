# Problem: https://adventofcode.com/2024/day/23
from itertools import islice

locks = []
keys = []
with open('input.txt', 'r') as file:
    while True:
        schematic = list(islice(file, 7))
        if not schematic:
            break
        schematic = [line.strip() for line in schematic]

        header, footer = schematic[0], schematic[-1]
        empty, full = '.' * 5, '#' * 5
        columns = [sum([schematic[row][col] == '#' for row in range(1, len(schematic) - 1)]) for col in range(5)]

        if (header, footer) == (empty, full):
            keys.append(columns)
        elif (header, footer) == (full, empty):
            locks.append(columns)

        file.readline()

valid_pairs = 0
for lock in locks:
    for key in keys:
        valid_pairs += all([sum(x) <= 5 for x in zip(lock, key)])

print(f'Valid lock/key pairs:', valid_pairs)
