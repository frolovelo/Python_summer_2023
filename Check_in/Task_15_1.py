d = {4: 1, 3: {4: 3, 3: {1: 6, 3: 1}, 2: 3}, 2: {1: 4}, 1: {2: 6}, 5: 2}

def rec(d, key):
    res = []
    for k, v in d.items():
        if key == k:
            res.append(v)
        if type(v) == dict:
            res.extend((rec(v, key)))
    return res


k = int(input('Введите ключик: '))
print(rec(d, k))

