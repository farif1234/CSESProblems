"""
Repetitions

You are given a DNA sequence: a string consisting of characters A, C, G, and T. Your task is to find the longest repetition in the sequence. This is a maximum-length substring containing only one type of character.
Input
The only input line contains a string of n characters.
Output
Print one integer: the length of the longest repetition.

Example
Input:
ATTCGGGA

Output:
3
"""

seq = input()

curr = seq[0]
count = 0
maxCount = 0
for char in seq:
    if char == curr:
        count += 1
        maxCount = max(maxCount, count)
    else:
        curr = char
        count = 1

print(maxCount)