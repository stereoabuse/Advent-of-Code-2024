import networkx as nx

with open('days/inputs/10') as f:
    input_text = f.read()


data = {(r,c): char for r, row in enumerate(input_text.splitlines()) for c, char in enumerate(row)}

G = nx.DiGraph()

DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for (x, y) in data:
    for (dx, dy) in DIRS:
        if (x + dx, y + dy) in data:
            current_height = int(data[(x, y)])
            neighbor_height = int(data[(x + dx, y + dy)])
            if neighbor_height == current_height + 1:
                G.add_edge((x, y), (x + dx, y + dy))

trailheads = [(x,y) for (x,y) in data if data[(x,y)] == '0' ]
ends = [(x,y) for (x,y) in data if data[(x,y)] == '9']

path = 0
total = 0
for trailhead in trailheads:
    for end in ends:
        if nx.has_path(G, trailhead, end):
            path += 1
        total += len(list(nx.all_simple_paths(G, trailhead, end)))

print(path, total)
