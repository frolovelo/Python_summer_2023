'''Класс item - setter, getter'''


class Item:
    def __init__(self, name, price, quantity):
        self._name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value.title()

    @property
    def total(self):
        return self.price * self.quantity

    # Total можно и так, вроде
    # def __getattr__(self, item):
    #     if item == 'total':
    #         return self.price * self.quantity
    #     else:
    #         return f'сlass Item не имеет атрибута: {item}'


a = Item('dan', 900, 2)
a.name = 'marivanna'
print(a.name)
print(a.total)
