"""
Two Knights

Your task is to count for k=1,2,\ldots,n the number of ways two knights can be placed on a k \times k chessboard so that they do not attack each other.
Input
The only input line contains an integer n.
Output
Print n integers: the results.

Example
Input:
8

Output:
0
6
28
96
252
550
1056
1848
"""
k = int(input())

def twoKnights(k):
    total = (k ** 2 * (k ** 2 - 1)) // 2
    if k <= 2:
        invalid = 0
    else:
        k -= 2
        invalid = 8 * (k * (k+1) // 2)
    return total - invalid

for i in range(1, k+1):
    print(twoKnights(i))