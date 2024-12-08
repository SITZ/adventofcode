# Problem: https://adventofcode.com/2024/day/8

map = open("input.txt", "r").readlines()
map = [row.strip() for row in map]
print(map)


def get_antinode_locations(extend_line=False):
    antinode_locations = set()
    for x1 in range(len(map)):
        for y1 in range(len(map[0])):
            if map[x1][y1] == '.':
                continue

            for x2 in range(len(map)):
                for y2 in range(len(map[0])):
                    if (x1, y1) == (x2, y2) or map[x1][y1] != map[x2][y2]:
                        continue

                    delta_x, delta_y = x1 - x2, y1 - y2
                    if extend_line:
                        antinode_locations.add((x1, y1))
                        antinode_locations.add((x2, y2))

                    antinode_x1, antinode_y1 = x1 + delta_x, y1 + delta_y
                    while 0 <= antinode_x1 < len(map) and 0 <= antinode_y1 < len(map[0]):
                        antinode_locations.add((antinode_x1, antinode_y1))
                        antinode_x1, antinode_y1 = antinode_x1 + delta_x, antinode_y1 + delta_y
                        if not extend_line:
                            break

                    antinode_x2, antinode_y2 = x2 - delta_x, y2 - delta_y
                    while 0 <= antinode_x2 < len(map) and 0 <= antinode_y2 < len(map[0]):
                        antinode_locations.add((antinode_x2, antinode_y2))
                        antinode_x2, antinode_y2 = antinode_x2 - delta_x, antinode_y2 - delta_y
                        if not extend_line:
                            break

    return len(antinode_locations)


print('pair_antinode_locations', get_antinode_locations(extend_line=False))
print('all_antinode_locations ', get_antinode_locations(extend_line=True))
