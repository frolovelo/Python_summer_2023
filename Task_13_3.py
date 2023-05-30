def fun(lst):
    for i in lst:
        if i % 2 != 0:
            yield i


lst = [int(i) for i in input('Введите числа через пробел: ').split()]
gen = fun(lst)
for i in gen:
    print(i)