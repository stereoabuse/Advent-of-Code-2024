from itertools import combinations

def gridify(schematic):
    return {(r,c): char for r, row in enumerate(schematic) for c, char in enumerate(row)}

with open('days/inputs/25') as f:
    schematics = [gridify(schematic) for schematic in f.read().split('\n\n')]

total = 0
for (a, b) in combinations(schematics,2):
    works = True
    for x, y in zip(a.values(), b.values()):
        if x == y == '#':
            works = False
    if works:
        total += 1
print(total)