n = input()
n = int(n)
res = [str(n)]

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = n*3 + 1
    res.append(str(n))

print(' '.join(res))