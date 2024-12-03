from itertools import pairwise

with open('days/inputs/2') as f:
    data = [[int(x) for x in line.strip().split()] for line in f.readlines()]


# part 1
safe_report = 0
for line in data:
    ascending_or_descending = (line == sorted(line) or line == sorted(line, reverse=True))
    if ascending_or_descending:
        if all(1 <= abs(a - b) <= 3 for (a,b) in pairwise(line)):
            safe_report += 1
print(safe_report)

# part 2

safe_report = 0
for full_line in data:
    works = []
    for i in range(len(full_line)): 
        line = full_line[:i] + full_line[i+1:]
        ascending_or_descending = (line == sorted(line) or line == sorted(line, reverse=True))
        if ascending_or_descending:
            if all(1 <= abs(a - b) <= 3 for (a,b) in pairwise(line)):
                works.append(True)
                break
    if any(works):
        safe_report += 1
print(safe_report)
