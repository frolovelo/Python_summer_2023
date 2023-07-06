'''Счётчик иневерсий'''


def count_inverse(lst):
    res = 0
    for a1, b1 in enumerate(lst):
        for a2, b2 in enumerate(lst):
            if a1 < a2 and b1 > b2:
                res += 1
    return res


lst = [[5, 4, 3, 2, 1], [1, 2, 3, 4, 5], [2, 1], [1, 2], [1, 1], [0], []]
for i in lst:
    print(i, '-->', count_inverse(i))
