n = int(input('Введите кол-во списочков: '))
lst = []
for i in range(1, n+1):
    lst.append([int(j.strip()) for j in input(f'Введи числа через запятую для {i}-го списка: ').split(',')])
print('Исходный список: ', lst)


def f(l):
    t = ''
    for i in l:
        t += str(i)
    return len(t)


lst = sorted(lst, key=lambda x: f(x))
print('Результат: ', list(map(lambda x: sorted(x, reverse=True), lst)))
