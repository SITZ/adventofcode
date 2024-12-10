# Problem: https://adventofcode.com/2024/day/9

disk_map = list(map(int, open('input.txt').readline().strip()))
print('disk_map:\n', disk_map)

disk = []
for i in range(len(disk_map)):
    id = '.' if i % 2 else i // 2
    disk.extend([id] * int(disk_map[i]))
print('disk:\n', disk)


def checksum(disk):
    filesystem_checksum = 0
    for index in range(len(disk)):
        id = 0 if disk[index] == '.' else disk[index]
        filesystem_checksum += index * id
    return filesystem_checksum


def defragment_serial(disk):
    left, right = 0, len(disk) - 1
    while left < right:
        if disk[right] == '.':
            right -= 1
        elif disk[left] != '.':
            left += 1
        else:
            disk[left], disk[right] = disk[right], disk[left]

    return disk


def defragment_block(disk, disk_map):
    disk_map_counter = [0] * len(disk)
    for frequency_index in range(1, len(disk_map), 2):
        disk_map_counter[sum(disk_map[:frequency_index])] = disk_map[frequency_index]

    for frequency_index in range(2 * (len(disk_map) - 1) // 2, -1, -2):
        right_frequency = disk_map[frequency_index]
        right_index = sum(disk_map[:frequency_index])
        for left_index in range(right_index):
            left_frequency = disk_map_counter[left_index]
            if left_frequency >= right_frequency:
                disk[left_index: left_index + right_frequency], disk[right_index: right_index + right_frequency] = disk[right_index: right_index + right_frequency], disk[left_index: left_index + right_frequency]
                disk_map_counter[left_index + right_frequency] = left_frequency - right_frequency
                disk_map_counter[left_index] = 0
                break

    return disk


print('filesystem_checksum_serial:', checksum(defragment_serial(disk.copy())))
print('filesystem_checksum_block:', checksum(defragment_block(disk.copy(), disk_map)))
