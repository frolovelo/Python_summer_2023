def recurs(n):
    if n < 10:
        return n
    else:
        n, n10 = divmod(n, 10) # при 123, n = 12, n10 = 3
        return n10 + recurs(n)


print(recurs(abs(int(input('Введите натуральное число: ')))))
