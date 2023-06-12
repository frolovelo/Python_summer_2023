class Shape:
    def __init__(self, color, square):
        self.color = color
        self.square = square

    def change_color(self, color):
        self.color = color

    def what_color(self):
        print(f'Цвет объекта: {self.color}')

    def change_square(self, square):
        self.square = square

    def what_square(self):
        print(f'Площадь объекта: {self.square}')


a = Shape('red', 9)
print('Стартовые: ', a.color, a.square)
print()
a.change_color('blue')
print(a.color, a.square)
a.what_color()
a.change_square(7)
print(a.color, a.square)
a.what_square()