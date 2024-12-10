import re

with open('days/inputs/3') as f:
    input_text = f.read()

def calculate_multiplications(text):
    multiplication_pairs = re.findall(r'mul\((\d+),(\d+)\)', text)
    return sum(int(a) * int(b) for a, b in multiplication_pairs)

# part 1
print(calculate_multiplications(input_text))

# part 2
allowed_sections = re.split(r"don't\(\).*?(?=do\(\))", input_text, flags=re.DOTALL)
total_sum = 0
for section in allowed_sections:
    total_sum += calculate_multiplications(section)

print(total_sum)