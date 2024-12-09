with open('days/inputs/9') as f:
    input_text = f.read()


new = []
id = 0
for i, n in enumerate(input_text):
    if i % 2 == 0:
        new.extend([str(id)] * int(n))
        id += 1
    else:
        new.extend(['.'] * int(n))
        

p1, p2 = 0, len(new) -1 

while p1 < p2:
    if new[p1] == '.' and new[p2] != '.':
        new[p1], new[p2] = new[p2], new[p1]
        p1 += 1
        p2 -= 1
    elif new[p2] == '.':
        p2 -= 1
    else:
        p1 += 1

checksum = 0
for i, char in enumerate(new):
    if char != '.':
        checksum += i * int(char)
print(checksum)
