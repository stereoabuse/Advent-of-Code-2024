with open('days/inputs/4') as f:
    input_text = f.read()



grid = input_text.strip().split('\n')

height, width = len(grid), len(grid[0])
grid_dict = {complex(row, col): grid[row][col] for row in range(height) for col in range(width)}

directions = [1, -1, 1j, -1j, 1+1j,-1-1j, 1-1j, -1+1j]

xmases = 0
for position in grid_dict:
    for direction in directions:
        if all(grid_dict.get(position + index * direction) == letter for index, letter in enumerate('XMAS')):
            xmases += 1
print(xmases)