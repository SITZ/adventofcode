# Problem: https://adventofcode.com/2024/day/2

def is_safe(levels):
    # Part-1
    level_gaps = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]
    return (all(level_gap >= 1 and level_gap <= 3 for level_gap in level_gaps) or
            all(level_gap <= -1 and level_gap >= -3 for level_gap in level_gaps))


def is_safe_with_dampener(levels):
    # Part-2
    for i in range(len(levels)):
        new_levels = levels[:i] + levels[i + 1:]
        if is_safe(new_levels):
            return True

    return False


total_safe = 0
total_safe_with_dampener = 0
for line in open('input.txt'):
    levels = list(map(int, line.strip().split()))
    print(levels)

    print(
        f'is_safe: {is_safe(levels)}\n'
        f'is_safe_with_dampener: {is_safe_with_dampener(levels)}'
    )
    total_safe += is_safe(levels)
    total_safe_with_dampener += is_safe_with_dampener(levels)

print()
print(
    f'total_safe: {total_safe}\n'
    f'total_safe_with_dampener: {total_safe_with_dampener}'
)
