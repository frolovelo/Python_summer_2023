string = input('Введите диапазоны через запятую: ')
lst = [[int(j) for j in i.split('-')] for i in string.split(',')]
print([j for i in lst for j in range(i[0], i[1] + 1)])