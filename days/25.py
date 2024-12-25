with open('days/inputs/25') as f:
    schematics = f.read().split('\n\n')

locks, keys = [], []

def gridify(schematic):
    return {(r,c): char for r, row in enumerate(schematic) 
                        for c, char in enumerate(row)}

for schematic in schematics:
    schematic = schematic.splitlines()
    if all(char == '#' for char in schematic[0]):
        locks.append(gridify(schematic))
    else:
        keys.append(gridify(schematic))

total = 0
for key in keys:
    for lock in locks:
        works = True
        for key_char, lock_char in zip(key.values(), lock.values()):
            if key_char == '#' and lock_char == '#':
                works = False
                break
        if works:
            total += 1
print(total)