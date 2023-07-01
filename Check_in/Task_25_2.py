'''Непоследовательные числа из списка'''


def noob(lst, step):
    res = []
    for i in range(len(lst) - 1):
        if lst[i] + step != lst[i + 1]:
            res.append(lst[i + 1])
    return res


lst = [1, 5, 6, 7, 9, 10]
print(noob(lst, 1))
