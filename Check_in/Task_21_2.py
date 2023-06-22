'''Матрица кратчайший путь'''
from math import inf

matrix = [[10, 20, 30], [5, 1, 80], [90, 2, 70]]


def min_matrix(matrix, n=len(matrix)):
    # Для удобства вывода матриц
    def mtx(matrix):
        for x in matrix:
            for s in x:
                print(f'{str(s):5}', end='')
            print()
        print('-' * 20)

    # Создаём свою матрицу для рассчётов
    mem = [[inf for _ in range(n)] for _ in range(n)]
    mtx(matrix)

    # Расчитываем последний столбец и нижнюю строку
    mem[n - 1][n - 1] = matrix[n - 1][n - 1]
    # Расчёт правого столбца и нижней строки
    for i in reversed(range(n - 1)):  # 1, 0
        mem[n - 1][i] = matrix[n - 1][i] + mem[n - 1][i + 1]  # mem[2][1] = matrix[2][1] + mem [2][2]
        mem[i][n - 1] = matrix[i][n - 1] + mem[i + 1][n - 1]  # mem[1][2] = matrix[1][2] + mem [2][2]
    # mtx(mem)
    # Расчёт оставшейся части матрицы
    for i in reversed(range(n - 1)):  # 1, 0
        for j in reversed(range(n - 1)):  # 1, 0
            if mem[i][j] > mem[i][j + 1] + matrix[i][j]:  # если inf > 150 + 1
                mem[i][j] = mem[i][j + 1] + matrix[i][j]  # mem[1][1] = 151
            if mem[j][i] > mem[j + 1][i] + matrix[j][i]:  # если 151 > 72 + 1
                mem[j][i] = mem[j + 1][i] + matrix[j][i]  # mem[1][1] = 73
    # mtx(mem)

    # Ищем кратчайший путь
    i, j = 0, 0
    res = []
    while True:
        res.append(matrix[j][i])
        if i == n - 1 and j == n - 1:
            break
        if j < n - 1:
            if mem[j][i] - matrix[j][i] == mem[j + 1][i]:
                j += 1
                continue
        if i < n - 1:
            if mem[j][i] - matrix[j][i] == mem[j][i + 1]:
                i += 1
                continue
    print('Минимальный путь =', sum(res))
    print(' -> '.join(map(str, res)))


min_matrix(matrix)
