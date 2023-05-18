
lst = [[1, 5, 3], [44, 2, 1], [1, 3]]
def f(l):
    t = ''
    for i in l:
        t += str(i)
    return len(t)
l = sorted(lst, key=lambda x: f(x))
print(l)
l1 = sorted(lst, key=lambda x: len(''.join([str(j) for j in x])))
print(l1)
