from itertools import pairwise

with open('days/inputs/2') as f:
    reports = [[int(x) for x in report.strip().split()] for report in f.readlines()]

def is_safe_report(line):
    monotonic = (line == sorted(line) or line == sorted(line, reverse=True))
    return monotonic and all(1 <= abs(a - b) <= 3 for (a,b) in pairwise(line))

# part 1
print(sum(1 for line in reports if is_safe_report(line)))

# part 2
safe_with_dampener = 0
for full_report in reports:
    safety = False
    for i in range(len(full_report)): 
        dampened = full_report[:i] + full_report[i+1:]
        if is_safe_report(dampened):
            safety = True
    if safety:
        safe_with_dampener += 1
print(safe_with_dampener)
