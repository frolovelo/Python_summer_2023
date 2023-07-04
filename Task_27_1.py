'''Матрица Дартс'''
n = int(input())
d = {}
for i in range(n):
    for j in range(n):
        d[i, j] = 0
x, y = 0, 0
dx, dy = 0, 1
d[x, y] = 1
c = 1
for _ in range(2, n*n+1):
    while True:
        x_n, y_n = x + dx, y + dy
        if d.get((x_n, y_n), -1) == 0:
            d[x_n, y_n] = c
            x += dx
            y += dy
            break
        else:
            if (dx, dy) == (0, 1):  dx, dy = 1, 0 # право
            elif (dx, dy) == (1, 0):  dx, dy = 0, -1 # вниз
            elif (dx, dy) == (0, -1):  dx, dy = -1, 0 # влево
            elif (dx, dy) == (-1, 0):
                dx, dy = 0, 1 # вверх!!!
                c += 1
# Вывод
for i in range(n):
    for j in range(n):
        print(str(d[i, j]), end=' ')
    print()