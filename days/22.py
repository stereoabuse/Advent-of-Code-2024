import re

with open('days/inputs/22') as f:
    nums = map(int, re.findall(r'\d+', f.read(), re.MULTILINE))

def next_secret(num):
    def mix(num, value):
        return num ^ value
    def prune(num):
        return num  % 16777216
    num = prune(mix(num, num * 64))
    num = prune(mix(num, num // 32))
    num = prune(mix(num, num * 2048))
    return num

ans = 0
for num in nums:
    for _ in range(2000):
        num = next_secret(num)
    ans += num

print(ans)
