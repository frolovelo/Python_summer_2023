'''Поиск самого длинного палиндрома-подслова'''
t = input('Введите строку: ')


def exp(t, i, j): # s = текст, i = 0, 0, j = 0, 1
    while i >= 0 and j < len(t) and t[i] == t[j]:
        i -= 1
        j += 1
    return t[i + 1:j]


def helpme(t):
    res = ''
    for i in range(len(t)):
        res = max(res, exp(t, i, i), exp(t, i, i + 1), key=len)
    return res


res = helpme(t)
print(f'Длина: {len(res)}, палиндром: {res}')
