'''Подсчёт количества цифр в числе'''
n = int(input('Введите число: '))
n = str(n)
lst = [str(i) for i in range(10)]
for i in lst:
    print(f'{i} - {n.count(i)}')
