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
