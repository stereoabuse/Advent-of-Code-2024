import re

with open('days/inputs/13') as f:
    input_text = f.read()


regex = r'''Button A: X\+(\d+), Y\+(\d+)
Button B: X\+(\d+), Y\+(\d+)
Prize: X=(\d+), Y=(\d+)'''


for offset in [0, 10000000000000]:
    total = 0
    for config in re.findall(regex, input_text):
        a_x, a_y, b_x, b_y, prize_x, prize_y = map(int,config)
        prize_x += offset
        prize_y += offset
        m = (prize_x * b_y - prize_y * b_x) // (a_x * b_y - a_y * b_x)
        if m * (a_x * b_y - a_y * b_x) != (prize_x * b_y - prize_y * b_x):
            continue
        n = (prize_y - a_y * m) // b_y
        if n * b_y != (prize_y - a_y * m):
            continue

        total += 3 * m + n
    print(total)