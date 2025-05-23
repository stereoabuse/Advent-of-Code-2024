import networkx as nx

with open('days/inputs/18') as f:
    input_data = f.read()

data = [map(int, line.split(',')) for line in input_data.split('\n')]
BYTES = 1024
G = nx.grid_2d_graph(71,71)

for i, (x, y) in enumerate(data):
    G.remove_node((x,y))
    if i == BYTES:
        # part 1
        print('p1 answer', nx.shortest_path_length(G, (0,0), (70,70)))
    try:
        nx.shortest_path_length(G, (0,0), (70,70))
    except nx.NetworkXNoPath:
        # part 2
        print(f'{x},{y}')
        break
