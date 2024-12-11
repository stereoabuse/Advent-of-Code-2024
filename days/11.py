with open('days/inputs/11') as f:
    input_text = f.read()

input_text = list(map(int, input_text.split()))
stack = []

for _ in range(25):
    stack = []  
    for num in input_text:
        if num == 0:  
            stack.append(1)
        elif len(str(num)) % 2 == 0:
            num_str = str(num)
            first, second = num_str[:len(num_str)//2], num_str[len(num_str)//2:]
            stack.append(int(first))
            stack.append(int(second))
        else:
            stack.append(num * 2024)
    input_text = stack.copy()  

print(len(stack))
