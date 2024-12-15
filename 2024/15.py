# Problem: https://adventofcode.com/2024/day/15
from copy import deepcopy

lines = [line.strip() for line in open("input.txt", "r").readlines()]


def print_warehouse(warehouse):
    print('\n'.join([''.join(warehouse[i]) for i in range(len(warehouse))]))


original_warehouse = [list(line) for line in lines[:lines.index('')]]
print(original_warehouse)

moves = ''.join(lines[lines.index(''):])
print(moves)


def total_gps_sum(warehouse, box):
    gps_sum = 0
    for i in range(0, len(warehouse) - 1):
        for j in range(0, len(warehouse[i]) - 1):
            if warehouse[i][j] == box:
                gps_sum += 100 * i + j

    return gps_sum


def get_robot_position(warehouse):
    for i in range(len(warehouse)):
        for j in range(len(warehouse[i])):
            if warehouse[i][j] == '@':
                return i, j


def part_1(warehouse):
    robot_i, robot_j = get_robot_position(warehouse)
    max_i, max_j = len(warehouse), len(warehouse[0])

    for move in moves:
        match move:
            case '>':
                for j in range(robot_j + 1, max_j - 1, +1):
                    if warehouse[robot_i][j] == '#':
                        break
                    if warehouse[robot_i][j] == '.':
                        warehouse[robot_i][j] = warehouse[robot_i][j - 1]
                        warehouse[robot_i][robot_j + 1] = '@'
                        warehouse[robot_i][robot_j] = '.'
                        robot_j += 1
                        break

            case '<':
                for j in range(robot_j - 1, 0, -1):
                    if warehouse[robot_i][j] == '#':
                        break
                    if warehouse[robot_i][j] == '.':
                        warehouse[robot_i][j] = warehouse[robot_i][j + 1]
                        warehouse[robot_i][robot_j - 1] = '@'
                        warehouse[robot_i][robot_j] = '.'
                        robot_j -= 1
                        break

            case 'v':
                for i in range(robot_i + 1, max_i, +1):
                    if warehouse[i][robot_j] == '#':
                        break
                    if warehouse[i][robot_j] == '.':
                        warehouse[i][robot_j] = warehouse[i - 1][robot_j]
                        warehouse[robot_i + 1][robot_j] = '@'
                        warehouse[robot_i][robot_j] = '.'
                        robot_i += 1
                        break

            case '^':
                for i in range(robot_i - 1, 0, -1):
                    if warehouse[i][robot_j] == '#':
                        break
                    if warehouse[i][robot_j] == '.':
                        warehouse[i][robot_j] = warehouse[i + 1][robot_j]
                        warehouse[robot_i - 1][robot_j] = '@'
                        warehouse[robot_i][robot_j] = '.'
                        robot_i -= 1
                        break

        # print(move, warehouse)

    return warehouse


print('total_gps_sum_part1', total_gps_sum(part_1(deepcopy(original_warehouse)), 'O'))


def scale_warehouse(warehouse):
    scaled_warehouse = []
    for line in warehouse:
        row = []
        for tile in line:
            match tile:
                case '#':
                    row += ['#', '#']
                case 'O':
                    row += ['[', ']']
                case '.':
                    row += ['.', '.']
                case '@':
                    row += ['@', '.']
        scaled_warehouse.append(row)
    # print_warehouse(scaled_warehouse)
    return scaled_warehouse


def part_2(warehouse):
    robot_i, robot_j = get_robot_position(warehouse)
    max_i, max_j = len(warehouse), len(warehouse[0])

    for move in moves:
        match move:
            case '>':
                for j in range(robot_j + 1, max_j - 1, +1):
                    if warehouse[robot_i][j] == '#':
                        break
                    if warehouse[robot_i][j] == '.':
                        warehouse[robot_i][robot_j + 1:j + 1] = warehouse[robot_i][robot_j:j]
                        warehouse[robot_i][robot_j] = '.'
                        robot_j += 1
                        break

            case '<':
                for j in range(robot_j - 1, 0, -1):
                    if warehouse[robot_i][j] == '#':
                        break
                    if warehouse[robot_i][j] == '.':
                        warehouse[robot_i][j:robot_j] = warehouse[robot_i][j + 1:robot_j + 1]
                        warehouse[robot_i][robot_j] = '.'
                        robot_j -= 1
                        break

            case 'v':
                levels = {robot_i: {robot_j}}
                for i in range(robot_i + 1, max_i - 1, +1):
                    levels[i] = set()
                    level_has_box = False
                    level_has_wall = False

                    for j in levels[i - 1]:
                        if warehouse[i][j] == '#':
                            level_has_wall = True
                            break

                        if warehouse[i][j] == '[':
                            levels[i].update({j, j + 1})
                            level_has_box = True
                        elif warehouse[i][j] == ']':
                            levels[i].update({j, j - 1})
                            level_has_box = True

                    if level_has_wall:
                        break

                    if level_has_box:
                        continue

                    for reverse_i in range(i, robot_i, -1):
                        for j in levels[reverse_i - 1]:
                            warehouse[reverse_i][j] = warehouse[reverse_i - 1][j]
                            warehouse[reverse_i - 1][j] = '.'

                    warehouse[robot_i][robot_j] = '.'
                    robot_i += 1
                    break

            case '^':
                levels = {robot_i: {robot_j}}
                for i in range(robot_i - 1, 0, -1):
                    levels[i] = set()
                    level_has_box = False
                    level_has_wall = False

                    for j in levels[i + 1]:
                        if warehouse[i][j] == '#':
                            level_has_wall = True
                            break

                        if warehouse[i][j] == '[':
                            levels[i].update({j, j + 1})
                            level_has_box = True
                        elif warehouse[i][j] == ']':
                            levels[i].update({j, j - 1})
                            level_has_box = True

                    if level_has_wall:
                        break

                    if not level_has_box:
                        for reverse_i in range(i, robot_i, +1):
                            for j in levels[reverse_i + 1]:
                                warehouse[reverse_i][j] = warehouse[reverse_i + 1][j]
                                warehouse[reverse_i + 1][j] = '.'

                        warehouse[robot_i][robot_j] = '.'
                        robot_i -= 1
                        break

        # print(move)
        # print_warehouse(warehouse)

    return warehouse


print('total_gps_sum_part2', total_gps_sum(part_2(scale_warehouse(deepcopy(original_warehouse))), '['))
