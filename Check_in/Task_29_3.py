'''Изомофрные слова'''


def izomorf(text):
    t1, t2 = text.split()
    if len(t1) != len(t2): return False
    tzip = zip(t1, t2)
    d = {}
    for i in tzip:
        d[i[0]] = i[1]
        if d.get(i[0], i[1]) != i[1]:
            return False
        if list(d.values()).count(i[1]) > 1:
            return False
    return True


lst = ['CBAABC DEFFED', 'XXX YYY', 'RAMBUNCTIOUSLY THERMODYNAMICS', 'AB CC', 'XXY XYY', 'ABAB CD']
for t in lst:
    print(t, '-', izomorf(t))
