"""
Trailing Zeros

Your task is to calculate the number of trailing zeros in the factorial n!.
For example, 20!=2432902008176640000 and it has 4 trailing zeros.
Input
The only input line has an integer n.
Output
Print the number of trailing zeros in n!.

Example
Input:
20

Output:
4
"""
# 10 -> 1, 2, 5, 10

n = int(input())
count = 0 
curr = 5

while curr <= n:
    count += n // curr
    curr *= 5

print(count)