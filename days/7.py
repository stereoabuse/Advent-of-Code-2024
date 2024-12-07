import re
from operator import mul, add
from itertools import product, cycle
from functools import reduce

with open('days/inputs/7') as f:
    input_text = f.read()

def integers(s):
    return [int(i) for i in re.split(r'\D+', s)]


total = 0
for row in input_text.splitlines():
    target, *sequence = integers(row)
    for operations in product([mul, add], repeat=len(sequence)-1):
        ops = cycle(operations)
        result = reduce(lambda x, y: next(ops)(x,y), sequence)
        if result == target:
            total += result
            break
# part 1
print(total)