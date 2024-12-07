with open('days/inputs/4') as f:
    input_text = f.read()

grid = input_text.strip().split('\n')

height, width = len(grid), len(grid[0])

grid_dict = {complex(row, col): grid[row][col] for row in 
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
