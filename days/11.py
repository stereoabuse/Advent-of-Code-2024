from functools import cache
from copy import deepcopy

with open('days/inputs/11') as f:
    input_text = f.read()

input_text = map(int, input_text.split())

p1_in = deepcopy(input_text)
for _ in range(25):
    stack = []  
    for num in p1_in:
        if num == 0:  
            stack.append(1)
        elif len(str(num)) % 2 == 0:
            num_str = str(num)
            first, second = num_str[:len(num_str)//2], num_str[len(num_str)//2:]
            stack.append(int(first))
            stack.append(int(second))
        else:
            stack.append(num * 2024)
    p1_in = stack.copy()  

# part 1
print(len(stack))

@cache
def calculate(num, day=75):
    if day == 0:
        return 1
    if num == 0:
        return calculate(1, day-1)

    num_str = str(num)
    if len(num_str) % 2 == 0:
        mid = len(num_str) // 2
        left = int(num_str[:mid]) 
        right = int(num_str[mid:])
        return calculate(left, day-1) + calculate(right, day-1)
    else:
        return calculate(num * 2024, day-1)

# part 2
print(sum(map(calculate, input_text)))