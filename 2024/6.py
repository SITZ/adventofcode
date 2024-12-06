map = open("input.txt", "r").readlines()
map = [list(row.strip()) for row in map]

[print(''.join(row)) for row in map]

rows, cols = len(map), len(map[0])
directions = ['^', '>', 'v', '<']
moves = [(-1, 0), (0, +1), (+1, 0), (0, -1)]
exits = [(0, None), (None, cols - 1), (rows - 1, None), (None, 0)]

start_i, start_j, start_direction = -1, -1, ''

for i in range(rows):
    for j in range(cols):
        if map[i][j] in directions:
            start_i, start_j, start_direction = i, j, map[i][j]
            break
    if start_direction:
        break


def traverse_positions(map):
    has_left = False
    position_i, position_j, position_direction = start_i, start_j, start_direction
    positions_visited = set()
    states_visited = set()

    while not has_left:
        positions_visited.add((position_i, position_j))

        current_state = (position_i, position_j, position_direction)
        if current_state in states_visited:
            return -1
        states_visited.add(current_state)

        for index in range(len(directions)):
            if position_direction == directions[index]:
                if (exits[index][0] in [None, position_i]) and (exits[index][1] in [None, position_j]):
                    has_left = True
                    break

                elif map[position_i + moves[index][0]][position_j + moves[index][1]] == '#':
                    position_direction = directions[(index + 1) % len(directions)]

                else:
                    position_i += moves[index][0]
                    position_j += moves[index][1]

    return len(positions_visited)


print('traversed_positions', traverse_positions(map))


def count_obstruction_positions(map):
    loop_positions = set()

    for i in range(rows):
        for j in range(cols):
            if map[i][j] == '.' and (i, j) != (start_i, start_j):
                map[i][j] = '#'
                if traverse_positions(map) == -1:
                    loop_positions.add((i, j))
                map[i][j] = '.'

    return len(loop_positions)


print('obstruction_positions', count_obstruction_positions(map))
