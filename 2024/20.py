# Problem: https://adventofcode.com/2024/day/20

import heapq
from collections import deque
from typing import List, Tuple, Set, Dict


def parse_map(grid_str: str) -> Tuple[List[List[str]], Tuple[int, int], Tuple[int, int]]:
    grid = [list(line) for line in grid_str.strip().split('\n')]
    start = end = None
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 'S':
                start = (i, j)
            elif cell == 'E':
                end = (i, j)
    return grid, start, end


def get_neighbors(position: Tuple[int, int], grid: List[List[str]], allow_walls: bool = False) -> List[Tuple[int, int]]:
    i, j = position
    neighbors = []
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        next_i, next_j = i + di, j + dj
        if 0 <= next_i < len(grid) and 0 <= next_j < len(grid[0]):
            if allow_walls or grid[next_i][next_j] != '#':
                neighbors.append((next_i, next_j))
    return neighbors


def shortest_paths(grid: List[List[str]], start: Tuple[int, int]) -> Dict[Tuple[int, int], int]:
    distances = {start: 0}
    queue = [(0, start)]

    while queue:
        distance, position = heapq.heappop(queue)
        if distance > distances[position]:
            continue

        next_distance = distance + 1
        for next_position in get_neighbors(position, grid):
            if next_position not in distances or next_distance < distances[next_position]:
                distances[next_position] = next_distance
                heapq.heappush(queue, (next_distance, next_position))

    return distances


def find_cheats_from_position(
        start_position: Tuple[int, int],
        grid: List[List[str]],
        base_distances: Dict[Tuple[int, int], int],
        max_cheat_steps: int
) -> Set[Tuple[Tuple[int, int], int]]:
    """Find all possible cheats starting from a given position. Returns a set of (end_position, savings) tuples."""

    cheats = set()  # Use a set to store unique (end_pos, savings) combinations
    visited = {start_position}
    queue = deque([(start_position, 0)])  # (position, cheat_steps)

    while queue:
        position, cheat_steps = queue.popleft()
        if cheat_steps >= max_cheat_steps:
            continue

        # Try all possible next positions
        for next_position in get_neighbors(position, grid, allow_walls=True):
            # Skip if we've been here during this cheat
            if next_position in visited:
                continue

            # If this is a valid path position (not a wall), calculate potential savings
            if grid[next_position[0]][next_position[1]] != '#' and next_position in base_distances:
                normal_time = base_distances[next_position] - base_distances[start_position]
                cheat_time = cheat_steps + 1
                if normal_time > cheat_time:
                    # Store the end position and the savings
                    cheats.add((next_position, normal_time - cheat_time))

            # Continue exploring if we haven't used all cheat steps
            if cheat_steps + 1 < max_cheat_steps:
                visited.add(next_position)
                queue.append((next_position, cheat_steps + 1))

    return cheats


def solve(grid_str: str, max_cheats: int = 2, min_savings: int = 1) -> int:
    # Parse input
    grid, start, end = parse_map(grid_str)

    # Get base distances from all points to end
    base_distances = shortest_paths(grid, end)

    # Track unique cheats by their (start_pos, end_pos) -> max_savings combination
    unique_cheats = {}

    # Find all possible cheats from each valid starting position
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != '#' and (i, j) in base_distances:
                start_position = (i, j)
                cheats = find_cheats_from_position(start_position, grid, base_distances, max_cheats)

                # Update unique_cheats with the maximum savings for each start/end combination
                for end_position, savings in cheats:
                    key = (start_position, end_position)
                    unique_cheats[key] = max(unique_cheats.get(key, 0), savings)

    # Count unique cheats that save >= min_savings picoseconds
    return sum(1 for savings in unique_cheats.values() if savings >= min_savings)


input = open('input.txt', 'r').read()
print(f"Part 1 - Number of cheats saving ≥100 picoseconds: {solve(input, max_cheats=2, min_savings=100)}")
print(f"Part 2 - Number of cheats saving ≥100 picoseconds: {solve(input, max_cheats=20, min_savings=100)}")
