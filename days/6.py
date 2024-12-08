input_text = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''

# with open('days/inputs/6') as f:
#     input_text = f.read()

G = {(r, c): char for r, line in enumerate(input_text.splitlines()) for c, char in enumerate(line)}

current = [key for key, value in G.items() if value == '^'][0]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
direction_index = 0
visited = set()

while current in G:
    next_current = tuple(v1 + v2 for v1, v2 in zip(current, directions[direction_index % 4]))
    if next_current in G:
        if G[next_current] == '#':
            direction_index += 1
            next_current = tuple(v1 + v2 for v1, v2 in zip(current, directions[direction_index % 4]))
            current = next_current
            visited.add(current)
        else:
            current = next_current
            visited.add(current)


    else:
        break


# part 1
print(len(visited))

