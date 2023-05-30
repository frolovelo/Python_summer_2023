def fun():
    n = 1
    k = -2
    while True:
        yield n
        n += 2
        yield k
        k -= 2


gen = fun()
for i in range(int(input('Сколько членов последовательности вывести: '))):
    print(next(gen), end=', ')
