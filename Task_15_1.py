d = {4: 1, 3: {4: 3, 3: {1: 6, 3: 1}, 2: 3}, 2: {1: 4}, 1: {2: 6}, 5: 2}
res = []

def rec(d, key):
    for k, v in d.items():
        if type(v) == dict:
            rec(v, key)
        elif key == k:
            res.append(v)

k = int(input('Введите ключик: '))
rec(d, k)
print(res if len(res) != 0 else f'Значений по ключу "{k}" не найдено!')
