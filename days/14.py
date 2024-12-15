import re
from math import prod
from itertools import count

with open('days/inputs/14') as f:
    input_data = f.read()

HEIGHT = 103
WIDTH = 101

for second in count(0):
    seen = set()
    q = [0] * 4
    for line in input_data.splitlines():
        # q = [0] * 4
        px, py, vx, vy = map(int, re.findall(r'-?\d+', line))
        px_1 = (px + (vx * second)) % WIDTH
        py_1 = (py + (vy * second)) % HEIGHT
        seen.add((px_1, py_1))
        if px_1 == WIDTH // 2 or py_1 == HEIGHT // 2:
            continue

        if px_1 < WIDTH // 2 and py_1 < HEIGHT // 2:
            q[0] += 1  
        elif px_1 >= WIDTH // 2 and py_1 < HEIGHT // 2:
            q[1] += 1  
        elif px_1 < WIDTH // 2 and py_1 >= HEIGHT // 2:
            q[2] += 1  
        elif px_1 >= WIDTH // 2 and py_1 >= HEIGHT // 2:
            q[3] += 1  

    if second == 100:
        print(prod(q)) # part 1
    if len(seen) == len(input_data.splitlines()):
        print(second) # part 2
        break