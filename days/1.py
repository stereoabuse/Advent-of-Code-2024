from collections import Counter

DAY = '1'

with open(f'src/inputs/{DAY}') as f:
    data = f.readlines()
    L = []
    R = []
    for line in data:
        l, r = [int(x) for x in line.split()]
        L.append(l)
        R.append(r)

L = sorted(L)
R = sorted(R)

distance = 0
for (l,r) in zip(L,R):
    distance += abs(l - r)

# part 1
print(distance)

similarity_score = 0
Rc = Counter(R)

for l in L:
    similarity_score += l * Rc[l]

print(similarity_score)