"""
Palindrome Reorder

Given a string, your task is to reorder its letters in such a way that it becomes a palindrome (i.e., it reads the same forwards and backwards).
Input
The only input line has a string of length n consisting of characters A-Z.
Output
Print a palindrome consisting of the characters of the original string. You may print any valid solution. If there are no solutions, print "NO SOLUTION".

Example
Input:
AAAACACBA

SQAADSDTQ
ADQSTSQDA


Output:
AACABACAA
"""
s = input()

count = [0] * 26

for char in s:
    count[ord(char) - ord('A')] += 1

numOfOdds = 0
for i, c in enumerate(count):
    if c % 2 != 0:
        numOfOdds += 1

if (len(s) % 2 == 0 and numOfOdds > 0) or (numOfOdds > 1):
    print("NO SOLUTION")
else:
    res = [''] * len(s)
    resI = 0
    for i, c in enumerate(count):
        letter = chr(i + ord('A'))
        if c % 2 == 0:
            for _ in range(c // 2):
                res[resI] = letter
                res[len(res) - 1 - resI] = letter
                resI += 1
        else:
            mid = len(s) // 2

            res[mid - c // 2 : mid + 1 + c // 2] = [letter] * c


    print(''.join(res))