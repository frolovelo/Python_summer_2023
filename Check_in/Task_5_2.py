'''Найти простые множители числа и не только 2**2 * 3**1 = 12'''
n = int(input('Введите положительное число'))
lst = []
print('Простое решение:')
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=' ')
    c = 0
    for k in range(1, i+1):
        if i % k == 0:
            c += 1
    if c == 2:
        lst.append(i)

print()
m = n
d = {}
for i in lst:
    while m % i == 0:
        m = m / i
        d[i] = d.get(i, 0) + 1

print('Сложное решение:')
if len(d) == 0:
    print(f'{n}-{n}')
for key, val in d.items():
    print(f'{key}-{val}')
print('Или:')
print('*'.join(list(map(lambda x: f'({x[0]}**{x[1]})', d.items()))))