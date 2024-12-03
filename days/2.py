from itertools import pairwise

with open('days/inputs/2') as f:
    data = [[int(x) for x in line.strip().split()] for line in f.readlines()]

def is_valid(line):
    ascending_or_descending = (line == sorted(line) or line == sorted(line, reverse=True))
    return ascending_or_descending and all(1 <= abs(a - b) <= 3 for (a,b) in pairwise(line))

# part 1
print(sum(1 for line in data if is_valid(line)))

# part 2
safe_report = 0
for full_line in data:
    works = False
    for i in range(len(full_line)): 
        line = full_line[:i] + full_line[i+1:]
        if is_valid(line):
            works = True
    if works:
        safe_report += 1
print(safe_report)
