'''Разница в строках одинаковой длины'''
a = 'abc'
b = 'acb'
print(sum([True if a[i] != b[i] else False for i in range(len(a))]))