# Problem: https://adventofcode.com/2024/day/12
import time

garden = open("input.txt", "r").readlines()
garden = [list(row.strip()) for row in garden]
print(garden)

ROWS, COLS = len(garden), len(garden[0])

visited = set()
deltas = [(-1, 0), (+1, 0), (0, -1), (0, +1)]


def dfs(i, j, plant, region):
    visited.add((i, j))
    region.add((i, j))

    for (delta_i, delta_j) in deltas:
        i_next, j_next = i + delta_i, j + delta_j

        if 0 <= i_next < ROWS and 0 <= j_next < COLS and (i_next, j_next) not in visited and garden[i_next][j_next] == plant:
            region = region.union(dfs(i_next, j_next, plant, region))

    return region


def count_sides(region):
    corner_candidates = set()
    for i, j in region:
        for ci, cj in [(i - 0.5, j - 0.5), (i + 0.5, j - 0.5), (i + 0.5, j + 0.5), (i - 0.5, j + 0.5)]:
            corner_candidates.add((ci, cj))

    corners = 0
    for ci, cj in corner_candidates:
        config = [(sr, sc) in region for sr, sc in [(ci - 0.5, cj - 0.5), (ci + 0.5, cj - 0.5), (ci + 0.5, cj + 0.5), (ci - 0.5, cj + 0.5)]]

        match sum(config):
            case 1: corners += 1
            case 2: corners += 2 if config == [True, False, True, False] or config == [False, True, False, True] else 0
            case 3: corners += 1
    return corners


total_price_part1 = 0
total_price_part2 = 0

for i in range(ROWS):
    for j in range(COLS):
        if (i, j) not in visited:
            region = dfs(i, j, garden[i][j], set())

            plant = garden[i][j]
            area = len(region)

            perimeter = 0
            for (region_i, region_j) in region:
                for (delta_i, delta_j) in deltas:
                    region_i_external, region_j_external = region_i + delta_i, region_j + delta_j

                    if (region_i_external, region_j_external) not in region:
                        perimeter += 1

            sides = count_sides(region)

            # print(f"Region {garden[i][j]}: area={area}, perimeter={perimeter}, sides={sides}")

            total_price_part1 += area * perimeter
            total_price_part2 += area * sides

print('total_price_part1', total_price_part1)
print('total_price_part2', total_price_part2)
