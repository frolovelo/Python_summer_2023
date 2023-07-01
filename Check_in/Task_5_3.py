'''Фибоначчи простая версия'''
n = int(input('Введите число: '))

print(1, end=' ')
a, b = 0, 1
for i in range(n-1):
    new = a + b
    a, b = b, new
    print(new, end=' ')
