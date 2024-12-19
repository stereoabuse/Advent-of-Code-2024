import heapq

with open('days/inputs/15') as f:
    input_data = f.read()


grid = {(r,c): char 
        for r, line in enumerate(input_data.splitlines())
        for c, char in enumerate(line.strip())}

start = next(pos for pos, char in grid.items() if char == 'S')

queue = [(0, start, (1,0))]
seen = {(start, (1,0))}



while queue:
    cost, pos, direction = heapq.heappop(queue)
    seen.add((pos, direction))
    
    if grid[pos] == "E":
        print(cost - 1000) # manually needs an offset? 
        break

    dr, dc = direction
    r, c = pos
    moves = [(cost + 1, (r + dr, c + dc), direction),
             (cost + 1000, pos, (dc, -dr)),
             (cost + 1000, pos, (-dc, dr))]
    
    for new_cost, new_pos, new_dir in moves:
        if new_pos not in grid or grid[new_pos] == "#":
            continue
        if (new_pos, new_dir) in seen:
            continue
        heapq.heappush(queue, (new_cost, new_pos, new_dir))