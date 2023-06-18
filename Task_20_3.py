'''itertools Генератор A-Z'''
from itertools import cycle, chain


class IterFrolTools:
    def __init__(self):
        self.chars = [chr(i) for i in range(65, 91)]
        self.numbers = [i for i in range(1, 27)]
        self.gen = cycle(chain.from_iterable(zip(self.chars, self.numbers)))

    def __iter__(self):
        return self

    def __next__(self):
        for i in self.gen:
            return i


az = IterFrolTools()
for _ in range(80):
    res = next(az)
    print(res, end=',')
    if res == 26:
        print()