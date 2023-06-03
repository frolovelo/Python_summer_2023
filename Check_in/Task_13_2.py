def fun():
    n = 1
    while True:
        if str(n) == str(n)[::-1]:
            yield n
        n += 1


gen = fun()
for i in range(int(input('Сколько членов последовательности вывести: '))):
    print(next(gen), end=', ')