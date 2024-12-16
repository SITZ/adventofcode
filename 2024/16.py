# Problem: https://adventofcode.com/2024/day/16

import heapq
from collections import defaultdict

RIGHT, DOWN, LEFT, UP = range(4)
moves = {
    RIGHT: (1, 0),
    DOWN: (0, 1),
    LEFT: (-1, 0),
    UP: (0, -1),
}

with open("input.txt", "r") as file:
    grid = file.read().splitlines()
    width, height = len(grid[0]), len(grid)

    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c == "S":
                start = x, y
            elif c == "E":
                end = x, y

    visited = set()
    paths = defaultdict(list)
    lowest_score = None

    score_pq = [(0, *start, RIGHT)]
    while score_pq:
        score, x, y, direction = heapq.heappop(score_pq)

        if lowest_score is not None and score > lowest_score:
            break

        if (x, y) == end:
            lowest_score = score
            continue

        if (x, y, direction) in visited:
            continue
        visited.add((x, y, direction))

        for next_move in (1, -1):
            next_direction = (direction + next_move) % 4
            heapq.heappush(score_pq, (score + 1000, x, y, next_direction))
            paths[(score + 1000, x, y, next_direction)].append((score, x, y, direction))

        dx, dy = moves[direction]
        next_x, next_y = x + dx, y + dy
        if grid[next_y][next_x] != "#":
            heapq.heappush(score_pq, (score + 1, next_x, next_y, direction))
            paths[(score + 1, next_x, next_y, direction)].append((score, x, y, direction))

    print("Part 1:", lowest_score)

    optimal_path_tiles = set()
    path_pq = [(lowest_score, *end, move) for move in moves]
    while path_pq:
        score, x, y, direction = path_pq.pop()
        optimal_path_tiles.add((x, y))
        for state in paths[(score, x, y, direction)]:
            path_pq.append(state)

    print("Part 2:", len(optimal_path_tiles))
