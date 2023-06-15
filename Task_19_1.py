'''itertools перебор купюр'''
from itertools import *
k = [50, 100, 200, 500, 1000, 2000, 5000]
for i in range(1, len(k)+1):
    print(f'{i} куп: ', end='')
    for j in combinations(k, i):
        print(sum(j), end=',')
    print()