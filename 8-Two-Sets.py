"""
Two Sets

Your task is to divide the numbers 1,2,\ldots,n into two sets of equal sum.
Input
The only input line contains an integer n.
Output
Print "YES", if the division is possible, and "NO" otherwise.
After this, if the division is possible, print an example of how to create the sets. First, print the number of elements in the first set followed by the elements themselves in a separate line, and then, print the second set in a similar way.

Example 1
Input:
7

Output:
YES
4
1 2 4 7
3
3 5 6
Example 2
Input:
6

Output:
NO
"""
n = int(input())

total = (n * (n + 1) // 2)
if total % 2 != 0 or n <= 2:
    print("NO")
else:
    print("YES")
    res = []
    sm = 0
    for i in range(n, 0,-1):
        sm += i
        res.append(i)
        if total // 2 - sm < i:
            if total // 2 - sm > 0:
                res.append(total //2 - sm)
            break
    print(len(res))
    print(*res)
    res = set(res)
    other = [i for i in range(1, n+1) if i not in res]
    print(len(other))
    print(*other)
