import networkx as nx
from collections import Counter

with open('days/inputs/20') as f:
    input_text = f.read()

data_basic = {(r, c): char for r, row in enumerate(input_text.splitlines()) for c, char in enumerate(row)}

ans = []
total_locations = len(data_basic)

for i, location in enumerate(data_basic):
    if i % 100 == 0:
        print(f"Progress: {i}/{total_locations} ({(i/total_locations*100):.1f}%)")
    try:
        data = {(r, c): char for r, row in enumerate(input_text.splitlines()) for c, char in enumerate(row)}
        data[location] = '.'
        G = nx.Graph()

        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for (x, y) in data:
            if data[(x, y)] != '#':
                for (dx, dy) in DIRS:
                    next_pos = (x + dx, y + dy)
                    if next_pos in data and data[next_pos] != '#':
                        G.add_edge((x, y), next_pos)

        START = [(x,y) for (x,y) in data if data[(x,y)] == 'S'][0]
        END = [(x,y) for (x,y) in data if data[(x,y)] == 'E'][0]

        ans.append(nx.shortest_path_length(G, START, END))
    except IndexError:
        continue

MAX = max(ans)
c = Counter(MAX - a for a in ans)

print(sum(v for k,v in c.items() if 100 <= k)) # insanely slow