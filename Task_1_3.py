x, y = int(input()), int(input())
a1 = x + y
a2 = x - y
a3 = x * y
a4 = x / y
a5 = x // y
result = [a1, a2, a3, a4, a5]
res1 = -10000
res = a1
if a2 > res:
    res = a2
if a3 > res:
    res = a3
if a4 > res:
    res = a4
if a5 > res:
    res = a5

if res1 < a1 < res:
    res1 = a1
if res1 < a2 < res:
    res1 = a2
if res1 < a2 < res:
    res1 = a2
if res1 < a3 < res:
    res1 = a3
if res1 < a4 < res:
    res1 = a4
if res1 < a5 < res:
    res1 = a5
print('Второй максимум:', res1)
print(f'Список чисел для удобства проверки: {result}')
