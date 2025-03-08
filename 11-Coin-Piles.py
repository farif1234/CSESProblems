"""
Coin Piles

You have two coin piles containing a and b coins. On each move, you can either remove one coin from the left pile and two coins from the right pile, or two coins from the left pile and one coin from the right pile.
Your task is to efficiently find out if you can empty both the piles.
Input
The first input line has an integer t: the number of tests.
After this, there are t lines, each of which has two integers a and b: the numbers of coins in the piles.
Output
For each test, print "YES" if you can empty the piles and "NO" otherwise.

Example
Input:
3
2 1
2 2
3 3

Output:
YES
NO
YES
"""
n = int(input())
answer = []
for _ in range(n):
    a, b = list(map(int, input().split()))
    r = (2 * b - a) / 3
    l = b - 2*r
    answer.append("YES" if (r.is_integer() and r >=
                  0 and l.is_integer() and l >= 0) else "NO")

for a in answer:
    print(a)
