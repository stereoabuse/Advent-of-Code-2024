from collections import defaultdict
import re

with open('days/inputs/24') as f:
    input_text = f.read()

wire_values, connections = input_text.split('\n\n')

conn_dict = defaultdict(bool)

for line in wire_values.splitlines():
    wire, value = line.split(': ')
    conn_dict[wire] = bool(int(value))

connections = connections.splitlines()
while connections:
    for line in connections:
        a, op, b, c = re.findall(r'[a-z0-9A-Z]{2,3}', line)
        if a in conn_dict and b in conn_dict:
            if op == 'AND':
                conn_dict[c] = conn_dict[a] & conn_dict[b]
            elif op == 'OR':
                conn_dict[c] = conn_dict[a] | conn_dict[b]
            elif op == 'XOR':
                conn_dict[c] = conn_dict[a] ^ conn_dict[b]
            else:
                print('problem')
            connections.remove(line)
            break

ans = ''
for wire in sorted(conn_dict.keys()):
    if wire.startswith('z'):
        ans += str(int(conn_dict[wire]))

print(int(ans[::-1],2))