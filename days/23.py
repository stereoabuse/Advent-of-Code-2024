from collections import defaultdict
from itertools import combinations

with open('days/inputs/23') as f:
    input_text = f.read()


G = defaultdict(list)

for line in input_text.splitlines():
    node1, node2 = line.split('-')
    G[node1].append(node2)
    G[node2].append(node1)


connections = set()

for node1 in G:
    for node2, node3 in combinations(G[node1],2):
        if node1 in G[node2] and node1 in G[node3] and node2 in G[node3]:
            connections.add(tuple(sorted([node1, node2, node3])))

ans = 0
for item in connections:
    if any(computer.startswith('t') for computer in item):
        ans += 1


print(ans)
