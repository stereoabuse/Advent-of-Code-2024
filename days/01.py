from collections import Counter

with open('days/inputs/1') as f:
    data = f.readlines()
    group1_locations, group2_locations = [], []
    for line in data:
        loc1, loc2 = [int(x) for x in line.split()]
        group1_locations.append(loc1)
        group2_locations.append(loc2)

group1_locations, group2_locations = sorted(group1_locations), sorted(group2_locations)

total_distance = 0
for (loc1, loc2) in zip(group1_locations, group2_locations):
    total_distance += abs(loc1 - loc2)

# part 1
print(total_distance)

# part 2
similarity_score = 0
group2_counts = Counter(group2_locations)

for location in group1_locations:
    similarity_score += location * group2_counts[location]

print(similarity_score)