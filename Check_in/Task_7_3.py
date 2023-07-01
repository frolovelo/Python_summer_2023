'''Матрица сортировка?'''
from math import inf


def matrix(n, m, mat):
    m1, m2, m3 = -inf, -inf, -inf
    for i in range(n):
        for j in range(m):
            if mat[i][j] > m1:
                m3 = m2
                m2 = m1
                m1 = mat[i][j]
            elif mat[i][j] > m2:
                m3 = m2
                m2 = mat[i][j]
            elif mat[i][j] > m3:
                m3 = mat[i][j]

    return [m3, m2, m1]


n, m = 2, 3
x = [[6, 2, 3], [1, 2, 4]]
print(matrix(n, m, x))