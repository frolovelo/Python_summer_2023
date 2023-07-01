'''Декоратор @property'''

class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if 1 <= age <= 100:
            self._age = age
            print('Good')
        else:
            print(f'Недопустимый возраст - {age}')

    @age.deleter
    def age(self):
        del self._age


matroskin = Person(3.5)
matroskin.age = 101
print(matroskin.age)
