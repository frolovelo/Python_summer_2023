n = int(input('Введите кол-во списочков: '))
lst = []
for i in range(1, n+1):
    lst.append([int(j.strip()) for j in input(f'Введи числа через запятую для {i}-го списка: ').split(',')])
print('Исходный список: ', lst)


lst = sorted(lst, key=lambda x: len(''.join([str(j) for j in x])))
print('Результат: ', list(map(lambda x: sorted(x, reverse=True), lst)))
