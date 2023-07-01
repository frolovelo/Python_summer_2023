'''Факториал циклом for'''
from math import *
n = int(input())
f = 1
for i in range(1, n+1):
    f *= i
print(f'Цикл выдал факториал: {f}')
print(f'Модуль math: {factorial(n)}')