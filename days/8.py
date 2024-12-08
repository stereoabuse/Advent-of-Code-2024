from collections import defaultdict
from itertools import permutations
from math import sqrt

with open('days/inputs/8') as f:
    input_text = f.read()

# input_text = '''............
# ........0...
# .....0......
# .......0....
# ....0.......
# ......A.....
# ............
# ............
# ........A...
# .........A..
# ............
# ............
# '''

antenna_by_location = {}
location_by_antenna = defaultdict(list)

for row_index, row in enumerate(input_text.splitlines()):
    for col_index, char in enumerate(row):
        antenna_by_location[(row_index, col_index)] = char
        location_by_antenna[char].append((row_index, col_index))

possible_locations = set(antenna_by_location)
SEEN = set()

for char, locations in location_by_antenna.items():
    if char != '.':
        # print(char)
        for (x1, y1), (x2, y2) in permutations(locations, 2):
            # print((x1, y1),( x2, y2))
            slope = (y2 - y1)/(x2 - x1)
            dist = sqrt((x2 - x1)**2 + (y2 - y1)**2)

            dx = x2 - x1
            dy = y2 - y1

            x3 = x2 + dx
            y3 = y2 + dy
            if (x3, y3) in possible_locations:
                SEEN.add((x3,y3))

print(len(SEEN))