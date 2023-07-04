'''Рекурсия, подсчёт кол-ва элементов списка списков'''
def recurs(lst):
    res = 0
    if len(lst) == 0:
        return 0
    for i in lst:
        if isinstance(i, list):
            res += recurs(i) + 1
        else:
            res += 1
    return res


lst = [1, 2, 3, [4, [5]]]
print(lst, recurs(lst))
