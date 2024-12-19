# Problem: https://adventofcode.com/2024/day/19

file = open("input.txt", "r")

patterns = [pattern.strip() for pattern in file.readline().strip().split(",")]
print(patterns)

possible_patterns = dict()


def count_valid_designs(pattern):
    count = pattern in patterns
    for i in range(1, len(pattern)):
        if pattern[:i] in patterns:
            sub_pattern = pattern[i:]
            if sub_pattern not in possible_patterns:
                possible_patterns[sub_pattern] = count_valid_designs(sub_pattern)
            count += possible_patterns[sub_pattern]
    return count


def is_valid_design(pattern):
    if pattern in patterns:
        return True
    for i in range(1, len(pattern)):
        if pattern[:i] in patterns and is_valid_design(pattern[i:]):
            return True
    return False


designs = [design.strip() for design in file]
print(designs)

valid_designs = sum([is_valid_design(design) for design in designs])
print('Valid designs:', valid_designs)

valid_designs_count = sum([count_valid_designs(design) for design in designs])
print('Valid designs count:', valid_designs_count)
