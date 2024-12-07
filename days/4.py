from collections import defaultdict

with open('days/inputs/4') as f:
    input_text = f.read()


grid = input_text.strip().split('\n')

height, width = len(grid), len(grid[0])

grid_dict = defaultdict(complex) | {complex(row, col): grid[row][col] for row in 
                                    range(height) for col in range(width)}

directions = [1, -1, 1j, -1j, 1+1j,-1-1j, 1-1j, -1+1j]

xmases = 0
for pos in grid_dict:
    for dir in directions:
        if all(grid_dict.get(pos + i * dir) == char 
               for i, char in enumerate('XMAS')):
            xmases += 1
# part 1
print(xmases)


x_shape = {1+1j: 'M', -1-1j: 'S', 1-1j:'S', -1+1j:'M'}
x_shape_reverse = {1+1j: 'S', -1-1j: 'M', 1-1j:'M', -1+1j:'S'}

cross_count = 0
grid_positions = list(grid_dict.keys())
for position in grid_positions:
    if grid_dict[position] == 'A':
        diagonal1_matches = all(grid_dict.get(position + d) == x_shape[d] for d in [1+1j, -1-1j])
        diagonal1_matches_flipped = all(grid_dict.get(position + d) == x_shape_reverse[d] for d in [1+1j, -1-1j])
        
        diagonal2_matches = all(grid_dict.get(position + d) == x_shape[d] for d in [1-1j, -1+1j])
        diagonal2_matches_flipped = all(grid_dict.get(position + d) == x_shape_reverse[d] for d in [1-1j, -1+1j])
        
        if (diagonal1_matches or diagonal1_matches_flipped) and (diagonal2_matches or diagonal2_matches_flipped):
            cross_count += 1

# part 2
print(cross_count)