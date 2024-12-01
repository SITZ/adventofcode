from collections import Counter

left_location_ids = []
right_location_ids = []

for line in open('input.txt'):
    left, right = map(int, line.strip().split())
    # print(left, right)
    left_location_ids.append(left)
    right_location_ids.append(right)

# print(left_location_ids)
# print(right_location_ids)

left_location_ids.sort()
right_location_ids.sort()

total_distance_between_lists = sum(abs(left - right) for left, right in zip(left_location_ids, right_location_ids))
print(total_distance_between_lists)

right_location_counter = Counter(right_location_ids)

total_similarity_score = 0
for left_location_id in left_location_ids:
    total_similarity_score += left_location_id * right_location_counter[left_location_id]
print(total_similarity_score)