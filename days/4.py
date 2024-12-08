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


x = {1+1j: 'M', -1-1j: 'S', 1-1j:'S', -1+1j:'M'}
x_rev = {1+1j: 'S', -1-1j: 'M', 1-1j:'M', -1+1j:'S'}

cross_count = 0
grid_positions = list(grid_dict.keys())
for position in grid_positions:
    if grid_dict[position] == 'A':
        diag1 = all(grid_dict.get(position + d) == x[d] for d in [1+1j, -1-1j])
        diag1_flip = all(grid_dict.get(position + d) == x_rev[d] for d in [1+1j, -1-1j])
        
        diag2 = all(grid_dict.get(position + d) == x[d] for d in [1-1j, -1+1j])
        diag2_flip = all(grid_dict.get(position + d) == x_rev[d] for d in [1-1j, -1+1j])
        
        if (diag1 or diag1_flip) and (diag2 or diag2_flip):
            cross_count += 1

# part 2
print(cross_count)