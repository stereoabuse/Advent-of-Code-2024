with open('days/inputs/9') as f:
    input_text = f.read()


positions = []
group_id = 0
for position, marker in enumerate(input_text):
    if position % 2 == 0:
        positions.extend([str(group_id)] * int(marker))
        group_id += 1
    else:
        positions.extend(['.'] * int(marker))
        

left_pointer, right_pointer = 0, len(positions) -1 

while left_pointer < right_pointer:
    if '.' == positions[left_pointer] != positions[right_pointer]:
        positions[left_pointer], positions[right_pointer] = positions[right_pointer], positions[left_pointer]
        left_pointer += 1
        right_pointer -= 1
    elif positions[right_pointer] == '.':
        right_pointer -= 1
    else:
        left_pointer += 1

checksum = 0
for position, marker in enumerate(positions):
    if marker != '.':
        checksum += position * int(marker)
print(checksum)
