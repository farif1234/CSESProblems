"""
Gray Code
"""

"""
000 001 010 100 X
001 000 011 101 X
010 011 000 110 X
011 010 001 111 X
100 101 110 000 X
101 100 111 001 X
110 111 100 010 X
111 110 101 011 X
"""


n = int(input())

curr = ['0'] *  n
seen = set()
res = []

while len(seen) < 2 ** n:
    seen.add(''.join(curr))
    res.append(''.join(curr))
    for i, v in enumerate(curr):
        temp = curr[:]
        temp[i] = str(int(not int(v)))
        if ''.join(temp) not in seen:
            curr = temp
            break

for r in res:
    print(r)