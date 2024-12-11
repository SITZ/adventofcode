# Problem: https://adventofcode.com/2024/day/11
from collections import defaultdict

stones = list(map(int, open('input.txt', 'r').readline().strip().split()))
print(stones)

stone_map = defaultdict(int)


def count_stones(stone, blinks):
    if blinks == 0:
        return 1
    if (stone, blinks) in stone_map:
        return stone_map[(stone, blinks)]

    if stone == 0:
        stone_count = count_stones(1, blinks - 1)
    elif not (stone_length := len(str(stone))) % 2:
        stone_left, stone_right = int(str(stone)[:stone_length // 2]), int(str(stone)[stone_length // 2:])
        stone_count = count_stones(stone_left, blinks - 1) + count_stones(stone_right, blinks - 1)
    else:
        stone_count = count_stones(stone * 2024, blinks - 1)

    stone_map[(stone, blinks)] = stone_count
    return stone_count


def count_stones_total(stones, blinks):
    total_stone_count = 0
    for stone in stones:
        total_stone_count += count_stones(stone, blinks)
    return total_stone_count


print(f'Stone counter after blink #25:', count_stones_total(stones, 25))
print(f'Stone counter after blink #75:', count_stones_total(stones, 75))
