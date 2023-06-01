def recurs(n, res=0):
    if n == 0:
        return res
    else:
        res += n % 10
        n //= 10
        return recurs(n, res)


print(recurs(abs(int(input('Введите натуральное число: ')))))
