# Problem: https://adventofcode.com/2024/day/10

trail_map = [list(map(int, row.strip())) for row in open("input.txt", "r").readlines()]
print(trail_map)

trailhead_paths = []


def dfs(current_i, current_j, trail_heights, trail_path):
    if trail_map[current_i][current_j] == 9 and len(trail_heights) == 9:
        trailhead_paths.append(trail_path + [(current_i, current_j)])
        return {(current_i, current_j)}

    trailhead_locations = set()
    for (delta_i, delta_j) in [(-1, 0), (+1, 0), (0, -1), (0, +1)]:
        next_i, next_j = current_i + delta_i, current_j + delta_j
        if 0 <= next_i < len(trail_map) and 0 <= next_j < len(trail_map[0]) and trail_map[next_i][next_j] == trail_map[current_i][current_j] + 1:
            trailhead_locations = trailhead_locations.union(dfs(next_i, next_j, trail_heights + [trail_map[current_i][current_j]], trail_path + [(current_i, current_j)]))
    return trailhead_locations


total_trailhead_score = 0
for i in range(len(trail_map)):
    for j in range(len(trail_map[i])):
        if trail_map[i][j] == 0:
            total_trailhead_score += len(dfs(i, j, [], []))

print('total_trailhead_score', total_trailhead_score)
print('total_trailhead_rating', len(trailhead_paths))
