def nok(lst):
    if len(lst) == 0:
        return 'Поробуй больше чисел!'
    if 0 in lst:
        return 0
    al = []
    for i in lst:
        d = {}
        i = abs(i)
        for j in range(2, i+10):
            while i % j == 0:
                i = i // j
                d[j] = d.get(j, 0) + 1
                if i == 1:
                    break
        al.append(d)
    print(al)
    new = {}
    for i in al:
        for k, v in i.items():
            if new.get(k, 0) < v:
                new[k] = v
    res = 1
    for k, v in new.items():
        res *= k**v
    return res


from math import *
l = [5, -45, 43, 6]
print('Моя функция:', nok(l))
print('Модуль math:', lcm(*l))
