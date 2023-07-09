'''Ханойская башня'''


def bashya(n, s2=1, s3=2):
    c = 0
    if n == 1:
        return 1
    else:
        c += bashya(n - 1, s2, 6 - s2 - s3) + 1
        c += bashya(n - 1, 6 - s2 - s3, s3)
    return c


n = int(input("Введите кол-во дисков: "))
print(bashya(n))
