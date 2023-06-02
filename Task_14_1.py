def recurs(n, res=0):
    if n < 10:
        return 1
    else:
        n //= 10
        return 1 + recurs(n)


print(recurs(abs(int(input('Введите натуральное число: ')))))
