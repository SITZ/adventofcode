# Problem: https://adventofcode.com/2024/day/22

secret_numbers = list(map(int, open('input.txt', 'r').readlines()))
print(secret_numbers)

final_secret_numbers = []
global_sequence_map = dict()
for secret_number in secret_numbers:
    local_sequence_map = dict()
    local_secret_numbers = [secret_number]
    local_secret_deltas = []

    for i in range(2000):
        secret_number = (secret_number ^ secret_number * 64) % 16777216
        secret_number = (secret_number ^ secret_number // 32) % 16777216
        secret_number = (secret_number ^ secret_number * 2048) % 16777216

        local_secret_deltas.append(secret_number % 10 - local_secret_numbers[-1] % 10)
        local_secret_numbers.append(secret_number % 10)
        if i >= 3:
            local_sequence_hash = tuple(local_secret_deltas[-4:])
            if local_sequence_hash not in local_sequence_map:
                local_sequence_map[local_sequence_hash] = local_secret_numbers[-1] % 10

    for sequence_hash, value in local_sequence_map.items():
        global_sequence_map[sequence_hash] = global_sequence_map.get(sequence_hash, 0) + value

    final_secret_numbers.append(secret_number)

print(f"Part-1:", sum(final_secret_numbers))

print(f"Part-2:", max(global_sequence_map.values()))
