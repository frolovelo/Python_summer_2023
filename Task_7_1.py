def nok(lst):
    if len(lst) == 0:
        return 'Поробуй больше чисел!'
    al = []
    for i in lst:
        d = {}
        for j in range(2, 19):
            while i % j == 0:
                i = i // j
                d[j] = d.get(j, 0) + 1
                if i == 1:
                    break
        al.append(d)
    new = {}
    for i in al:
        for k, v in i.items():
            if new.get(k, 0) < v:
                new[k] = v
    res = 1
    for k, v in new.items():
        res *= k**v
    return res


print(nok([1, 2, 3]))
