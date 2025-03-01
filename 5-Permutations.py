"""
Permutations

A permutation of integers 1,2,\ldots,n is called beautiful if there are no adjacent elements whose difference is 1.
Given n, construct a beautiful permutation if such a permutation exists.
Input
The only input line contains an integer n.
Output
Print a beautiful permutation of integers 1,2,\ldots,n. If there are several solutions, you may print any of them. If there are no solutions, print "NO SOLUTION".

Example 1
Input:
5

Output:
4 2 5 3 1
Example 2
Input:
3

Output:
NO SOLUTION
"""

n = int(input())
if n == 1:
    print('1')
elif n <= 3:
    print('NO SOLUTION')
else:
    resE = [2*i for i in range(1, (n // 2) + 1)]
    resO = [2*i - 1 for i in range(1, (n // 2) + 1)]
    if n % 2 == 1:
        resO.append(n)
    res = resE + resO
    print(*res)
