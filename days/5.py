import re
from collections import defaultdict

with open('days/inputs/5') as f:
    input_text = f.read()

def integers(s):
    return [int(i) for i in re.split(r'\D+', s)]

rules, updates = [list(map(integers, section.splitlines())) for section in input_text.split('\n\n')]

G = defaultdict(set)
for first, second in rules:
    G[first].add(second)

def validate_sequence(update):
    for i in range(len(update)-1):
        if update[i+1] not in G[update[i]]:
            return False
    return True

middle_pages = 0
for update in updates:
    if validate_sequence(update):
        middle_pages += update[len(update)//2]

print(middle_pages)

