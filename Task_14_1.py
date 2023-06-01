def recurs(n, res=0):
    if n == 0:
        return res
    else:
        n //= 10
        res += 1
        return recurs(n, res)


print(recurs(abs(int(input('Введите натуральное число: ')))))
