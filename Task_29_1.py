'''Найти отличающееся число из списка одинаковых чисел'''
lst = [2, 2, 2, 2, 2, 9]
print(min(lst, key=lambda x: lst.count(x)))
