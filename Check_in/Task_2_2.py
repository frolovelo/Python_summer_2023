'''Поиск min тернарными операторами'''
from random import *
lst = [randint(1,50) for i in range(10)]
m = lst[0]
for i in lst[1:]:
    if i < m:
        m = i
print(f'Минимум: {m} из списка {lst}')
print(f'Функция min: {min(lst)}')