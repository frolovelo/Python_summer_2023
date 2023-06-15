from itertools import *
k = [50, 100, 200, 500, 1000, 2000, 5000]
for i in range(2, len(k)+1):
    status = 'купюры' if 2 <= i <= 4 else 'купюр'
    print(f'{i} {status}: ', end='')
    for j in combinations(k, i):
        print(sum(j), end=',')
    print()