# Problem: https://adventofcode.com/2024/day/18
import collections

MEMORY_SIZE, failed_byte_count = 71, 1024

memory = [['.'] * MEMORY_SIZE for y in range(MEMORY_SIZE)]


def bfs():
    q = collections.deque([(0, 0, 0)])
    visited = {0, 0}

    while q:
        y, x, steps = q.popleft()
        if (y, x) == (MEMORY_SIZE - 1, MEMORY_SIZE - 1):
            return steps

        for (dy, dx) in [(-1, 0), (+1, 0), (0, -1), (0, +1)]:
            next_y, next_x = y + dy, x + dx
            if (
                    0 <= next_y < MEMORY_SIZE and 0 <= next_x < MEMORY_SIZE and
                    memory[next_y][next_x] == '.' and
                    (next_y, next_x) not in visited
            ):
                q.append((next_y, next_x, steps + 1))
                visited.add((next_y, next_x))
    return -1


for line in open('input.txt', 'r'):
    x, y = map(int, line.strip().split(','))
    memory[y][x] = '#'
    steps_needed = bfs()

    failed_byte_count -= 1
    if failed_byte_count == 0:
        print(f'Part-1: {steps_needed}')

    if steps_needed < 0:
        print(f'Part-2: {x},{y}')
        break
