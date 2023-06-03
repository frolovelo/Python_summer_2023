def fun(n, delim=0):
    if n > delim:
        delim = n
    if n == 0:
        return
    else:
        print(f"{'* ' * n:^{delim*2}}")
        fun(n-1, delim)
        if n != 1:
            print(f"{'* ' * n:^{delim*2}}")


fun(abs(int(input('Введите натуральное число: '))))
