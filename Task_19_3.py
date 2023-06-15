class Person:
    def __init__(self, n1, n2, n3):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
    def __repr__(self):
        return f'{self.n1}{self.n2}{self.n3}'[::-1]


p = Person('Рэй', 'Дуглас', 'Брэдбери')
print(p)
