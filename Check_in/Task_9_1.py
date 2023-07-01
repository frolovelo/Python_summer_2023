'''ДНК в РНК'''
def dnk_to_rnk(dnk):
    d = {'G': 'C',
         'T': 'A',
         'C': 'G',
         'A': 'T'}
    rnk = ''
    for i in dnk:
        n = d.get(i, 0)
        if n == 0:
            return 'Это не ДНК!'
        rnk += n
    return rnk


print(dnk_to_rnk(input('Введите ДНК: ')))
