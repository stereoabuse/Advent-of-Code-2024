from collections import defaultdict
from itertools import permutations

with open('days/inputs/8') as f:
    input_text = f.read()

antenna_by_location = set()
location_by_antenna = defaultdict(list)

for row_index, row in enumerate(input_text.splitlines()):
    for col_index, char in enumerate(row):
        antenna_by_location.add((row_index, col_index))
        location_by_antenna[char].append((row_index, col_index))

SEEN_1, SEEN_2 = set(), set()

for char, locations in location_by_antenna.items():
    if char != '.':
        for (x1, y1), (x2, y2) in permutations(locations, 2):

            dx = x2 - x1
            dy = y2 - y1

            x3 = x2 + dx
            y3 = y2 + dy
            
            if (x3, y3) in antenna_by_location:
                SEEN_1.add((x3,y3))

            for i in range(0, len(row)):
                x3 = x2 + dx * i
                y3 = y2 + dy * i
                if (x3, y3) in antenna_by_location:
                    SEEN_2.add((x3,y3))

print(len(SEEN_1))

print(len(SEEN_2))