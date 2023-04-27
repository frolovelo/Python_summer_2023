x, y = int(input()), int(input())
a1 = x + y
a2 = x - y
a3 = x * y
a4 = x / y
a5 = x // y
result = [a1, a2, a3, a4, a5]
res = 0

if a1 >= a2:
    if a1 >= a3:
        if a1 >= a4:
            if a1 >= a5:
                res = a1
            else:
                res = a5

if a2 >= a1:
    if a2 >= a3:
        if a2 >= a4:
            if a2 >= a5:
                res = a2
            else:
                res = a5

if a3 >= a1:
    if a3 >= a2:
        if a3 >= a4:
            if a3 >= a5:
                res = a3
            else:
                res = a5
if a4 >= a1:
    if a4 >= a2:
        if a4 >= a3:
            if a4 >= a5:
                res = a4
            else:
                res = a5
if a5 >= a1:
    if a5 >= a2:
        if a5 >= a3:
            if a5 >= a4:
                res = a5
            else:
                res = a4
print(f'Максимум {res}')
print(f'Список чисел для удобства: {result}')