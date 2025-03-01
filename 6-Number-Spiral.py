"""
Number Spiral

A number spiral is an infinite grid whose upper-left square has number 1. Here are the first five layers of the spiral:

Your task is to find out the number in row y and column x.
Input
The first input line contains an integer t: the number of tests.
After this, there are t lines, each containing integers y and x.
Output
For each test, print the number in row y and column x.

Example
Input:
3
2 3
1 1
4 2

Output:
8
1
15
"""
inp = []
n = int(input())
for _ in range(n):
    inp.append(list(map(int, input().split())))

def numberSpiral(row, col):
    base = (max(row, col))**2 - max(row, col) + 1
    if row >= col:
        addOrSub = 1 if row % 2 == 0 else -1
        return (base + addOrSub * (row - col))
    else:
        addOrSub = -1 if col % 2 == 0 else 1
        return (base + addOrSub * (col - row))

for a,b in inp:
    print(numberSpiral(a, b))
