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