'''Отбор Максима тернарными операторами'''
x, y = int(input()), int(input())
a1 = x + y
a2 = x - y
a3 = x * y
a4 = x / y
a5 = x // y
result = [a1, a2, a3, a4, a5]
res = a1

if res < a2:
    res = a2
if res < a3:
    res = a3
if res < a4:
    res = a4
if res < a5:
    res = a5


print(f'Максимум {res}')
print(f'Список чисел для удобства: {result}')